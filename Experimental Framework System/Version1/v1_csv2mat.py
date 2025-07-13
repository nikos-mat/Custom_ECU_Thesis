import csv
import scipy.io
import pandas as pd

# INPUTS
csv_file_path = "data_3042024_13127.csv"
csv_catalog = "Logged Variables simple.xlsx"

# Mat file's name
mat_file_path = csv_file_path[0:-3] + "mat"

# Open the excel file and get the variable names from the first column
df = pd.read_excel(csv_catalog)
var_names = df.iloc[:, 0].tolist()

# Read the excel row by row and save them in a list
rows = []
with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rows.append(row)
for row in rows:
    row[0] = var_names[int(row[0])]

# Structure the data for .mat 
data_for_matlab = {}
for row in rows:
    variable_name, value, timestamp = row
    if variable_name not in data_for_matlab:
        data_for_matlab[variable_name] = {
            "Name": variable_name,
            "Values": [],
            "Timestamps": []
        }
    data_for_matlab[variable_name]["Values"].append(float(value))
    data_for_matlab[variable_name]["Timestamps"].append(int(timestamp)/1000)

# Export data to .mat file
matfile = {"Data":data_for_matlab, "Description": 1}
scipy.io.savemat(mat_file_path, matfile )

print("Data exported to " + mat_file_path)