# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtGui import (QIcon, QPixmap)
from PySide6.QtGui import QCloseEvent
from QT.ui_mainwindow import Ui_MainWindow
import pandas as pd
import math
import struct
import scipy
from tkinter import filedialog
import os
import tkinter as tk
import json 

from includes.connectivity import (pingThread,MQTT)
from includes.sshFuntionalities import (SSHFunc)
from includes.datafile_conversion import (csv2mat)
import paramiko 
from scp import SCPClient


SOURCE_FILE  = "..//Source Variable File//VariablePackets.xlsx"
bootloader_load = 0

blue = ".\\Qt\\images\\blue-led.png"
green = ".\\Qt\\images\\green-led.png"
red = ".\\Qt\\images\\red-led.png"
off = ".\\Qt\\images\\off-led.png"

class Mainwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    # Window init/close functions
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("ARCODE")

        self.ping_thread = pingThread()
        self.mqtt = MQTT()
        # self.datafile_convert = DatafileConversion()
        self.sshFunc_thread = SSHFunc()

        # Read catalogs should be first
        self.read_catalogs()
        self.read_defaults()
        
        self.init_leds()
        self.buttonFunctionality()

        self.mqtt_connected = False

    def buttonFunctionality(self):
        self.ping_pushButton.clicked.connect(self.ping_ip)
        self.connect_pushButton.clicked.connect(self.mqtt_connection)
        self.control_refresh_files_button.clicked.connect(self.refresh_folder_control)
        self.general_refresh_files_button.clicked.connect(self.refresh_folder_general)
        self.refresh_datafiles_pushButton.clicked.connect(self.refresh_folder_datafiles)
        self.control_delete_file_button.clicked.connect(self.delete_file_control)
        self.general_delete_file_button.clicked.connect(self.delete_file_general)
        self.delete_datafiles_pushButton.clicked.connect(self.delete_datafile)
        self.control_transfer_file_button.clicked.connect(self.control_transmit_file)
        self.general_transfer_file_button.clicked.connect(self.general_transmit_file)
        self.control_choose_local_file_button.clicked.connect(self.control_choose_local_file)
        self.general_choose_local_file_button.clicked.connect(self.general_choose_local_file)
        self.download_datafiles_pushButton.clicked.connect(self.download_datafile)
        self.control_load_code_button.clicked.connect(self.control_load_code)
        self.general_load_code_button.clicked.connect(self.general_load_code)
        self.convert_pushButton.clicked.connect(self.convert_csv2mat)

        self.ip_lineEdit.textChanged.connect(self.ip_changed)
        self.client_name_lineEdit.textChanged.connect(self.client_name_changed)
        self.general_mcu_id_lineEdit.textChanged.connect(self.general_mcu_id_changed)
        self.control_mcu_id_lineEdit.textChanged.connect(self.control_mcu_id_changed)

        self.general_tune_refresh_pushButton.clicked.connect(self.general_tune_refresh)
        self.general_tune_pushButton.clicked.connect(self.general_tune_var)
        self.control_tune_refresh_pushButton.clicked.connect(self.control_tune_refresh)
        self.control_tune_pushButton.clicked.connect(self.control_tune_var)

        self.reboot_pi.clicked.connect(self.reboot_pi_command)
        self.poweroff_pi.clicked.connect(self.poweroff_pi_command)
        self.restart_supervisor.clicked.connect(self.restart_supervisor_command)
        self.stop_supervisor.clicked.connect(self.stop_supervisor_command)
        self.start_supervisor.clicked.connect(self.start_supervisor_command)

        self.general_reset_mcu_button.clicked.connect(self.general_reset_mcu)
        self.control_reset_mcu_button.clicked.connect(self.control_reset_mcu)
        
        
        
    def init_leds(self):
        self.connection_status_led.setPixmap(QPixmap(red))
        self.general_mcu_status_led.setPixmap(QPixmap(red))
        self.control_mcu_status_led.setPixmap(QPixmap(red))

    def read_catalogs(self):
        # source_file = "..//Variable Packets.xlsx"
        df_dl = pd.read_excel(SOURCE_FILE, sheet_name="Datalogging")
        df_st = pd.read_excel(SOURCE_FILE, sheet_name="Streaming")
        df = pd.concat([df_dl, df_st])

        available_packet_ids = set(df['Packet'])
        available_packet_ids = {x for x in available_packet_ids if not (isinstance(x, float) and math.isnan(x))}
        
        self.Variables_in_packet = dict()
        if available_packet_ids:
            for packet_id in available_packet_ids:
                self.Variables_in_packet[packet_id] = df[df['Packet'] == packet_id]
        self.dataframe = df
        
        self.Variable_Values = dict()
        for var_name in df['Variable']:
            if not (isinstance(var_name, float) and math.isnan(var_name)):
                self.Variable_Values[var_name] = [0]
        for i,name in enumerate(self.Variable_Values.keys()):
            if isinstance(name, str):
                self.main_tableWidget_1.insertRow(self.main_tableWidget_1.rowCount())
                self.main_tableWidget_1.setItem(i, 0, QtWidgets.QTableWidgetItem(name))


        

    
    def read_defaults(self):
        with open("defaults.txt","r") as txt:
            lines = txt.readlines()
        # mqtt
        self.mqtt.host_ip = self.find_default_value(lines,"host_ip")
        self.mqtt.port = self.find_default_value(lines,"port")
        self.mqtt.username = self.find_default_value(lines,"username")
        self.mqtt.password = self.find_default_value(lines,"password")
        self.mqtt.main_topic = self.find_default_value(lines,"main_topic")
        self.mqtt.arcode_topic = self.find_default_value(lines,"arcode_topic")
        self.mqtt.client_name = self.find_default_value(lines,"client_name")
        # file_transfer
        self.sshFunc_thread.ssh_username =self.find_default_value(lines,"ssh_username")
        self.sshFunc_thread.ssh_hostname = self.find_default_value(lines,"ssh_hostname")
        self.sshFunc_thread.ssh_password = self.find_default_value(lines,"ssh_password")
        # programming
        self.general_mcu_id = self.find_default_value(lines,"general_mcu_id")
        self.control_mcu_id = self.find_default_value(lines,"control_mcu_id")
        #
        self.source_file = self.find_default_value(lines,"source_file")

        self.control_destination_path_lineEdit.setText(self.find_default_value(lines,"vcu_control_firmware_path"))
        self.general_destination_path_lineEdit.setText(self.find_default_value(lines,"vcu_general_firmware_path"))
        self.target_folder_lineEdit.setText(self.find_default_value(lines,"vcu_datafile_path"))
        self.ip_lineEdit.setText(self.mqtt.host_ip)
        self.client_name_lineEdit.setText(self.mqtt.client_name)
        self.general_mcu_id_lineEdit.setText(self.general_mcu_id)
        self.control_mcu_id_lineEdit.setText(self.control_mcu_id)
    
    def find_default_value(self, lines, name_to_search):
        i=0
        for line in lines:
            ind = str(line).find(name_to_search+"=")
            if ind == -1:
                i+=1
            else:
                return line[len(name_to_search)+1:-1]
        return ""  
    
    def closeEvent(self, event = None):
        super().closeEvent(event)
        if self.mqtt_connected:
            self.mqtt.stop_loop()
            self.mqtt.disconnect()
        event.accept()
    
    # Button functionality
    def ip_changed(self):
        self.mqtt.host_ip = self.ip_lineEdit.text()

    def client_name_changed(self):
        self.mqtt.client_name = self.client_name_lineEdit.text()

    def ping_ip(self):
        self.ping_output_label.setText("...")
        self.ping_thread.response.connect(self.ping_output)
        
        if not self.ping_thread.isRunning():
            ip = self.ip_lineEdit.text()
            self.ping_thread.set_ip(ip)
            self.ping_thread.start()
        
    def ping_output(self, response):
        if response == False:
            self.ping_output_label.setText("Failed")
        else:
            self.ping_output_label.setText("Succeed")
    
    def general_mcu_id_changed(self):
        self.general_mcu_id = self.general_mcu_id_lineEdit.text()
    
    def control_mcu_id_changed(self):
        self.control_mcu_id = self.control_mcu_id_lineEdit.text()

    def refresh_folder_general(self):
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.output.connect(self.list_general_files)
        self.sshFunc_thread.set_command(f"cd {self.general_destination_path_lineEdit.text()} && stat -c ""%y,%s,%n"" -- *")
        self.sshFunc_thread.start()

    def refresh_folder_control(self):
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.output.connect(self.list_control_files)
        self.sshFunc_thread.set_command(f"cd {self.control_destination_path_lineEdit.text()} && stat -c ""%y,%s,%n"" -- *")
        self.sshFunc_thread.start()
        
    def list_control_files(self, output):
        self.sshFunc_thread.output.disconnect()
        i=0
        self.control_binfiles_tableWidget.setRowCount(0)
        for file in output:
            [date, bytess, name] = file.split(',')
            kb = str(int(bytess)/1000)
            idx =date.find('.')
            date = date[:idx]
            name = name[:-1]
            self.control_binfiles_tableWidget.insertRow(self.control_binfiles_tableWidget.rowCount())
            self.control_binfiles_tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(date))
            self.control_binfiles_tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(kb))
            self.control_binfiles_tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(name))
            i+=1
    
    def list_general_files(self, output):
        self.sshFunc_thread.output.disconnect()
        self.general_binfiles_tableWidget.setRowCount(0)
        i=0
        for file in output:
            [date, bytess, name] = file.split(',')
            kb = str(int(bytess)/1000)
            idx =date.find('.')
            date = date[:idx]
            name = name[:-1]
            self.general_binfiles_tableWidget.insertRow(self.general_binfiles_tableWidget.rowCount())
            self.general_binfiles_tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(date))
            self.general_binfiles_tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(kb))
            self.general_binfiles_tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(name))
            i+=1

    def list_datafiles(self,output):
        self.sshFunc_thread.output.disconnect()
        self.datafiles_tableWidget.setRowCount(0)
        i=0
        for file in output:
            [date, bytess, name] = file.split(',')
            kb = str(int(bytess)/1000)
            idx =date.find('.')
            date = date[:idx]
            name = name[:-1]
            self.datafiles_tableWidget.insertRow(self.datafiles_tableWidget.rowCount())
            self.datafiles_tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(date))
            self.datafiles_tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(kb))
            self.datafiles_tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(name))
            i+=1
        
    def delete_file_general(self):
        i = self.general_binfiles_tableWidget.currentRow()
        name = self.general_binfiles_tableWidget.item(i,2).text()
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.set_command(f"cd {self.general_destination_path_lineEdit.text()} && rm {name}")
        self.sshFunc_thread.start()
    
    def delete_file_control(self):
        i = self.control_binfiles_tableWidget.currentRow()
        name = self.control_binfiles_tableWidget.item(i,2).text()
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.set_command(f"cd {self.control_destination_path_lineEdit.text()} && rm {name}")
        self.sshFunc_thread.start()

    def delete_datafile(self):
        i = self.datafiles_tableWidget.currentRow()
        name = self.datafiles_tableWidget.item(i,2).text()
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.set_command(f"cd {self.target_folder_lineEdit.text()} && rm {name}")
        self.sshFunc_thread.start()

    def control_choose_local_file(self):
        root = tk.Tk()
        root.withdraw()
        
        filepath = filedialog.askopenfilename(initialdir = "./",
                                          title = "Select a Firmware File",
                                          filetypes = (("Elf files",
                                                        "*.elf"), ("Hex files",
                                                        "*.hex"),("Binary files",
                                                        "*.bin"),))
        self.control_local_path_lineEdit.setText(filepath)
        
    def general_choose_local_file(self):
        root = tk.Tk()
        root.withdraw()
        
        filepath = filedialog.askopenfilename(initialdir = "./",
                                          title = "Select a Firmware File",
                                          filetypes = (("Elf files",
                                                        "*.elf"), ("Hex files",
                                                        "*.hex"),("Binary files",
                                                        "*.bin"),))
        self.general_local_path_lineEdit.setText(filepath)

    def refresh_folder_datafiles(self):
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.output.connect(self.list_datafiles)
        self.sshFunc_thread.set_command(f"cd {self.target_folder_lineEdit.text()} && stat -c ""%y,%s,%n"" -- *")
        self.sshFunc_thread.start()

    def control_transmit_file(self):
        self.sshFunc_thread.set_mode("send")
        self.sshFunc_thread.set_target_path(self.control_local_path_lineEdit.text())
        self.sshFunc_thread.set_destination_path(self.control_destination_path_lineEdit.text())
        self.sshFunc_thread.start()
    
    def general_transmit_file(self):
        self.sshFunc_thread.set_mode("send")
        self.sshFunc_thread.set_target_path(self.general_local_path_lineEdit.text())
        self.sshFunc_thread.set_destination_path(self.general_destination_path_lineEdit.text())
        self.sshFunc_thread.start()

    def download_datafile(self):
        root = tk.Tk()
        root.withdraw()
        
        folder_path = filedialog.askdirectory(
            initialdir="./",
            title="Select a Folder"
        )
        i = self.datafiles_tableWidget.currentRow()
        name = self.datafiles_tableWidget.item(i,2).text()
        target_path = self.target_folder_lineEdit.text() + "/" + name
        self.sshFunc_thread.set_mode("get")
        self.sshFunc_thread.set_target_path(target_path)
        self.sshFunc_thread.set_destination_path(folder_path)
        self.sshFunc_thread.start()
    
    def control_load_code(self):
        i = self.control_binfiles_tableWidget.currentRow()
        name = self.control_binfiles_tableWidget.item(i,2).text()
        path = self.control_destination_path_lineEdit.text() + name
        if bootloader_load:
            command = "raspi-gpio set 15 op dh; raspi-gpio set 24 op dh; sleep 0.1; raspi-gpio set 24 op dl; raspi-gpio set 15 op dl;" \
            "stm32loader --port /dev/ttyAMA1 --erase --write --verify {}".format(path)
        else:
            command = "pyocd flash -t STM32H723VGTx --format elf -u {} {}".format(self.control_mcu_id_lineEdit.text(), path)
        
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.set_command(command)
        self.sshFunc_thread.start()
    
    def general_load_code(self):
        i = self.general_binfiles_tableWidget.currentRow()
        name = self.general_binfiles_tableWidget.item(i,2).text()
        path = self.general_destination_path_lineEdit.text() + name
        if bootloader_load:
            command = "raspi-gpio set 16 op dh; raspi-gpio set 26 op dh; sleep 0.1; raspi-gpio set 26 op dl; raspi-gpio set 16 op dl;" \
            "stm32loader --port /dev/ttyAMA2 --erase --write --verify {}".format(path)
        else:
            command = "pyocd flash -t STM32H723VGTx --format elf -u {} {}".format(self.general_mcu_id_lineEdit.text(), path)
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.set_command(command)
        self.sshFunc_thread.start()

    def general_reset_mcu(self):
        command = "raspi-gpio set 26 op dh; sleep 0.1; raspi-gpio set 26 op dl"
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.set_command(command)
        self.sshFunc_thread.start()

    def control_reset_mcu(self):
        command = "raspi-gpio set 24 op dh; sleep 0.1; raspi-gpio set 24 op dl"
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.set_command(command)
        self.sshFunc_thread.start()

    def control_tune_refresh(self):
        df_tune_control = pd.read_excel(SOURCE_FILE, sheet_name="ParametersControl")
        names = df_tune_control['Name'].dropna().astype(str).tolist()
        self.control_tune_dict = {name: idx + 1 for idx, name in enumerate(names)}
        
        self.control_tuning_vars_comboBox.clear()
        self.control_tuning_vars_comboBox.addItems(self.control_tune_dict.keys())

    def control_tune_var(self):
        chosen_Var = self.control_tuning_vars_comboBox.currentText()
        string_value = self.control_tuning_value_lineEdit.text()
        try:
            value =  float(string_value)
            if self.mqtt_connected and chosen_Var!='None':
                
                self.mqtt.sendMessage("toVCU/tuning",f'Control,{value},{self.control_tune_dict[chosen_Var]}')
                
            else:
                print("No connection")
        except (ValueError, TypeError):
            print("no numb")
            pass

    def general_tune_refresh(self):
        df_tune_general = pd.read_excel(SOURCE_FILE, sheet_name="ParametersGeneral")
        names = df_tune_general['Name'].dropna().astype(str).tolist()
        self.general_tune_dict = {name: idx + 1 for idx, name in enumerate(names)}
        
        self.general_tuning_vars_comboBox.clear()
        self.general_tuning_vars_comboBox.addItems(self.general_tune_dict.keys())

    def general_tune_var(self):
        chosen_Var = self.general_tuning_vars_comboBox.currentText()
        string_value = self.general_tuning_value_lineEdit.text()
        try:
            value =  float(string_value)
            if self.mqtt_connected and chosen_Var!='None' :
                # print(f'General,{value},{self.general_tune_dict[chosen_Var]}')
                self.mqtt.sendMessage("toVCU/tuning",f'General,{value},{self.general_tune_dict[chosen_Var]}')
                print(f'General,{value},{self.general_tune_dict[chosen_Var]}')
            else:
                print("No connection")
        except (ValueError, TypeError):
            print("no numb")
            pass

    def reboot_pi_command(self):
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.set_command("sudo reboot")
        self.sshFunc_thread.start()
    
    def poweroff_pi_command(self):
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.set_command("sudo poweroff")
        self.sshFunc_thread.start()

    def stop_supervisor_command(self):
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.set_command("systemctl stop spawnECU.service")
        self.sshFunc_thread.start()
    
    def start_supervisor_command(self):
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.set_command("systemctl start spawnECU.service")
        self.sshFunc_thread.start()
    
    def restart_supervisor_command(self):
        self.sshFunc_thread.set_mode("command")
        self.sshFunc_thread.set_command("{systemctl stop spawnECU.service")
        self.sshFunc_thread.start()
            
        
        
    def convert_csv2mat(self):
        # file = r"C:\Users\nmata\Desktop\data_29102024_171830.csv"
        # if multi is selected choose many files
        # files = [path1, path2]
        # else choose one
        root = tk.Tk()
        root.withdraw()
        
        filepath = filedialog.askopenfilename(initialdir = "./",
                                          title = "Select a CSV File",
                                          filetypes = (("CSV files",
                                                        "*.csv"),))
        # if many files, sort them and merge them
        matfile = csv2mat(filepath, self.Variables_in_packet)

        # get matfiles new path
        matpath = filedialog.askdirectory(title="Select Folder to Save the .mat File")
        filename = os.path.basename(filepath)[:-3] + "mat"
        matpath = matpath + "/" + filename
        matpath.replace("/", "\\" )
        # matpath = r"C:\Users\nmata\Desktop\data_29102024_171830.mat"

        scipy.io.savemat(matpath, matfile )
        print("done")




    # MQTT functionality
    def mqtt_connection(self):
        if not self.mqtt_connected:
            
            if self.mqtt.client_name == "":
                self.connection_status_label.setText("Add Client Name")
            else:
                try:
                    self.mqtt.connect_to_host()
                    self.mqtt.client.on_message = self.onMessage 
                    self.mqtt.start_loop()
                    self.mqtt_connected = True
                    self.connect_pushButton.setText("Disconnect")
                    self.connection_status_label.setText("Connected")
                    self.connection_status_led.setPixmap(QPixmap(green))
                except TimeoutError:
                    self.connection_status_label.setText("TimeoutError: Failed to Connect")
        else:
            self.mqtt.stop_loop()
            self.mqtt.disconnect()
            self.mqtt_connected = False
            self.connection_status_led.setPixmap(QPixmap(red))
            self.connect_pushButton.setText("Connect")
            self.connection_status_label.setText("Disconnected")

    def onMessage(self, client, userdata, msg):
        topic = msg.topic
        message = msg.payload.decode()
        
        if topic == "VCU/state":
            parts = message.split(',')
            temp = parts[0]
            self.temperature_value_label.setText(temp)
            g_active = parts[1]=='Active'
            if g_active: 
                self.general_mcu_status_led.setPixmap(QPixmap(green))
            else:
                self.general_mcu_status_led.setPixmap(QPixmap(red))
            c_active = parts[2]=='Active'
            if c_active: 
                self.control_mcu_status_led.setPixmap(QPixmap(green))
            else:
                self.control_mcu_status_led.setPixmap(QPixmap(red))
            last_log = str(float(parts[3])/60) + ":" + str(float(parts[3])%60)
            self.datalogging_timestamp_value.setText(last_log)
        elif topic == "toARCODE/variables":
            try:
            
                packets = message.split('\n')[:-1]
                # print(packets)
                for line in packets:
                    parts = line.split(',')
                    parts = [eval(i) for i in parts]
                    packet_id = parts[0]
                    time = parts[1]
                    data = parts[2:]

                    scaling = self.Variables_in_packet[packet_id]['Scaling'].to_list()
                    datatype = self.Variables_in_packet[packet_id]['Data_Type'].to_list()
                    num_bytes = self.Variables_in_packet[packet_id]['Bytes'].to_list()
                    names = self.Variables_in_packet[packet_id]['Variable'].to_list()

                    idx1 =0
                    idx2 = 0
                    for i in range(len(num_bytes)):
                        idx1=idx2
                        idx2+= num_bytes[i]
                        encoded = data[idx1:idx2]
                        
                        self.Variable_Values[names[i]] = [decode_bytes(encoded,datatype[i])/scaling[i]]
                self.update_all_variable_list()
            except:
                print(f"id:{packet_id} i:{i}, name: {names[i]} bytes:{encoded}, datatype:{datatype[i]} ")
        
    
    
    def update_all_variable_list(self):
        for i,name in enumerate(self.Variable_Values.keys()):
            # print(f"{name}  {self.Variable_Values[name][-1]}")
            self.main_tableWidget_1.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.Variable_Values[name][-1])))
   
    
