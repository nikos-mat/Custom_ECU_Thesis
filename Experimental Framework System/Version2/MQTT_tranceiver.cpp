/*
 * MQTT Data Logger for Variable Monitoring
 * 
 * This program reads data from a named pipe (FIFO), processes the data,
 * and publishes it to an MQTT broker. It also supports reading an XLSX file
 * to determine the number of variables to monitor.
 * 
 * Libraries used:
 * - fcntl.h: File control options for opening the FIFO.
 * - unistd.h: System calls for file handling and sleep functions.
 * - iostream: Standard C++ input/output.
 * - fstream: File handling.
 * - string: String operations.
 * - vector: Dynamic array handling.
 * - thread: Multithreading support.
 * - signal.h: Handling system signals (e.g., Ctrl+C to exit).
 * - cstring: String manipulation functions.
 * - MQTTClient.h: MQTT client for communication.
 * - chrono: Time-based operations (for publish intervals).
 * - regex: Regular expressions (used for parsing XML in XLSX files).
 * - zip.h: Reading compressed ZIP archives (for extracting XLSX contents).
 */

 #include <fcntl.h>
 #include <stdio.h>
 #include <unistd.h>
 #include <iostream>
 #include <fstream>
 #include <string>
 #include <vector>
 #include <thread>
 #include <signal.h>
 #include <cstring>
 #include <MQTTClient.h>
 #include <chrono>
 #include <regex>
 #include <zip.h>
 
 // MQTT Broker Configuration
 #define ADDRESS     "tcp://192.168.137.70:1883"
 #define PUBCLIENTID "mqtt_transceiver_pub"
 #define SUBCLIENTID "mqtt_transceiver_sub"
 #define PUBTOPIC    "test/topic"
 #define SUBTOPIC    "test/topic"
 #define QOS         1
 #define TIMEOUT     10000L
 #define USERNAME    "AristurtleECU"
 #define PASSWORD    "aristurtle!@#"
 #define PUBLISH_INTERVAL_MS 100 // Publish every 0.1 seconds
 
 // XLSX File Paths for Variable Monitoring
 #define LOGGED_VARS_XLSX "includes/Logged Variables simple.xlsx"
 #define MONITOR_VARS_XLSX "includes/Monitor Variables simple.xlsx"
 
 bool ctrl_c_pressed = false; // Flag for graceful shutdown
 
 // Signal handler for Ctrl+C (SIGINT)
 void sigint_handler(int signum) {
     ctrl_c_pressed = true;
 }
 
 // Packs an array of float values into a single string, separated by semicolons
 std::string packMessage(float* buffer, int num_of_rows) {
     std::string output;
     for (int i = 0; i < num_of_rows; i++) {
         output += std::to_string(buffer[i]);
         if (i != num_of_rows - 1) {
             output += ";"; // Separate values with a semicolon
         }
     }
     return output;
 }
 
 // MQTT Publishing Thread
 void publishThread(float* variables_buffer, int num_of_rows) {
     MQTTClient client;
     MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
 
     conn_opts.keepAliveInterval = 20;
     conn_opts.cleansession = 1;
     conn_opts.username = USERNAME;
     conn_opts.password = PASSWORD;
 
     MQTTClient_create(&client, ADDRESS, PUBCLIENTID, MQTTCLIENT_PERSISTENCE_NONE, NULL);
 
     if (MQTTClient_connect(client, &conn_opts) != MQTTCLIENT_SUCCESS) {
         std::cerr << "PUB Failed to connect" << std::endl;
         return;
     }
     
     std::string payload;
 
     while (!ctrl_c_pressed) {
         payload = packMessage(variables_buffer, num_of_rows);
         MQTTClient_message pubmsg = MQTTClient_message_initializer;
         pubmsg.payload = (void*)payload.c_str();
         pubmsg.payloadlen = payload.length();
         MQTTClient_publishMessage(client, PUBTOPIC, &pubmsg, NULL);
         std::this_thread::sleep_for(std::chrono::milliseconds(PUBLISH_INTERVAL_MS));
     }
 
     MQTTClient_disconnect(client, 10000);
     MQTTClient_destroy(&client);
 }
 
 // Function to count rows in an XLSX file
 int countRowsInXLSX(const std::string& filename) {
     zip* archive = zip_open(filename.c_str(), 0, NULL);
     if (!archive) {
         std::cerr << "Failed to open " << filename << std::endl;
         return -1;
     }
     
     struct zip_stat zipStat;
     zip_stat_init(&zipStat);
     zip_stat(archive, "xl/worksheets/sheet1.xml", 0, &zipStat);
     zip_file* sheetFile = zip_fopen(archive, "xl/worksheets/sheet1.xml", 0);
     if (!sheetFile) {
         std::cerr << "Failed to open sheet1.xml in " << filename << std::endl;
         zip_close(archive);
         return -1;
     }
     
     std::string sheetData;
     sheetData.resize(zipStat.size);
     zip_fread(sheetFile, &sheetData[0], zipStat.size);
     zip_fclose(sheetFile);
     zip_close(archive);
     
     std::regex rowRegex("<row[^>]*>");
     return std::distance(std::sregex_iterator(sheetData.begin(), sheetData.end(), rowRegex),
                          std::sregex_iterator());
 }
 
 int main() {
     signal(SIGINT, sigint_handler);
 
     int num_logged_vars = countRowsInXLSX(LOGGED_VARS_XLSX) - 1; // Subtract title row
     int num_of_vars = 500; // Set total monitored variables
     
     float* variables_buffer = new float[num_of_vars]();
     
     // Open FIFO for reading sensor data
     int StoMQTT_fd;
     const char* toMQTT_fifo = "/tmp/fifo_StoMQTT";
     StoMQTT_fd = open(toMQTT_fifo, O_RDONLY);
     if (StoMQTT_fd < 0) {
         std::cerr << "Failed to open FIFO." << std::endl;
         return -1;
     }
 
     // Start MQTT publishing in a separate thread
     std::thread pubThread(publishThread, variables_buffer, num_of_vars);
     pubThread.detach();
 
     uint32_t count_messages = 0;
     char byte;
     ssize_t bytes_read;
     uint8_t extra_id_bits;
     uint16_t id;
     float value;
     bool datalogging;
 
     // Main loop to read from FIFO and update variables
     while (true) {
         bytes_read = read(StoMQTT_fd, &byte, 1);
         if (bytes_read < 0) std::cerr << "Error reading FIFO" << std::endl;
         
         if ((byte >> 4) == 11) { // Check message type
             count_messages++;
             datalogging = ((byte - 176) >> 2);
             extra_id_bits = byte - 176;
             if (datalogging) extra_id_bits -= 4;
             
             read(StoMQTT_fd, &byte, 1);
             id = byte + (extra_id_bits << 8) + 1;
             read(StoMQTT_fd, &value, 4);
             
             if (datalogging) id += num_of_vars;
             variables_buffer[id - 1] = value;
         }
 
         if (ctrl_c_pressed) {
             std::cout << "\nMQTT: FIFO Messages Received: " << count_messages << std::endl;
             close(StoMQTT_fd);
             unlink(toMQTT_fifo);
             delete[] variables_buffer;
             return 0;
         }
     }
     return 0;
 }
 