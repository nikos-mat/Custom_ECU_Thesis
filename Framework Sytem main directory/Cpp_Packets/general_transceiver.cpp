#include <iostream>
#include <fcntl.h>
#include <termios.h>
#include <unistd.h>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <signal.h>
#include <sys/ioctl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <mutex>

#define BAUDRATE B2000000

// Mechanism to kill the thread
bool ctrl_c_pressed = 0;
void sigint_handler(int signum){
    ctrl_c_pressed = 1;  
}

int main() {

    signal(SIGINT, sigint_handler);

    // Initialize the State File
    std::ofstream stateFile("states/general_state.txt", std::ios::out | std::ios::trunc);
    if (!stateFile) {
        std::cout << "Error opening file for writing!" << std::endl;
        return 1;
    }
    uint8_t state=1;
    stateFile << "Active";
    stateFile.close();

    /* Create the FIFO (named pipe) to communicate with the Logging&Streaming */
    int GtoDL_fd;
    const char * GtoDL = "/tmp/fifo_GtoDL";
    mkfifo(GtoDL, 0666);
    GtoDL_fd = open(GtoDL, O_WRONLY);
    std::cout << "fifo_GtoDL opened" << std::endl;

    //Open fifo for communication with the Supervisor
    int SVtoG_fd;
    const char * SVtoG_fifo = "/tmp/SVtoG_fifo";
    SVtoG_fd = open(SVtoG_fifo, O_RDONLY| O_NONBLOCK);
    std::cout << "SVtoG_fifo opened" << std::endl;
    
    // Open the serial port
    int serial_port = open("/dev/ttyAMA2", O_RDWR| O_NOCTTY | O_NDELAY);
    // Create new termios struct, we call it 'tty' for convention
    struct termios tty;
    
    // Read in existing settings, and handle any error
    if(tcgetattr(serial_port, &tty) != 0) {
        printf("Error %i from tcgetattr: %s\n", errno, strerror(errno));
        return 1;
    }

    tty.c_cflag &= ~O_NONBLOCK; // Clear the O_NONBLOCK flag (enabling blocking mode)
    tty.c_cflag &= ~PARENB; // Clear parity bit, disabling parity (most common)
    tty.c_cflag &= ~CSTOPB; // Clear Gtop field, only one Gtop bit used in communication (most common)
    tty.c_cflag &= ~CSIZE; // Clear all bits that set the data size 
    tty.c_cflag |= CS8; // 8 bits per byte (most common)
    tty.c_cflag &= ~CRTSCTS; // Disable RTS/CTS hardware flow control (most common)
    tty.c_cflag |= CREAD | CLOCAL; // Turn on READ & ignore ctrl lines (CLOCAL = 1)
    tty.c_lflag &= ~ICANON;
    tty.c_lflag &= ~ECHO; // Disable echo
    tty.c_lflag &= ~ECHOE; // Disable erasure
    tty.c_lflag &= ~ECHONL; // Disable new-line echo
    tty.c_lflag &= ~ISIG; // Disable interpretation of INTR, QUIT and SUSP
    tty.c_iflag &= ~(IXON | IXOFF | IXANY); // Turn off s/w flow ctrl
    tty.c_iflag &= ~(IGNBRK|BRKINT|PARMRK|ISTRIP|INLCR|IGNCR|ICRNL); // Disable any special handling of received bytes
    tty.c_oflag &= ~OPOST; // Prevent special interpretation of output bytes (e.g. newline chars)
    tty.c_oflag &= ~ONLCR; // Prevent conversion of newline to carriage return/line feed
    tty.c_cc[VTIME] = 1;    // Wait for up to 1s (10 deciseconds), returning as soon as any data is received.
    tty.c_cc[VMIN] = 0;
    // Set in/out baud rate to be B2000000
    cfsetispeed(&tty, BAUDRATE);
    cfsetospeed(&tty, BAUDRATE);
    // Save tty settings, also checking for error
    if (tcsetattr(serial_port, TCSANOW, &tty) != 0) {
        printf("Error %i from tcsetattr: %s\n", errno, strerror(errno));
        return 1;
    }
    
    // Variables for the while loop
    uint32_t count_messages = 0;
    ssize_t bytes_read;
    int bytes_available;

    char id;
    bool datalogging;
    char byte;
    uint16_t length=0;
    char packet[500];

    packet[0]=254;
    

    char tun_packet[9]={'$','0','0','0','0','0','0','0','0'};

    // Starting the Reading While loop
    std::cout << "General Transceiver started" << std::endl;
    while(true) {
        // Try to read the Starter_Frame, if it fails, update State File 
        bytes_read = read(serial_port, &byte, 1);
        if (bytes_read <= 0 && !state==0){ 
            std::ofstream stateFile("states/general_state.txt", std::ios::out | std::ios::trunc);
            stateFile << "Inactive"; state=0;stateFile.close();}
        else{
            if (byte==254){
                
                // read and place id
                read(serial_port, &id, 1);
                std::memcpy(packet+1, &id, 1);
                
                // read and place data length of packet
                read(serial_port, &length, 2);
                std::memcpy(packet+2, &length, 2);

                // wait untill bytes are available,read and place data
                do{
                    ioctl(serial_port, FIONREAD, &bytes_available);
                }
                while (bytes_available<length); // Get the number of bytes available)
                bytes_read = read(serial_port, (packet+4), length);

                if (bytes_read != length) std::cout << "General: Failed to read the right length: "<< bytes_read << "!=" << int(length) << std::endl;
                else{
                    // read end byte, and write data
                    read(serial_port, &byte, 1);
                    if(byte==id){
                        
                        count_messages++;
                        std::memcpy(packet+length+4, &byte, 1);
                        write(GtoDL_fd, packet, length+5);
                        if(!state==1) {
                            std::ofstream stateFile("states/general_state.txt", std::ios::out | std::ios::trunc);
                            stateFile << "Active";
                            state=1;
                        }
                    }
                    else {
                        std::cerr << "Control: End byte: " << int(byte) << " Not equal to the id: " << int(id) << std::endl;
                        std::ofstream stateFile("states/general_state.txt", std::ios::out | std::ios::trunc);
                        stateFile << "Corrupted Packet" ;
                        state = 2;
                        stateFile.close();
                    }
                }
            }
        }


        // Check for commands from the Supervisor
        bytes_read = read(SVtoG_fd, &byte, 1);
        if (bytes_read>0){
            if(byte==36){
                bytes_read = read(SVtoG_fd, &tun_packet+1, 8);
                if(bytes_read==8 && tun_packet[2]==tun_packet[8] && tun_packet[1]==tun_packet[7]){
                    write(serial_port, tun_packet, 9);
                }
            }
        }

        if(ctrl_c_pressed == 1) {
            
            ioctl(serial_port, FIONREAD, &bytes_available); // Get the number of bytes available
            close(serial_port);
            close(GtoDL_fd);
            unlink(GtoDL);  
            
            close(SVtoG_fd);
            unlink(SVtoG_fifo);

            std::cout << "\tGeneral: Messages Received: " << count_messages<< "\tBuffer Leftovers: " << bytes_available << "\tUART Port and Fifos Closed" << std::endl;  
            return 0;
        }
         
    }
    
    return 0;


}