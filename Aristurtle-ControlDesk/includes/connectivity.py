from PySide6.QtCore import (QObject, QThread, Signal)
from pythonping import ping
import paho.mqtt.client as paho
import sys


class pingThread(QThread):

    response = Signal(bool)

    def __init__(self, ip_address= "", parent= None):
        super().__init__(parent)
        self.ip = ip_address
        
    def set_ip(self, ip):
        self.ip = ip

    def run(self):
        output = str(ping(self.ip, verbose=False, count=1)).find("Request timed out")
        if output == -1:
            response = True
        else:
            response = False
        self.response.emit(response)

class MQTT():
    
    def __init__(self):
        self.host_ip = ""
        self.port = ""
        self.main_topic= ""
        self.arcode_topic= ""
        self.username = ""
        self.password = ""
        self.client_name = ""
        

    def setup(self):
        self.client = paho.Client(paho.CallbackAPIVersion.VERSION2, client_id=self.client_name)
        self.client.username_pw_set(self.username, self.password) 
        self.client.on_connect = self.onConnect
        self.client.on_disconnect = self.onDisconnect



    def connect_to_host(self):
        self.setup()
        if self.client.connect(self.host_ip, int(self.port), 60) != 0:
            sys.exit(-1)

    
    def disconnect(self):
        self.client.disconnect()

    def start_loop(self):
        self.client.loop_start()
    
    def stop_loop(self):
        self.client.loop_stop()

    def onConnect(self,client, userdata, flags, rc, properties):
        client.subscribe(self.main_topic)
        client.subscribe(self.arcode_topic)
        client.subscribe("VCU/state")
        client.subscribe("VCU/file_explorer")

    def onDisconnect(self,client, userdata, flags, rc, properties):
        self.stop_loop()

    def sendMessage(self, topic, message):
        self.client.publish(topic, message)
        
    def onMessage(self, client, userdata, msg):
        message = msg.payload.decode()
        print(message)
        
