This repository contains some of the codes and scripts that I implemented for a Custom Electronic Control Unit. This ECU is my Thesis for my Master's degree and is meant to control a Formula Student Race Car.

The thesis proposes a complete process of studying, designing, and building such a Unit, specifically tailored to the needs of the team’s race car. The ECU architecture was based on modern high-performance microcontrollers 
and was designed to fully replace the team’s previous control unit. The hardware was implemented by my coleague Kaplanis Vasilios.

My job was to adapt the team’s existing codebase to the new architecture and integrate the framework system responsible for the ECU’s non-critical, yet important functions. Features were developed for telemetry, 
datalogging, and remote access and control, enhancing the diagnostic capability and real-time monitoring of the vehicle.

The ECU PCB has three processors on it. Two STM32H7 for the main code that has to do with the vehicle and a Raspberry Pi, responsible for the supportive system. In 
