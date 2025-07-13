#include <fcntl.h>      // For file control operations (open, read, write)
#include <stdio.h>      // For input/output functions (printf, etc.)
#include <sys/stat.h>   // For file system operations (e.g., file types)
#include <unistd.h>     // For POSIX API (close, read, write, etc.)
#include <chrono>       // For time-related operations (system_clock, duration, etc.)
#include <iostream>     // For standard I/O operations (cin, cout)
#include <fstream>      // For file stream operations (ifstream, ofstream)
#include <string>       // For string manipulation and conversions
#include <ctime>        // For time functions (time_t, tm)
#include <iomanip>      // For stream manipulators (e.g., setting precision)
#include <vector>       // For using vector containers
#include <thread>       // For threading support (std::thread)
#include <signal.h>     // For handling signals (SIGINT)
#include <cstring>      // For C string manipulation functions
#include <algorithm>    // For algorithms (e.g., std::copy)

#define BUFFER_SIZE 3000           // Size of the buffer (number of values to store)
#define SAVING_PATH "Datafiles_CSV/" // Path to save the CSV files

bool ctrl_c_pressed = 0;          // Flag to detect if Ctrl+C is pressed
std::ofstream outputFile;         // Output file stream for writing CSV data
uint32_t num_of_saves = 0;        // Counter to track the number of saves made

// Signal handler for Ctrl+C (SIGINT) to gracefully exit
void sigint_handler(int signum) {
    ctrl_c_pressed = 1;  
}

// Function to save contents of the buffer to a CSV file
void saveToCSV(float* buffer, std::string filename_relative_path) {
    // Open file in append mode
    std::ofstream outputFile(filename_relative_path, std::ios::app | std::ios::out);
    if (!outputFile) {
        std::cerr << "Error: Unable to open file for writing: " << filename_relative_path << std::endl;
        return;
    }

    // Write contents of the buffer to the CSV file
    int index;
    for (int i = 0; i < BUFFER_SIZE; i++) {
        index = i * 3;    
        outputFile << buffer[index] << "," << buffer[index + 1] << "," << buffer[index + 2] << "\n";
    }

    outputFile.close();  // Close file after writing
    num_of_saves++;      // Increment save counter
}

int main() {
    // Set up signal handler for Ctrl+C
    signal(SIGINT, sigint_handler);

    // Get the current date and time for naming the CSV file
    std::time_t now = std::time(nullptr);  // Get current system time
    std::tm* tm = std::localtime(&now);    // Convert to local time
    std::string today = std::to_string(tm->tm_mday) + std::to_string(tm->tm_mon + 1) + std::to_string(tm->tm_year + 1900);  // Format date (day-month-year)
    std::string current_time = std::to_string(tm->tm_hour) + std::to_string(tm->tm_min) + std::to_string(tm->tm_sec);  // Format time (hour-minute-second)
    
    // Generate file name with the format "data_ddmmyyyy_hhmmss.csv"
    std::string name = "data_" + today + "_" + current_time + ".csv";
    std::string databaseRelPath = SAVING_PATH + name;  // Full path to the file
    
    // Open the output file to initialize it
    outputFile.open(databaseRelPath, std::ios::app | std::ios::out);
    outputFile.close();
    
    // Open the FIFO for reading data
    int StoDL_fd;
    const char* toDL_fifo = "/tmp/fifo_StoDL";  // Path to FIFO for inter-process communication
    StoDL_fd = open(toDL_fifo, O_RDONLY);  // Open FIFO in read-only mode

    // Variables for UART communication
    uint32_t count_messages = 0;  // Counter for the number of messages received
    char byte;                    // Buffer to store a single byte read from FIFO
    ssize_t bytes_read;           // Number of bytes read
    uint8_t extra_id_bits;        // Extra bits for ID extraction
    uint16_t id;                  // ID of the received message
    float value;                  // Value of the received message

    // Get the starting time for calculating relative timestamps
    auto start_time = std::chrono::system_clock::now();
    double start_seconds = std::chrono::duration_cast<std::chrono::duration<double>>(start_time.time_since_epoch()).count();
    int time;  // Variable to store the calculated relative time
    
    // Buffers for storing received variables before saving to CSV
    float variableBuffer[BUFFER_SIZE * 3];    // Buffer to store the data (ID, value, time)
    float variableBuffer_copy[BUFFER_SIZE * 3]; // Copy of the buffer for saving
    uint16_t buffer_index = 0;  // Index to track the buffer position

    // Main loop to read from FIFO and process data
    while (true) {
        bytes_read = read(StoDL_fd, &byte, 1);  // Read a byte from FIFO
        if (bytes_read < 0) std::cerr << "Error reading\n";
        
        if (byte >> 4 == 11) {  // Check if the byte corresponds to the expected message type
            count_messages++;  // Increment message counter

            extra_id_bits = (byte - 176 - 4);  // Extract extra ID bits
            bytes_read = read(StoDL_fd, &byte, 1);  // Read next byte for ID
            if (bytes_read < 0) std::cerr << "Error reading\n";
            id = byte + (extra_id_bits << 8) + 1;  // Combine bytes to form the full ID

            bytes_read = read(StoDL_fd, &value, 4);  // Read the 4-byte value
            if (bytes_read < 0) std::cerr << "Error reading\n";

            // Calculate the relative time
            std::chrono::system_clock::time_point curr_time = std::chrono::system_clock::now();
            std::chrono::duration<double> curr_seconds_duration = std::chrono::duration_cast<std::chrono::duration<double>>(curr_time.time_since_epoch());
            double curr_seconds = curr_seconds_duration.count();
            time = static_cast<int>(curr_seconds * 1000 - start_seconds * 1000);  // Time in milliseconds

            // Store the data in the buffer
            variableBuffer[buffer_index++] = id;
            variableBuffer[buffer_index++] = value;
            variableBuffer[buffer_index++] = time;

            // If the buffer is full, save data to CSV and reset buffer
            if (buffer_index == 3 * BUFFER_SIZE) {
                // Copy buffer to a new array to prevent overwrite during saving
                std::copy(std::begin(variableBuffer), std::end(variableBuffer), std::begin(variableBuffer_copy));
                buffer_index = 0;  // Reset buffer index
                // Create a new thread to save data asynchronously
                std::thread saveThread(saveToCSV, variableBuffer_copy, databaseRelPath);
                saveThread.detach();  // Detach thread to run independently
            }
        }

        // Check if Ctrl+C was pressed to gracefully terminate the program
        if (ctrl_c_pressed == 1) {
            std::cout << "\n----------------------\nDatalogging:" << std::endl;
            std::cout << "\tFIFO Messages Received: " << count_messages << std::endl;
            std::cout << "\tNumber of saves: " << num_of_saves << std::endl;
            close(StoDL_fd);  // Close the FIFO file descriptor
            unlink(toDL_fifo);  // Remove the FIFO file
            std::cout << "\tFIFO Port Closed" << std::endl;  
            return 0;
        }
    }

    return 0;
}
