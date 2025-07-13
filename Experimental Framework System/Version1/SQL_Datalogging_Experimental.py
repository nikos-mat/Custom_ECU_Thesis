import sqlite3
import time


# Initialize the SQLite Database
conn = sqlite3.connect('SavedData\\your_database.db')
cursor = conn.cursor()

# Create a Table to store the data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS variables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        value REAL,
        timestamp INTEGER
    )
''')
conn.commit()
print("Database created!")
conn.close()


# Function to add values to a variable
def add_values_to_variable_and_export(variable_name, values):
    timestamp = int(time.time()) 
    
    # Insert each value into the database
    for value in values:
        cursor.execute("INSERT INTO variables (name, value, timestamp) VALUES (?, ?, ?)", (variable_name, value, timestamp))
        conn.commit()


# Logging 3 values to Variable1
conn = sqlite3.connect('SavedData\\your_database.db')
cursor = conn.cursor()

values_for_variable1 = [1 , 2, 3]
add_values_to_variable_and_export("Variable1", values_for_variable1)

conn.close()
print("Database updated!")

