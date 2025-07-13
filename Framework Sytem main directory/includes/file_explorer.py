import os
import datetime
import sys

def get_creation_date(file_path):
    """
    Get the creation date of a file.
    """
    creation_time = os.path.getctime(file_path)
    return datetime.datetime.fromtimestamp(creation_time)

def get_storage_size(file_path):
    """
    Get the storage size of a file.
    """
    return os.path.getsize(file_path)

def list_files(folder_path):
    output = ""
    # folder_path = sys.argv[1]
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            creation_date = get_creation_date(file_path)
            storage_size = get_storage_size(file_path)/1000
            # Format the date to a shorter form
            formatted_creation_date = creation_date.strftime("%Y-%m-%d %H:%M:%S")
            output += f"{formatted_creation_date},{storage_size},{file_name};"

    return output

# output = ""
# folder_path = sys.argv[1]
# for file_name in os.listdir(folder_path):
#     file_path = os.path.join(folder_path, file_name)
#     if os.path.isfile(file_path):
#         creation_date = get_creation_date(file_path)
#         storage_size = get_storage_size(file_path)/1000
#         # Format the date to a shorter form
#         formatted_creation_date = creation_date.strftime("%Y-%m-%d %H:%M:%S")
#         output += f"{formatted_creation_date},{storage_size},{file_name};"
# print(output)