# Turning the Roomba 900 Series into a Remote-Controlled Robot with ROS – Remote Operation Edition

## Overview
In the previous article of this series, we introduced how to connect a Roomba 900 series with an Ubuntu PC using a USB cable and control it via ROS in a wired setup.

In this article, we will demonstrate how to make the Roomba 900 series a WiFi-enabled ROS-controlled remote operation robot by connecting it to a battery-powered Raspberry Pi via USB and also attaching a USB camera to the Raspberry Pi.

---

## Execution Environment

### Previous Configuration
In the previous setup, the Roomba was controlled via a USB connection to an Ubuntu PC. The configuration was as follows:

- **Roomba 961** (Previously connected to a PC, now connected to Raspberry Pi)
- **Micro USB cable** (Now used to connect the Raspberry Pi to the Roomba)
- **PC:** Dell Inspiron 13 5390
- **OS:** Ubuntu 24.04 + ROS Jazzy (ROS2)
- **Controller:**
  - Xbox360-compatible gamepad (8bitDo SN30 Pro – USB wired)
  - 3D mouse (3DConnexion SpaceMouse Wireless, used wired)
- **Code used:** [GitHub Repository](https://github.com/y-yosuke/create_robot/tree/humble-add-setmode)

### Additional Configuration
For this remote operation setup, we add the following hardware:

- **Raspberry Pi 4B**
  - Recommended microSD card: 100MB/s or faster read speed
- **OS:** Ubuntu 24.04 + ROS Jazzy (ROS2)
- **USB power bank:** Anker Power Bank (10000mAh, 30W)
- **USB Camera:** Buffalo WEB Camera BSW505MBK
- **Code used:** [GitHub Repository](https://github.com/y-yosuke/create_robot/tree/humble-add-setmode)

Previous tests also confirmed functionality with Ubuntu 22.04 and ROS Humble.

---

## Installation & Build

### Installing Ubuntu 24.04.1 on Raspberry Pi
Write the Ubuntu 24.04 disk image to a microSD card following the official installation guide: [Install Ubuntu on a Raspberry Pi](https://ubuntu.com/download/raspberry-pi).

### Installing & Building Software on Raspberry Pi
Follow the previous article’s [installation and build instructions](https://opensource-robotics.tokyo.jp/?p=8244#install-build). If `gnome-text-editor` does not launch, use `nano` or `gedit`.

#### Enabling SSH on Raspberry Pi
Ubuntu 24.04.1 does not include an SSH server by default. Install and enable it with:
```bash
$ sudo apt update
$ sudo apt install openssh-server
```

#### Installing Missing Dependencies
Install the `v4l2_camera` package, which was missing from dependency descriptions:
```bash
$ sudo apt install ros-jazzy-v4l2-camera
```

---

## Remote Operation of the Roomba

### Hardware Setup
Connect the Raspberry Pi to the Roomba, USB camera, and power bank. On the Ubuntu PC side, connect a game controller.

```
[Raspberry Pi 4B + USB Camera + Power Bank] <==(USB cable)==> [Roomba 900 Series]
   ↑       /// ( WiFi Network ) ///        ↓
[Ubuntu PC + Game Controller]
```

### Connecting to Raspberry Pi via SSH
From the Ubuntu PC, connect to the Raspberry Pi using SSH:
```bash
$ ssh robotuser@robotuser-rp4b.local
robotuser@robotuser-rp4b:~$ sudo chmod 777 /dev/ttyACM0
```
Keep this SSH session open.

### Running the Software
On the Raspberry Pi SSH terminal, start `create_1_camera.launch`:
```bash
robotuser@robotuser-rp4b:~$ source ~/roomba_ws/install/setup.bash
robotuser@robotuser-rp4b:~$ ros2 launch create_bringup create_1_camera.launch
```

#### Displaying Camera Feed
On the Ubuntu PC, open a new terminal and run:
```bash
$ source ~/roomba_ws/install/setup.bash
$ ros2 run rqt_image_view rqt_image_view
```
Select `image_raw` to view the camera feed.

#### Controlling Roomba
**Using an Xbox360-compatible gamepad:**
```bash
$ source ~/roomba_ws/install/setup.bash
$ ros2 launch create_bringup joy_teleop.launch
```
Press the **L1 button** while using the **right analog stick** to control movement.

**Using a 3DConnexion SpaceMouse:**
```bash
$ source ~/roomba_ws/install/setup.bash
$ ros2 launch create_bringup spacenav_teleop.launch
```

### Video Demonstration
This video shows the Roomba moving independently, controlled remotely via a gamepad, while streaming its camera feed:

[![YouTube Video](https://opensource-robotics.tokyo.jp/wordpress/wp-content/uploads/2024/10/maxresdefault_wifi-roomba.jpg)](https://www.youtube.com/embed/rRmRd7Aj0Rc?si=-95btUC_Q5prhfQh)

To stop the Roomba, press **Ctrl+C** in each running terminal.

---

## Appendix A: Roomba in Passive Mode
Even while cleaning, the Roomba’s state can be obtained via Roomba Open Interface (ROI) in passive mode.

To enable passive mode:
```bash
robotuser@robotuser-rp4b:~$ ros2 launch create_bringup create_1_camera.launch control_mode:=passive
```

Pressing the **CLEAN button** on the Roomba or starting cleaning via the **iRobot app** will activate cleaning mode while maintaining ROS topic output.

---

## Appendix B: Troubleshooting

### Terminal Fails to Launch
If the terminal fails to start in Ubuntu 24.04, check the `LANG` setting in `/etc/default/locale`:
```
LANG="en_US.UTF-8"
```

### `gnome-text-editor` Fails to Launch
Use an alternative editor like `nano` or `gedit`:
```bash
$ nano ~/roomba_ws/src/libcreate/include/create/packet.h
```
or
```bash
$ sudo apt update
$ sudo apt install gedit
$ gedit ~/roomba_ws/src/libcreate/include/create/packet.h
```

---

This concludes this article. For previous and next articles in this series:

- **Previous:** [Roomba 900 Series as a ROS Remote-Controlled Robot – USB Wired Edition](https://opensource-robotics.tokyo.jp/?p=8244)
- **Next:** [Using SwitchBot with ROS – Adding Data Acquisition Devices](https://opensource-robotics.tokyo.jp/?p=8500)

