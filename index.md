# Welcome to the Robotics Section

This is a hobby project focused on learning robotics systems through both hardware and software platforms.

## Topics Covered
- [Neato and ROS2](#Neato-with-ROS2-Jazzy)
- [Roomba with PyRobot](#Roomba-Platform)
- [Vision](mechanical-design.md)

# 1. Neato with ROS2 Jazzy
The Neato section of this project is adapted from my undergraduate course, **ENGR3370 Computational Robotics**.


### 1.1. Processor
The computing module is a **Raspberry Pi 5 (8GB RAM)** running **Ubuntu 24.04**. With good support of ROS2 Jazzy
### 1.2. Sensor

### 1.3. Actuator
- **CSI interface camera connected to Rpi:** official camera module.
- **LiDAR (Laser Distance Sensor):** 360° scanning for navigation and mapping.
- **Infrared Sensors:** Detect obstacles and adjust movement.
- **Bumper Sensors:** Detect physical collisions and redirect.
- **Drop Sensors:** Prevents falls by detecting height changes.
- **Wheel Encoders:** Track movement and measure distance.
- **Battery & Charging Sensors:** Monitor battery and locate the dock.
- **USB camera module:** Planning on connect high resolution use camera and dual camera
- **ICM20948:** Planning on add a accelerometer connect to Rpi gpio.


### 1.4. Software
the software for neato project is strictly limited to the ROS2 platform, as a learning progress. Currently code and progress listed below: 
├── gscam
│   ├── examples
│   ├── include
│   ├── scripts
│   └── src
├── image_processing
├── kalman_filters
├── my_pf
│   ├── cfg
│   ├── launch
│   └── scripts
├── neato_2dnav
│   ├── launch
│   ├── maps
│   ├── params
│   └── rviz
├── neato_basic_1
│   ├── drive_square_sample_1
│   ├── drive_square_sample_2
│   ├── drive_square_sample_3
│   ├── marker_sample
│   └── wall_approach_starter
├── neato_basic_2
│   ├── back_forth
│   ├── emergency_stop
│   ├── messages
│   ├── relative_motion
│   └── wall_approach
├── neato_description
│   ├── launch
│   ├── meshes
│   ├── rviz
│   ├── sdf
│   └── urdf
├── neato_driver
│   └── src
├── neato_gazebo
│   ├── launch
│   ├── model
│   ├── scripts
│   └── worlds
├── neato_node
│   ├── include
│   ├── launch
│   ├── msg
│   ├── nodes
│   └── src
├── neato_robot
├── neato_soccer
│   └── scripts
├── path_planning
├── probability_basics
│   └── figures
├── simple_filter
│   ├── cfg
│   ├── msg
│   └── scripts
└── teleop_twist_keyboard




# 2.Roomba Platform
The Roomba section of this project uses the **iRobot Roomba 865** as the chassis platform.

### 2.1. Processor
#### 2.1.1. **Raspberry Pi Zero W**
The Raspberry Pi Zero W is an older yet cost-effective and power-efficient model. However, its official OS support is limited to **Raspbian Lite (Bookworm-based)**, which lacks official ROS2 support. Wile compiling ROS2 for raspian, some modules failed to load correctly. While inspired me to explore possibility exploring software robotic platform based on python, taking advantages of extensive interfaces and excellent support for computer vision and machine learning libraries. Some existed platform could be used, such as: [**PyRobot**](https://github.com/AtsushiSakai/PythonRobotics), and [**PySLAM**](https://github.com/luigifreda/pyslam). By using Python, communication between the Roomba and the processing unit is established via **serial communication** through the pre-built **7-pin Mini-DIN port** on the Roomba. Additionally, video streaming and remote control are enabled over **WLAN** and **Raspberry Pi**.

**Update:** The **7-Pin Mini-DIN port** connects directly to Roomba’s **14V battery**, which was inadvertently wired to the power input on a USB converter. Unfortunately, unlike larger Raspberry Pi models, the **Pi Zero W lacks a voltage regulator**, leading to the board burning out.

#### 2.1.2. **Raspberry Pi Zero 2W**
To mitigate the power issue, I upgraded to a **Raspberry Pi Zero 2W**, which offers low power consumption and includes a **CSI-2 camera connector**. Additionally, I purchased an **official iRobot communication cable** (7-Pin Mini-DIN to USB) that includes an **integrated voltage regulation chip**, ensuring safe operation.

#### 2.1.3. **Raspberry Pi 2** *(Backup Plan)*
As a backup, I considered using a **Raspberry Pi 2** for controlling the Roomba via **ROS2**. The latest officially supported OS for the Pi 2 is **Ubuntu 22.04 LTS**, which corresponds to **ROS2 Humble**. However, since the Pi 2 lacks a built-in wireless module, I purchased a **USB network card** from China with an **AIC8800 controller chip**. To use this card on Linux, an additional driver installation is required.

### 2.2. Sensor
- **Infrared Sensors:** Detects obstacles and helps avoid collisions.
- **Bumper Sensors:** Detects physical contact with objects.
- **Cliff Sensors:** Prevents falls by detecting ledges and stairs.
- **Dirt Detect Sensors:** Identifies high-dirt areas for focused cleaning.
- **Wheel Encoders:** Tracks movement and distance traveled.
- **Battery & Charging Sensors:** Monitors battery life and dock location.

### 2.3. Actuator

### 2.4. Software


# Compter vision study
## Stereo vision
### Kinect
### Dual camera
## Semantic segmantation
