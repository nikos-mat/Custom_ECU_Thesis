#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <chrono>
#include <iostream>
#include <fstream>
#include <string>
#include <ctime>
#include <iomanip>
#include <thread>
#include <signal.h>
#include <cstring>
#include <algorithm>
#include <MQTTClient.h>
#include <regex>
#include <zip.h>
#include <climits>
#include <mutex>
#include <unordered_map>

//Logging
#define BUFFER_SIZE 15000
#define SAVING_PATH "../Datafiles_CSV/"
// Streaming
#define PUBTOPIC        "toARCODE/variables"
#define PUBCLIENTID    "mqtt_transceiver_pub"
#define SUBCLIENTID    "mqtt_transceiver_sub"
#define QOS         1
#define TIMEOUT     10000L
#define USERNAME    "AristurtleECU"
#define PASSWORD    "aristurtle!@#"
#define PUBLISH_INTERVAL_MS 100 // Publish every 0.1 seconds

// Global variables
bool ctrl_c_pressed = 0;
const char* ADDRESS;
std::ofstream outputFile;
uint32_t num_of_saves = 0;

// Mutex for the shared variables between the threads
std::mutex map_mutex;
std::unordered_map<int, std::string> streaming_packets;

// Function that helps to kill the packet
void sigint_handler(int signum);

// Function to save contents of the buffer to a CSV file
void saveToCSV(std::string buffer, std::string filename_relative_path);

// Thread that published data in mqtt
void publishThread();

// Function that reads the current ip 
const char* get_tcp_address_from_file(const char* filename); 

int main()
{

    //  -------- VARIABLES START --------  //

    // Set the current ip
    ADDRESS = get_tcp_address_from_file("states/current_ip.txt");

    // Open the fifo to read the variables
    int GtoDL_fd;
    int CtoDL_fd;
    const char * GtoDL_fifo = "/tmp/fifo_GtoDL";
    const char * CtoDL_fifo = "/tmp/fifo_CtoDL";
    
    
    //Variables to change between the pipes
    bool CGflag = 0;
    int fd;

    // variables for the uart read
    uint32_t count_messages = 0;
    char byte;
    ssize_t bytes_read;
    char id;
    bool datalogging;
    uint16_t length=0;
    char data_bytes[600]; 

    // buffers to save variables to csv file
    std::string packet;
    std::string Logging_Buffer;
    std::string Logging_Buffer_Copy;
    int i;

    //  -------- VARIABLES END --------  //


    // Initialize and Create the csv file
    std::time_t now = std::time(nullptr);
    std::tm* tm = std::localtime(&now);
    std::string today = std::to_string(tm->tm_mday) + std::to_string(tm->tm_mon + 1) + std::to_string(tm->tm_year + 1900);
    std::string current_time = std::to_string(tm->tm_hour) + std::to_string(tm->tm_min) + std::to_string(tm->tm_sec); // Get current time
    std::string name = "data_" + today + "_" + current_time + ".csv";
    std::string databaseRelPath = SAVING_PATH + name;
    outputFile.open(databaseRelPath, std::ios::app | std::ios::out);
    outputFile.close();
    
    // get the starting time to work with relative time
    auto start_time = std::chrono::system_clock::now();
    double start_seconds = std::chrono::duration_cast<std::chrono::duration<double>>(start_time.time_since_epoch()).count();
    uint32_t time;

    // Handle the sigint signal
    signal(SIGINT, sigint_handler);

    // Open the FIFOs
    GtoDL_fd = open(GtoDL_fifo, O_RDONLY| O_NONBLOCK);
    CtoDL_fd = open(CtoDL_fifo, O_RDONLY| O_NONBLOCK);

    // Start the Data Streaming
    std::thread pubThread(publishThread);
    pubThread.detach();

    // Initialize the State File
    std::ofstream stateFile("states/logging_state.txt", std::ios::out | std::ios::trunc);
    stateFile << 0;
    stateFile.close();

    while(true){
        //Switching between pipes
        fd = CGflag ? GtoDL_fd : CtoDL_fd;
        CGflag = CGflag ? 0 : 1;

        // Start Byte
        read(fd, &byte, 1);
        if (byte==254){
            
            // ID
            read(fd, &id, 1);
            if(id<220)  datalogging=1;
            else        datalogging=0;

            // Data Length of packet
            read(fd, &length, 2);

            // Data Bytes
            bytes_read = read(fd, data_bytes, length);
            if (bytes_read != length) std::cout << "Data L&S: Failed to read the right length: "<< bytes_read << "!=" << int(length) << std::endl;

            else{
                // Read End Byte, and Write Data
                read(fd, &byte, 1);
                if(byte==id){
                    
                    count_messages++;
                    // std::cout << count_messages << std::endl;

                    //Save the receiving time
                    std::chrono::system_clock::time_point curr_time = std::chrono::system_clock::now();
                    std::chrono::duration<double> curr_seconds_duration = std::chrono::duration_cast<std::chrono::duration<double>>(curr_time.time_since_epoch());
                    double curr_seconds = curr_seconds_duration.count();
                    time = (uint32_t)(curr_seconds*1000 -start_seconds*1000);

                    packet.clear();
                    packet += std::to_string(id); packet += ','; packet += std::to_string(time);
                    for (i=0;i<length;i++){
                        packet += ',';
                        packet += std::to_string(data_bytes[i]);     
                    }         
                }
                else std::cerr << "Data Logger/ Streamer: End byte: " << int(byte) << " Not equal to the id: " << int(id) << std::endl;
            

                // Use the lock mutex before changing the shared streaming_packets with the Streaming Publisher
                std::unique_lock<std::mutex> lock(map_mutex);
                streaming_packets[id] = packet;

                // If the packet is for Data Logging
                if (datalogging){
                    // Append to the Logging buffer
                    Logging_Buffer += packet; Logging_Buffer += '\n';

                    // Copy to another buffer that Saving Thread uses and Save
                    if(Logging_Buffer.length() >= BUFFER_SIZE){
                        Logging_Buffer_Copy = Logging_Buffer;
                        Logging_Buffer.clear();
                        std::thread saveThread(saveToCSV, Logging_Buffer_Copy, databaseRelPath);
                        saveThread.detach();
                        //CHECK IF IT WORKS
                        std::ofstream stateFile("states/logging_state.txt", std::ios::out | std::ios::trunc);
                        stateFile << time;
                        stateFile.close();
                    }
                }
            }
        }

        if(ctrl_c_pressed == 1) {
            close(GtoDL_fd);
            unlink(GtoDL_fifo); 
            std::cout << "\tData Logging&Streaming: FIFO Messages Received: " << count_messages << "\tNumber of saves: " << num_of_saves  << "\tFIFO Port Closed" << std::endl;
            return 0;
        }

    }

    return 0;
}

