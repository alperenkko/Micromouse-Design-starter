# ⚡ Micromouse - Autonomous Maze Solving Robot

An autonomous Micromouse robot capable of navigating and solving a maze with high speed and efficiency with custom 3D-printed suction components.

![Micromouse CAD Preview](cad/micromice_lightning.png)
---

## 🎯 Motivation & Project Goal
I am an 11th-grade student at a Turkish high school with interests in robotics, embedded systems and PCB design. I created this project over the course of the past two months to expand my knowledge of control systems, algorithms, and my own custom hardware design capabilities. My goal is to design and fabricate a high-performance Micromouse robot that is capable of competing against the fastest Maze Solving Robots with the help of suction assistance, and optimized algorithms.
---

## 🚀 Features & Technical Overview
Autonomous Navigation: Implemented the Floodfill Algorithm for calculating the shortest maze path
Closed-Loop Control: PID control with quadrature encoders and 6-axis gyroscope for precise wall centering and 90-degree turns.
Custom Sensing: Integrated 5 custom IR sensor modules for distance calculation and wall tracking
Aerodynamic Suction: Custom 3D-printed impeller and mount (designed in Fusion 360) to create additional downforce and maximize cornering
Brain: STM32 Microcontroller for sensor data acquisition and motor control
---

## 🛠️ Hardware & PCB Design

The image below shows the layout of the custom PCB designed in KiCad:

[![View PCB on KiCanvas](https://hack.club/pcb-badge)](https://github.com/alperenkko/Micromouse-Design-starter/blob/main/pcb/micromouse_pcb.kicad_pcb)

If you are viewing this repo directly, please replace this text with a screenshot preview of your PCB layout/schematic!
---

## 📁 Repository Structure
`/cad` contains all STL files (chassis, impeller, and motor mounts)
`/pcb` contains the KiCad schematic and PCB board file.
`/firmware` contains the STM32 source-code for PID motor control, IR sensing and the Floodfill algorithm.
---

## 📊 Bill of Materials (BOM)

| Material | Description | Quantity | Est. Unit Price ($) |
| :--- | :--- | :---: | :---: |
| STM32 Controller | STM32 Microcontroller Board | 1 | $4.50 |
| Custom IR Array | Custom Infrared Sensors (TCRT5000 / Op-Amps) | 5 | $3.00 |
| N20 Motors | DC Gear Motors with Encoders | 2 | $8.00 |
| IMU / Gyroscope | MPU6050 / Gyro Sensor Module | 1 | $2.00 |
| Motor Driver | TB6612FNG Dual Motor Driver Module | 1 | $2.50 |
| 3D Printed Parts | Chassis, Impeller & Bracket (PLA/PETG) | 1 | $3.00 |
| Wheels & Tires | High-traction mini wheels | 2 | $3.00 |
| Battery | LiPo Battery Pack | 1 | $6.00 |
| Total | | | ~$32.00 |
