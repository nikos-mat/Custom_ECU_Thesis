#!/bin/bash

# Compile and build C++ codes
g++ 'Logging&Streaming.cpp' -o 'Logging&Streaming' -l paho-mqtt3c -lzip -pthread
g++ general_transceiver.cpp -o general_transceiver
g++ control_transceiver.cpp -o control_transceiver


# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful."
else
    echo "Compilation failed."
fi