def decode_bytes(byte_list, data_type):
    # Convert the list of bytes to a bytes object (struct requires a bytes-like object)
    byte_data = bytes(byte_list)
    
    # Define format strings for the given data types
    formats = {
        'int16': 'h',     # signed 16-bit integer
        'uint16': 'H',    # unsigned 16-bit integer
        'int8': 'b',      # signed 8-bit integer
        'uint8': 'B',     # unsigned 8-bit integer
        'single': 'f',    # 32-bit floating point (single precision)
        'int32': 'i',     # signed 32-bit integer
        'uint32': 'I',    # unsigned 32-bit integer
    }
    
    # Check if the provided data type exists in the format dictionary
    if data_type not in formats:
        raise ValueError(f"Unsupported data type: {data_type}")
    
    # Decode the bytes using struct.unpack() based on the format for the data type
    result = struct.unpack(formats[data_type], byte_data)
    
    # Since struct.unpack always returns a tuple, we return the first element
    return result[0]


def process_file(input_file, output_file):
    tunning_vars = []
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Trim spaces from the start and end of the line
            trimmed_line = line.strip()
            # Check if the line starts with "/* Variable: "
            if trimmed_line.startswith("/* Variable: "):
                # Write the rest of the line (after "/* Variable: ") to the output file
                variable_content = trimmed_line[len("/* Variable: "):]
                tunning_vars.append(variable_content)
    return tunning_vars