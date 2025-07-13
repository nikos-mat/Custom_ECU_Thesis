import threading
import subprocess
import time
import os
import re
import struct
import paho.mqtt.client as paho


SVtoG_fifo_path = "/tmp/SVtoG_fifo"
SVtoC_fifo_path = "/tmp/SVtoC_fifo"


def get_cpu_temp_vcgencmd():
    try:
        output = subprocess.check_output(["vcgencmd", "measure_temp"]).decode()
        return output.split('=')[1].split("'")[0]
    except Exception:
        return None
    
def onDisconnect(client, userdata,rc=0):
    client.loop_stop()

def onConnect(client, userdata, flags, rc):
    client.subscribe("ARCODE/tuning")

def onMessage(clien, userdata, msg):
    message = msg.payload.decode()
    
    if msg.topic == "ARCODE/tuning":
        parts = message.split(',')
        mcu_name = parts[0]
        value = float(parts[1])
        index = int(parts[2])
        data_bytes = struct.pack('<BHfH', 36 , index, value, index)
        if mcu_name=="Control":
            with open(SVtoC_fifo_path, 'wb') as fifo:
                print(data_bytes)
                fifo.write(data_bytes)
                fifo.flush()
        elif mcu_name=="General":
            with open(SVtoG_fifo_path, 'wb') as fifo:
                fifo.write(data_bytes)
                fifo.flush()

# Function to run a .o file
def run_o_file(file_name):
    subprocess.run(["./Cpp_Packets/" + file_name])

# fucntion that reads the ip using ifconfig
def get_ip_from_ifconfig(interface="wlan0"):
    try:
        result = subprocess.check_output(["ifconfig", interface]).decode()
        match = re.search(r"inet (\d+\.\d+\.\d+\.\d+)", result)
        if match:
            return match.group(1)
    except subprocess.CalledProcessError:
        pass
    return None

if __name__ == "__main__":
    # Find the ip and write it in txt, for the Logging&Streaming to read
    host = get_ip_from_ifconfig()
    with open("states/current_ip.txt", "w") as file:
        file.write(host)

    # Open the communication Fifos with the transceivers
    if not os.path.exists(SVtoG_fifo_path):
        os.mkfifo(SVtoG_fifo_path)
    if not os.path.exists(SVtoC_fifo_path):
        os.mkfifo(SVtoC_fifo_path)

    # MQTT Initialization
    count = 0
    client = paho.Client(paho.CallbackAPIVersion.VERSION1, "Supervisor")
    client.username_pw_set("AristurtleECU", "aristurtle!@#")
    client.on_connect = onConnect
    client.on_disconnect = onDisconnect
    client.on_message = onMessage
    while client.connect(host,1883,60) != 0:
        print("No connect")
        time.sleep(1)
    client.loop_start()

    
    # List of .o file names
    o_files = ["general_transceiver", "control_transceiver", "Logging&Streaming"]
    # List to store thread objects
    threads = []

    # Start threads for each .o file
    for file_name in o_files:
        thread = threading.Thread(target=run_o_file, args=(file_name,))
        thread.daemon = True
        thread.start()

        threads.append(thread)
        time.sleep(0.1)
    
    
    try:
        while(1): 
            # Read the vcu states info and publish it every 1 sec
            time.sleep(1)
            temp = get_cpu_temp_vcgencmd()
            with open("states/general_state.txt", "r") as file:
                g_active = file.read()
            with open("states/control_state.txt", "r") as file:
                c_active = file.read()
            with open("states/logging_state.txt", "r") as file:
                last_logging = file.read()
            message = temp + ',' + g_active + ',' + c_active + ',' + last_logging 
            client.publish("VCU/state", message)

    
    except KeyboardInterrupt:
        client.loop_stop()
        exit(0)

    
        