import paho.mqtt.client as paho
import sys
import csv
import time
import datetime 
import threading

# Automatically subscribe to the topic, when the client connects to the Broker
def onConnect(client, userdata, flags, rc):
    client.subscribe("VCU/main_vars")

# Open the csv file and write the data in the csv
def save_data_to_csv(data):
    with open(databaseRelPath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

# function that will be called by a thread (includes mechanisms for safety)
def save_data(buff):
    # modify a global variable that is a flag for whether the function 
    # is running or not
    global thread_running
    thread_running = 1
    print("working")
    # modify a global variable that counts the number of saves
    global numSaves
    numSaves = numSaves + 1

    print(len(buff))
    # save the data buffer
    save_data_to_csv(buff)

    thread_running = 0
    print("resting")

# Function that is called when a message is received from MQTT and 
# appends the information to the buffer
# coding is "var_id:value"
def onMessage(client, userdata, msg):
    global mqttRx
    mqttRx = mqttRx + 1

    data = msg.payload.decode()
    ind = data.find(':')
    var_id = data[0:ind]
    timestamp = int((time.time() - startTime)*100)
    value = int(data[ind+1:])

    global buffer
    buffer.append([var_id, value, timestamp])

    # If tthe buffer length is above the threshold, the saving process 
    # begins and the buffer is cleared
    global thread_running
    if len(buffer)>saving_threshold and thread_running==0:
        # copy the buffer to another buffer so the one can be saved 
        # and the other is cleared to be refilled
        buff = buffer.copy()
        print("buff new value")
        saver_thread = threading.Thread(target = save_data, args = [buff])
        saver_thread.start()
        # save_data(buff)
        buffer.clear()

       
# Number of packets received before saving
saving_threshold = 1000 - 1

# Initialize MQTT Connection
host = "192.168.137.120"
client = paho.Client("Datalogger")
client.username_pw_set("AristurtleECU","aristurtle!@#") 
client.on_connect = onConnect
client.on_message = onMessage      

# Generate file path according to the current date and time
dt = datetime.date.today()
today = dt.strftime("%d%m%Y")
t = time.localtime()
current_time = time.strftime("%H%M%S", t)
name = "data_" + today + "_" + current_time + ".csv"
databaseRelPath = "../Datafiles_CSV/" + name

# MQTT Connection
if client.connect(host) != 0:
    print("Connection failed to the host: {}".format(host))
    sys.exit(-1)
print("Connected to the host: {}".format(host))

# Initialize Variables
buffer = []
mqttRx = 0
numSaves = 0
startTime = time.time()
thread_running = 0

# Enter MQTT Rx loop
try:
    print("Press CTRL+C to exit")
    client.loop_forever()
except:
    print("\nDisconnecting from Broker")

# Code after exception
client.disconnect()
stop_saving = 1
print(mqttRx)
print(numSaves)
sys.exit()



