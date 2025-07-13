clear;
file = "VariablePackets.xlsx"; % Define the input Excel file

%% Datalogging

% Read the 'Datalogging' sheet from the Excel file into a table
datalogging_file = readtable(file,"ReadRowNames",false,"Sheet","Datalogging");

rows = height(datalogging_file); % Get the number of rows in the table
names = datalogging_file.Variable; % Extract variable names
names = string(strrep(names," ","_")); % Replace spaces with underscores
samplingHz = datalogging_file.Sampling_Hz; % Extract sampling frequencies
datatypes = string(datalogging_file.Data_Type); % Extract data types
numBytes = datalogging_file.Bytes; % Extract byte size per variable
mcu = datalogging_file.MCU; % Extract MCU type (Control/General)

% Initialize counters and length accumulators for different categories
Cindex100 = 0; Cindex1 = 0; Gindex100 = 0; Gindex1 = 0;
Clen100 = 0; Clen1 = 0; Glen100 = 0; Glen1=0;

if(rows>0)
    % Iterate through each variable entry
    for i = 1:rows
        Hz = samplingHz(i);
        
        % Categorize based on sampling frequency and MCU type and 
        % create the Bus Elements
        if (Hz==100 && mcu(i)=="Control")
            Cindex100 = Cindex100 + 1;
            Celems100(Cindex100) = Simulink.BusElement;
            Celems100(Cindex100).Name = matlab.lang.makeValidName(names(i));
            Celems100(Cindex100).DataType = 'uint8';
            Celems100(Cindex100).Dimensions = numBytes(i);
            Clen100 = Clen100 + numBytes(i);
        elseif (Hz==1 && mcu(i)=="Control")
            Cindex1 = Cindex1 + 1;
            Celems1(Cindex1) = Simulink.BusElement;
            Celems1(Cindex1).Name = names(i);
            Celems1(Cindex1).DataType = 'uint8';
            Celems1(Cindex1).Dimensions = numBytes(i);
            Clen1 = Clen1 + numBytes(i);
        elseif (Hz==100 && mcu(i)=="General")
            Gindex100 = Gindex100 + 1;
            Gelems100(Gindex100) = Simulink.BusElement;
            Gelems100(Gindex100).Name = names(i);
            Gelems100(Gindex100).DataType = 'uint8';
            Gelems100(Gindex100).Dimensions = numBytes(i);
            Glen100 = Glen100 + numBytes(i);
        elseif (Hz==1 && mcu(i)=="General")
            Gindex1 = Gindex1 + 1;
            Gelems1(Gindex1) = Simulink.BusElement;
            Gelems1(Gindex1).Name = names(i);
            Gelems1(Gindex1).DataType = 'uint8';
            Gelems1(Gindex1).Dimensions = numBytes(i);
            Glen1 = Glen1 + numBytes(i);
        end
    end
    
    % Write computed lengths to the 'Packets' sheet in the Excel file
    writematrix(Clen100, file, 'Sheet', 'Packets', 'Range', "D2");
    writematrix(Clen1, file, 'Sheet', 'Packets', 'Range', "D3");
    writematrix(Glen100, file, 'Sheet', 'Packets', 'Range', "D4");
    writematrix(Glen1, file, 'Sheet', 'Packets', 'Range', "D5");
    
    % Create Simulink Bus objects for each category
    ControlDatalogging100 = Simulink.Bus;
    ControlDatalogging100.Elements = Celems100;
    ControlDatalogging1 = Simulink.Bus;
    ControlDatalogging1.Elements = Celems1;
    GeneralDatalogging100 = Simulink.Bus;
    GeneralDatalogging100.Elements = Gelems100;
    GeneralDatalogging1 = Simulink.Bus;
    GeneralDatalogging1.Elements = Gelems1;
    
    % Save the bus structures as .mat files
    save("acu_general/BusDL100_General.mat","GeneralDatalogging100")
    save("acu_general/BusDL1_General.mat","GeneralDatalogging1")
    save("acu_control/BusDL100_Control.mat","ControlDatalogging100")
    save("acu_control/BusDL1_Control.mat","ControlDatalogging1")
    
    fprintf("Datalogging Busses Complete\n")
else
    fprintf("There are no variables for Datalogging\n")
end

%% Streaming

% Read the 'Streaming' sheet from the Excel file into a table
streaming_file = readtable(file,"ReadRowNames",false,"Sheet","Streaming");

rows = height(streaming_file); % Get the number of rows
names = streaming_file.Variable;
names = string(strrep(names," ","_"));
samplingHz = streaming_file.Sampling_Hz;
datatypes = string(streaming_file.Data_Type);
numBytes = streaming_file.Bytes;
mcu = streaming_file.MCU;

% Initialize counters and length accumulators for streaming
Cindex10 = 0;  Gindex10 = 0; 
Clen10 = 0;  Glen10 = 0; 

if(rows>0)
    % Iterate through each streaming variable entry
    for i = 1:rows
        Hz = samplingHz(i);
        % Categorize based on MCU type and create the Bus Elements
        if (Hz==10 && mcu(i)=="Control")
            Cindex10 = Cindex10 + 1;
            Celems10(Cindex10) = Simulink.BusElement;
            Celems10(Cindex10).Name = names(i);
            Celems10(Cindex10).DataType = 'uint8';
            Celems10(Cindex10).Dimensions = numBytes(i);
            Clen10 = Clen10 + numBytes(i);
        elseif (Hz==10 && mcu(i)=="General")
            Gindex10 = Gindex10 + 1;
            Gelems10(Gindex10) = Simulink.BusElement;
            Gelems10(Gindex10).Name = names(i);
            Gelems10(Gindex10).DataType = 'uint8';
            Gelems10(Gindex10).Dimensions = numBytes(i);
            Glen10 = Glen10 + numBytes(i);
        end
    end
    
    % Write computed lengths to the 'Packets' sheet in the Excel file
    writematrix(Clen10, file, 'Sheet', 'Packets', 'Range', "D6");
    writematrix(Glen10, file, 'Sheet', 'Packets', 'Range', "D7");
    
    % Create Simulink Bus objects for streaming data
    ControlStreaming10 = Simulink.Bus;
    ControlStreaming10.Elements = Celems10;
    GeneralStreaming10 = Simulink.Bus;
    GeneralStreaming10.Elements = Gelems10;
    
    % Save the streaming bus structures as .mat files
    save("acu_general/BusStr100_General.mat","GeneralStreaming10")
    save("acu_control/BusStr100_Control.mat","ControlStreaming10")
    
    fprintf("Streaming Busses Complete\n")
else
    fprintf("There are no variables for Streaming\n")
end