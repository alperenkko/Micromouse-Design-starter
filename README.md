# Micromouse - Autonomous Maze Solving Robot

An autonomous Micromouse robot that is  capable of navigating and solving a maze with high speed and efficiency with custom 3D-printed suction components.

![Micromouse CAD Preview](cad/micromice_lightning.png)
---

## Features
The Complex algorithms, the PID tuning and 6 Fully-Custom IR sensors. It compares the value between two sensors to center itself in the middle of the maze cell. theres 2 side (90°) and 2 front (0°) sensors that it can use(2 corner sensors too). Also, it uses a complex algorithm that even has floodfill implemented inside to find the closest/most efficient exit possible. When tuned right with the PID and the signal values such as sensor values and PWM for the motors, this robot can slide in mazes like a wet soap in your hand, but with one exception; theres no crashes that make you sad!
---

## Technical Overview
Brain: STM32 Blackpill Microcontroller for sensor data acquisition and motor control,
Motors: N20 12mm 2000rpm encoder motors.
Wheels: 21x14mm jsumo silicone wheels for maximum grab and control over the corner-turns.
motor drivers: TB66FNG motor driver
Impeller fan: 720 coreless motor and 30-mm wide 9-wing impeller for ~50gr of suction power
6 Fully-Custom IR sensors: They work in analog voltage so you can sense even one centimeter if you make it good enough!💯
---

## Hardware & PCB Design

The image below shows the layout of the custom PCB designed in KiCad:
(it was so hard to do those since it was my first time lol)
---
[![View PCB on KiCanvas](https://hack.club/pcb-badge)](https://github.com/alperenkko/Micromouse-Design-starter/blob/main/pcb/micromouse_pcb.kicad_pcb)

![PCB 3d view](pcb/pcb_3dside.png)
![PCB Layout](pcb/pcb_schematic.png)

## Repository Structure
`/cad` contains all STL files (chassis, impeller, and motor mounts)
`/pcb` contains the KiCad schematic and PCB board file such as png and .kicad files.
`/firmware` contains the STM32 source-code for PID motor control, IR sensing and the Floodfill algorithm(read down there)
---

## Bill of Materials (BOM)
- [BOM.csv](bom/BOM.csv) - The main BOM file 
- [BOM_ozdisan.csv](bom/BOM_ozdisan.csv) - The BOM file for the custom IR sensor 
- [BOM_ozdisan.pdf](bom/BOM_ozdisan.pdf) - The PDF version / datasheet for the custom IR sensor (The pdf version of the IR sensor file.(downloaded from the website, its raw and half turkish.)


## /firmware folder
the code uses the STM32 library on ArduınoIDE to code the blackpill board using arduino IDE. heres the link of the library so you can download it too:
https://github.com/stm32duino/BoardManagerFiles/raw/main/package_stmicroelectronics_index.json
also, dont forget that thisa was just  a test code and NOT  the actual code since this is still in the design.
---

thanks for reading, i think thats all i can do, i would be really happy if you approve it- also nothing here is AI Generated, i used AI just fore research and did everything myself i think. :) see you!!
