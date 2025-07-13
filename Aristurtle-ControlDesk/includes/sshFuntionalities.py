from PySide6.QtCore import (QThread, Signal)
import paramiko 
from scp import SCPClient
import csv
import scipy.io


        

class SSHFunc(QThread):

    output = Signal(list)

    def __init__(self, parent= None):
        super().__init__(parent)
        self.ssh_username = ""
        self.ssh_hostname = ""
        self.ssh_password = ""

        self.mode = ""
        self.target_path = ""
        self.destination_path = ""
        self.command = ""
        
    def set_mode(self, mode):
        self.mode = mode
    def set_target_path(self, path):
        self.target_path = path
    def set_destination_path(self, path):
        self.destination_path = path
    def set_command(self, path):
        self.command = path


    def run(self):
        # Create an SSH client instance
        ssh = paramiko.SSHClient()
        # Automatically add host keys
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        if self.mode=="get":
            try:
                # Connect to the SSH server
                ssh.connect(self.ssh_hostname, username=self.ssh_username, password=self.ssh_password)
                # Create an SCP client
                with SCPClient(ssh.get_transport()) as scp:
                    # Get the file from the remote server
                    scp.get(self.target_path, self.destination_path)        
                self.output.emit(0)
            except Exception as e:
                self.output.emit(1)
            finally:
                # Close the SSH connection
                ssh.close()

        elif self.mode=="send":
            try:
                # Connect to the SSH server
                ssh.connect(self.ssh_hostname, username=self.ssh_username, password=self.ssh_password)          
                # Create an SCP client
                with SCPClient(ssh.get_transport()) as scp:
                    # Send the file to the remote server
                    scp.put(self.target_path, self.destination_path)     
                self.output.emit(2)
            except Exception as e:
                self.output.emit(3)
            finally:
                # Close the SSH connection
                ssh.close()

        elif self.mode=="command":
            try:
                # Connect to the SSH server
                ssh.connect(self.ssh_hostname, username=self.ssh_username, password=self.ssh_password)
                
                # Execute the command to delete the file
                ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(self.command)
                self.output.emit(ssh_stdout.readlines())
                

            except Exception as e:
                print(f"Error: {e}")
            
            finally:
                # Close the SSH connection
                ssh.close()
        else:
            self.output.emit(4)

        
            
# class DatafileConversion(QThread):

#     output = Signal(int)

#     def __init__(self, parent= None):
#         super().__init__(parent)
#         self.var_names = []
#         self.csv_file_path = ""

        
    
#     def run(self):
#         mat_file_path = self.csv_file_path[:-3]+"mat"
#         rows = []
#         with open(self.csv_file_path, 'r') as csvfile:
#             reader = csv.reader(csvfile)
#             for row in reader:
#                 rows.append(row)
        
#         # CHECK IF IT NEEDS int(row[0])-1
#         for row in rows:
#             row[0] = self.var_names[int(row[0])]

#         # Structure the data for .mat 
#         data_for_matlab = {}
#         for row in rows:
#             variable_name, value, timestamp = row
#             if variable_name not in data_for_matlab:
#                 data_for_matlab[variable_name] = {
#                     "Name": variable_name,
#                     "Values": [],
#                     "Timestamps": []
#                 }
                
#             data_for_matlab[variable_name]["Values"].append(float(value))
#             data_for_matlab[variable_name]["Timestamps"].append(int(timestamp)/100)

#         # Export data to .mat file
#         matfile = {"Data":data_for_matlab, "Description": 1}
#         scipy.io.savemat(mat_file_path, matfile )

#         self.output.emit(1)