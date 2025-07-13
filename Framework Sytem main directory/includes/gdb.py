import time
import subprocess

mcu_ids = { "General": "003B001E3133510237363734", "Control": "0042001C3133510237363734" }
port = { "General": "3334", "Control": "3333" }
telnet_port = { "General": "4445", "Control": "4444" }

polling_interval = 0.1  # 10 ms
# pyocd gdbserver -p 3333 --telnet-port 4444 -t STM32H723VGTx -u 0042001C3133510237363734
# pyocd gdbserver -p 3334 --telnet-port 4445 -t STM32H723VGTx -u 003B001E3133510237363734
# args=[f"pyocd gdbserver -p {port[mcu_name]} --telnet-port {telnet_port[mcu_name]} -t STM32H723VGTx -u {mcu_ids[mcu_name]}"],
        
def set_parameter(mcu_name, elf_file, variable_name, value):
    #     ['gdb', '-ex','/home/mat/Documents/AristurtleProjects/ECU/Version_Control/Control/Control.elf', 'target remote localhost:3333', '-ex', 'set pagination off', '-ex', 'monitor reset halt', '-ex'],
    gdb_server = subprocess.Popen(
        args=[
        "pyocd", "gdbserver",
        "-p", port[mcu_name],
        "--telnet-port", telnet_port[mcu_name],
        "-t", "STM32H723VGTx",  
        "-u", mcu_ids[mcu_name]
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    while(1):
        output = gdb_server.stderr.readline()
        print(output.strip())
        if "GDB server started on port" in output:
            break
    print("Server Opened")
   


    # Start GDB as a subprocess
    gdb_process = subprocess.Popen(
        ['gdb', '-ex', f'file {elf_file}','-ex', 'set pagination off', '-ex', f'target remote localhost:{port[mcu_name]}' ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print("Server Started")

    try:
        while(1):
            output = gdb_process.stdout.readline()
            print(output.strip())
            if "Remote debugging using " in output:
                break
        print("Begin the commands")

        command = f'set {variable_name}={value}\n'
        gdb_process.stdin.write(command)
        gdb_process.stdin.flush()
        
        print("Parameter was set")

        command = f'p {variable_name}\n'
        gdb_process.stdin.write(command)
        gdb_process.stdin.flush()

        print("Parameter changed")

        command = 'continue &\n'
        gdb_process.stdin.write(command)
        gdb_process.stdin.flush()

        time.sleep(1)
        
        print("Quitting")
        command = 'q\n'
        gdb_process.stdin.write(command)
        gdb_process.stdin.flush()
        command = 'y\n'
        gdb_process.stdin.write(command)
        gdb_process.stdin.flush()

    except KeyboardInterrupt:
        print("\nTerminating")
    finally:
        gdb_process.terminate()
        gdb_server.kill()
        gdb_server.terminate()

# Aporriptetai logo tou oti ta etimata exipiretountai poly arga kai den einai swsto logo interrupt
def get_parameters(mcu_name, elf_file, variable_name):
    gdb_server = subprocess.Popen(
        args=[
        "pyocd", "gdbserver",
        "-p", port[mcu_name],
        "--telnet-port", telnet_port[mcu_name],
        "-t", "STM32H723VGTx",  
        "-u", mcu_ids[mcu_name]
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    while(1):
        output = gdb_server.stderr.readline()
        print(output.strip())
        if "GDB server started on port" in output:
            break
    print("Server Opened")
   


    # Start GDB as a subprocess
    gdb_process = subprocess.Popen(
        ['gdb', '-ex', f'file {elf_file}','-ex', 'set pagination off', '-ex', f'target remote localhost:{port[mcu_name]}' ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print("Server Started")

    try:
        while(1):
            time.sleep(polling_interval)

            print("Interrupt\n")
            command = 'interrupt\n'
            gdb_process.stdin.write(command)
            gdb_process.stdin.flush()
            time.sleep(0.1) #Thelei xrono na apntisei

            print("Ask for Print")
            command = f'p {variable_name}\n'
            gdb_process.stdin.write(command)
            gdb_process.stdin.flush()
            
            time.sleep(polling_interval)
            command = 'continue &\n'
            gdb_process.stdin.write(command)
            gdb_process.stdin.flush()

            p=0
            while(1):
                output = gdb_process.stdout.readline()
                print(output)
                if "$" in output:
                    
                    print(1)
                    break
            
            print("\nContinue Succeed\n")

    except KeyboardInterrupt:
        print("\nTerminating")
    finally:
        gdb_process.terminate()
        gdb_server.kill()
        gdb_server.terminate()


if __name__ == "__main__":
    mcu_name = "General"
    elf_file = dict()
    elf_file["Control"] = "/home/mat/Documents/AristurtleProjects/ECU/Version_Control/Control/Control.elf"
    elf_file["General"] = "/home/mat/Documents/AristurtleProjects/ECU/Version_Control/General/General.elf"
    var = 'P.Start_Up_Hack'
    var = 'P.Start_Stop_Bypass'

    set_parameter(mcu_name=mcu_name, elf_file=elf_file[mcu_name], variable_name=var, value=1) #kapws na kleineis to port
    # get_parameters(mcu_name=mcu_name, elf_file=elf_file, variable_name=var )
