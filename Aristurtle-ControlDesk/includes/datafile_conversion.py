import csv
import scipy.io
import struct
import string as str

def csv2mat(csv_file_path, Variables_in_packet):
        mat_file_path = csv_file_path[:-3]+"mat"
        rows = []
        with open(csv_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                rows.append(row)
        
        # CHECK IF IT NEEDS int(row[0])-1
        # for row in rows:
        #     row[0] = var_names[int(row[0])]

        # Structure the data for .mat 
        data_for_matlab = {}
        for row in rows:
            # parts = row.split(',')
            parts = [eval(i) for i in row]
            packet_id = parts[0]
            time = parts[1]
            data = parts[2:]

            if packet_id not in Variables_in_packet:
                continue
            scaling = Variables_in_packet[packet_id]['Scaling'].to_list()
            datatype = Variables_in_packet[packet_id]['Data_Type'].to_list()
            num_bytes = Variables_in_packet[packet_id]['Bytes'].to_list()
            names = Variables_in_packet[packet_id]['Variable'].to_list()

            idx1 =0
            idx2 = 0
            for i in range(len(num_bytes)):
                idx1=idx2
                idx2+= num_bytes[i]
                encoded = data[idx1:idx2]
                value= decode_bytes(encoded,datatype[i])/scaling[i]
                name = names[i].replace(" ", "_")
                if name not in data_for_matlab:
                    data_for_matlab[name] = {
                        "Name": name,
                        "Values": [],
                        "Timestamps": []
                    }
                  
                data_for_matlab[name]["Values"].append(float(value))
                data_for_matlab[name]["Timestamps"].append(int(time)/100)
        # Export data to .mat file
        matfile = {"Data":data_for_matlab, "Description": 1}
        return matfile
        # scipy.io.savemat(mat_file_path, matfile )

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
