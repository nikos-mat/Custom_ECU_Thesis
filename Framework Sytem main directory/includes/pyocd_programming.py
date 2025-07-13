from pyocd.core.helpers import ConnectHelper
from pyocd.flash.file_programmer import FileProgrammer
import time
import logging
import os

# binfile1 = "blinkStSimu.bin"
# binfile2 = "StSpi.bin"
# mc_id="003D004F3432511430343838"

mcu_ids = { "General": "002C00193133510237363734", "Control": "003F00333133511939363430" }

def load_code(microcontroller_name, binary_file_name):
    microcontroller_id = mcu_ids[microcontroller_name]
    try:
        logging.basicConfig(level=logging.INFO)
        # with ConnectHelper.session_with_chosen_probe(unique_id=microcontroller_id) as session:
        with ConnectHelper.session_with_chosen_probe() as session:
            board = session.board
            target = board.target

            flash = target.memory_map.get_boot_memory()

            # Load firmware into device.
            FileProgrammer(session).program(file_format="hex", file_or_path=binary_file_name)
            # Reset
            target.reset_and_halt()
            
            # Read some registers.
            # print("pc: 0x%X" % target.read_core_register("pc"))

            target.step()
            # print("pc: 0x%X" % target.read_core_register("pc"))

            target.resume()
            time.sleep(0.2)
            target.halt()
            # print("pc: 0x%X" % target.read_core_register("pc"))

            target.reset_and_halt()
            # print("pc: 0x%X" % target.read_core_register("pc"))
            return 1
    except:
        return 0
        
def stop_mcu(microcontroller_id):
    try:
        logging.basicConfig(level=logging.INFO)
        with ConnectHelper.session_with_chosen_probe(unique_id=microcontroller_id) as session:
            board = session.board
            target = board.target
            # Reset
            target.reset_and_halt()
            return 1
    except:
        return 0

def reset_mcu(microcontroller_id):
    try:
        logging.basicConfig(level=logging.INFO)
        with ConnectHelper.session_with_chosen_probe(unique_id=microcontroller_id) as session:
            board = session.board
            target = board.target
            # Reset
            target.reset_and_halt()
            target.resume()
            return 1
    except:
        return 0

if __name__ == "__main__":
    elf_file = dict()
    elf_file["Control"] = "/home/mat/Documents/AristurtleProjects/ECU/Version_Control/Control/Control.elf"
    elf_file["General"] = "/home/mat/Documents/AristurtleProjects/ECU/Version_Control/General/General.elf"

    mcu_name = "Control"
    # mcu_name = "General"


    command = "pyocd flash -t STM32H723VGTx --format elf -u {} {}".format( mcu_ids[mcu_name], elf_file[mcu_name])
    # command = "pyocd flash -t STM32H723VGTx --format elf  {}".format(elf_file[mcu_name])
    # command = "pyocd reset -t STM32H723VGTx -u {}".format(mcu_ids[mcu_name])
    os.system(command)
