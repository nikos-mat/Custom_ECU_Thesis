import serial 
import struct
import paho.mqtt.client as paho
import sys   

# UART Initialization
uart2 = "/dev/ttyAMA1" # pins: 27,28
uart3 = "/dev/ttyAMA2" # pins: 7,29
uart1 = "/dev/ttyAMA0" # pins: 8,10
port = uart3

# Choose the maximum baudrate for the Rspberry Pi
baudrate = 2000000

# MQTT Initialization
host = "192.168.137.120"
client = paho.Client("Control Embedded")
client.username_pw_set("username", "password")
if client.connect(host,1883,60) != 0:
    print("No connect")
    sys.exit(-1)
else:
    print("MQTT Connected")

# UART Initialization 
ser = serial.Serial(port, baudrate)
if ser.is_open:
    print("UART Conected")

sent_packets = 0
# UART Communication Loop
try:
    while True:
        # If there are bytes available in the UART
        if ser.in_waiting>0:
            # Read the first byte containing: Starter Frame, Topic, A part of the id
            first_byte_dec = int.from_bytes(ser.read(1),'big', signed = False)
            # Isolate the starter frame
            starter = first_byte_dec >> 4
            if starter == 11: # == 1011
                # Isolate the topic bits
                dataloggib_bit = (first_byte_dec- 176)>>2 # 176 is the  11 shifted left by 4
                # Isolate the 2 bits for the id
                extra_id_bits_contribution= (first_byte_dec - 176 - dataloggib_bit*4)<<8
                # Read the remaining id_frame bits
                second_byte_dec = int.from_bytes(ser.read(1),'big', signed = False)
                # Get the full id_frame
                var_id =  second_byte_dec + extra_id_bits_contribution +1
                # Read the value as float
                value = struct.unpack('f',ser.read(4))
                value = value[0]

                # Construct the mqtt message: "Id:Value"
                mqtt_packet = str(var_id) + ":" + str(value)
                # If the Topic is 01: Publish in main_vars(Datalogging) for both Datalogging and Streaming
                # Else: Publish on streaming vars for Streaming only
                if dataloggib_bit:
                    pubStatus = client.publish("VCU/main_vars", mqtt_packet, 0)
                else:
                     pubStatus = client.publish("VCU/streaming_vars", mqtt_packet, 0)

                if(pubStatus[0] != 0):
                    print("MQTT Tx Failed")
                sent_packets+=1
      
except KeyboardInterrupt:
    print("")
    print(sent_packets)
    print(ser.in_waiting)
    ser.close() 