void publishThread() {
    // Initialize MQTT
    MQTTClient client;
    MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
    conn_opts.keepAliveInterval = 20;
    conn_opts.cleansession = 1;
    conn_opts.username = USERNAME;
    conn_opts.password = PASSWORD;
    MQTTClient_create(&client, ADDRESS, PUBCLIENTID, MQTTCLIENT_PERSISTENCE_NONE, NULL);
    if (MQTTClient_connect(client, &conn_opts) != MQTTCLIENT_SUCCESS) {
        std::cerr << "MQTT Packet PUB Failed to connect" << std::endl;
        return;
    }
    std::string payload;

    while (!ctrl_c_pressed) {
        // Publish a message 
        payload.clear();
        for (const auto& pair : streaming_packets) {
            payload += pair.second.c_str();
            payload += '\n';
        }

        // Set and transmit the packets
        MQTTClient_message pubmsg = MQTTClient_message_initializer;
        pubmsg.payload = (void *)payload.c_str();
        pubmsg.payloadlen = payload.length();
        MQTTClient_publishMessage(client, PUBTOPIC, &pubmsg, NULL);

        
        // Sleep for the specified interval
        std::this_thread::sleep_for(std::chrono::milliseconds(PUBLISH_INTERVAL_MS));
    
    }

    // Terminate the MQTT
    MQTTClient_disconnect(client, 10000);
    MQTTClient_destroy(&client);
}

// Function to save contents of the buffer to a CSV file
void saveToCSV(std::string buffer, std::string filename_relative_path) {
    
    std::ofstream outputFile(filename_relative_path, std::ios::app | std::ios::out);
    if (!outputFile) {
        std::cerr << "Error: Unable to open file for writing: " << filename_relative_path << std::endl;
        return;
    }
    outputFile << buffer;

    outputFile.close();
    num_of_saves++;
}

void sigint_handler(int signum){
    ctrl_c_pressed = 1;  
}

const char* get_tcp_address_from_file(const char* filename) {
    static char address[64];

    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Cannot open file: " << filename << std::endl;
        return nullptr;
    }

    std::string ip;
    std::getline(file, ip);
    file.close();

    if (ip.empty()) {
        std::cerr << "IP is empty in file: " << filename << std::endl;
        return nullptr;
    }

    strcpy(address, "tcp://");
    strcat(address, ip.c_str());
    strcat(address, ":1883");

    return address;
}