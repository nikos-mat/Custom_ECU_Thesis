#include <iostream>     // For standard input and output operations
#include <fcntl.h>       // For file control options like open(), O_WRONLY, etc.
#include <termios.h>     // For configuring serial communication settings
#include <unistd.h>      // For POSIX API like read(), write(), close()
#include <cstring>       // For memory operations like memcpy()
#include <cstdlib>       // For general utilities like exit()
#include <fstream>       // For file operations
#include <signal.h>      // For handling signals like SIGINT (Ctrl+C)
#include <sys/ioctl.h>   // For input/output control operations like checking buffer size
#include <sys/stat.h>    // For file status operations
#include <sys/types.h>   // For type definitions like ssize_t
#include <mutex>         // For thread safety (not used in this code but included)

// Define the baud rate for serial communication
#define BAUDRATE B2000000

// Global flag to detect Ctrl+C signal
bool ctrl_c_pressed = 0;

// Signal handler function for SIGINT (Ctrl+C)
void sigint_handler(int signum) {
    ctrl_c_pressed = 1;  // Set the flag to terminate the loop safely
}

int main() {
    // Register the SIGINT signal handler
    signal(SIGINT, sigint_handler);

    int StoDL_fd;  // File descriptor for FIFO "StoDL"
    int StoMQTT_fd; // File descriptor for FIFO "StoMQTT"
    const char *StoDL = "/tmp/fifo_StoDL"; // Named pipe for data logging
    const char *StoMQTT = "/tmp/fifo_StoMQTT"; // Named pipe for MQTT communication

    // Create the named pipes (FIFOs) with read/write permissions
    mkfifo(StoDL, 0666);
    mkfifo(StoMQTT, 0666);

    // Open the FIFOs for writing
    StoDL_fd = open(StoDL, O_WRONLY);
    std::cout << "fifo_DL opened" << std::endl;
    StoMQTT_fd = open(StoMQTT, O_WRONLY);
    std::cout << "fifo_MQTT opened" << std::endl;

    // Open the serial port for reading and writing
    int serial_port = open("/dev/ttyAMA2", O_RDWR);
    if (serial_port < 0) {
        std::cerr << "Error opening serial port" << std::endl;
        return 1;
    }

    // Configure the serial port settings
    struct termios tty;
    if (tcgetattr(serial_port, &tty) != 0) {
        std::cerr << "Error getting terminal attributes: " << strerror(errno) << std::endl;
        return 1;
    }

    // Set up serial port settings
    tty.c_cflag &= ~PARENB; // No parity bit
    tty.c_cflag &= ~CSTOPB; // Use one stop bit
    tty.c_cflag &= ~CSIZE; // Clear character size bits
    tty.c_cflag |= CS8; // Use 8-bit characters
    tty.c_cflag &= ~CRTSCTS; // Disable hardware flow control
    tty.c_cflag |= CREAD | CLOCAL; // Enable reading and ignore modem control lines

    tty.c_lflag &= ~(ICANON | ECHO | ECHOE | ECHONL | ISIG); // Disable line processing and echoing
    tty.c_iflag &= ~(IXON | IXOFF | IXANY | ICRNL | IGNBRK | BRKINT | PARMRK | ISTRIP | INLCR | IGNCR);
    tty.c_oflag &= ~(OPOST | ONLCR); // Raw output mode
    
    tty.c_cc[VTIME] = 10;  // Timeout in deciseconds (1 second max wait)
    tty.c_cc[VMIN] = 0;     // Non-blocking read mode

    // Set baud rate
    cfsetispeed(&tty, BAUDRATE);
    cfsetospeed(&tty, BAUDRATE);

    // Apply settings to the serial port
    if (tcsetattr(serial_port, TCSANOW, &tty) != 0) {
        std::cerr << "Error setting terminal attributes: " << strerror(errno) << std::endl;
        return 1;
    }

    uint32_t count_messages = 0; // Counter for received messages
    ssize_t bytes_read;
    int bytes_available;
    char byte; // Single byte buffer for reading
    bool datalogging;
    char packet[6]; // Buffer for storing a received packet
    std::cout << "Transceiver started" << std::endl;

    // Main loop for reading from the serial port
    while (true) {
        bytes_read = read(serial_port, &byte, 1);
        if (bytes_read < 0) std::cerr << "Error reading from serial port" << std::endl;
        
        // Check if the received byte indicates a valid message
        if ((byte >> 4) == 11) { // Checking the upper 4 bits
            count_messages++; // Increment message counter
            datalogging = ((byte - 176) >> 2); // Extract datalogging flag
            std::memcpy(packet, &byte, 1); // Copy first byte to packet
            
            // Read remaining 5 bytes of the packet
            bytes_read = read(serial_port, packet + 1, 5);
            if (bytes_read < 0) std::cerr << "Error reading from serial port" << std::endl;

            // Write to FIFO based on datalogging flag
            if (datalogging) {
                write(StoDL_fd, packet, 6); // Write to data logging FIFO
            }
            
            write(StoMQTT_fd, packet, 6); // Write to MQTT FIFO
        }

        // Handle Ctrl+C termination
        if (ctrl_c_pressed) {
            ioctl(serial_port, FIONREAD, &bytes_available); // Check buffer for remaining bytes
            
            std::cout << "\n----------------------\nSafety Shutdown:" << std::endl;
            std::cout << "\tMessages Received: " << count_messages << std::endl;
            std::cout << "\tBuffer Leftovers: " << bytes_available << std::endl;
            
            close(serial_port); // Close UART port
            std::cout << "\tUART Port Closed" << std::endl;
            
            close(StoDL_fd); // Close and remove FIFO files
            unlink(StoDL);
            close(StoMQTT_fd);
            unlink(StoMQTT);
            std::cout << "\tStoDL, StoMQTT FIFOs Closed" << std::endl;
            return 0;
        }
    }
    return 0;
}
