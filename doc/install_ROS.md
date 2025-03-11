Here is the markdown code for your documentation, formatted and ready for you to copy or save:

```markdown
# Prerequisites

## 1.1. Recommended Operating System

**Ubuntu 24.04 LTS**:
- Standard maintenance until April 2029.
- Legacy support until 2036.

## 1.2. Recommended Hardware

**NVIDIA Graphics Card**:
- Ensure the NVIDIA driver is installed.
- To verify the driver version, use the following command:

```bash
nvidia-smi
```

Example output:

```
Wed Sep 16 13:53:41 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.100      Driver Version: 440.100      CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce MX150       Off  | 00000000:02:00.0 Off |                  N/A |
| N/A   54C    P0    N/A /  N/A |    316MiB /  2002MiB |      5%      Default |
+-------------------------------+----------------------+----------------------+
                                                                              
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1024      G   /usr/lib/xorg/Xorg                            29MiB |
|    0      1786      G   /usr/lib/xorg/Xorg                           126MiB |
|    0      2019      G   /usr/bin/gnome-shell                         101MiB |
|    0      4581      G   ...AAAAAAAAAAAACAAAAAAAAAA= --shared-files    19MiB |
|    0     78591      G   /opt/zoom/zoom                                24MiB |
|    0     84198      G   /usr/lib/firefox/firefox                       1MiB |
+-----------------------------------------------------------------------------+
```

## 1.3. Basic Dependencies

- Python >= 3.11
- PyTorch
- Git
- OpenSSH
- OpenCV
- YOLO
- VSCode
- Conda
- Jupyter

## 1.4. Installation of ROS 2

### 1.4.1 ROS 2 Distributions and Ubuntu Compatibility

| Distro              | Release Date    | EOL Date       |
|---------------------|-----------------|----------------|
| Iron Irwini         | May 23rd, 2023 | November 2024  |
| Humble Hawksbill    | May 23rd, 2022 | May 2027       |
| Galactic Geochelone | May 23rd, 2021 | December 9th, 2022 |
| Foxy Fitzroy        | June 5th, 2020 | June 20th, 2023 |
| Eloquent Elusor     | November 22nd, 2019 | November 2020 |
| Dashing Diademata   | May 31st, 2019 | May 2021       |
| Crystal Clemmys     | December 14th, 2018 | December 2019 |
| Bouncy Bolson       | July 2nd, 2018 | July 2019      |
| Ardent Apalone      | December 8th, 2017 | December 2018 |
| Beta Releases       | Various        | Various        |

**Recommendation:** Install the latest LTS/stable version of dependencies and upgrade every three years. As of **January 12th, 2025**, it is recommended to use **Ubuntu 24.04** and **ROS 2 Jazzy Jalisco**, both of which have EOL in mid-2029.

### 1.4.2 System Setup

#### Set Locale

Ensure you have a locale that supports UTF-8. Use the following commands:

```bash
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```

#### Enable Required Repositories

Add the ROS 2 apt repository to your system:

1. Enable the Ubuntu Universe repository:

   ```bash
   sudo apt install software-properties-common
   sudo add-apt-repository universe
   ```

2. Add the ROS 2 GPG key:

   ```bash
   sudo apt update && sudo apt install curl -y
   sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
   ```

3. Add the repository to your sources list:

   ```bash
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
   ```

#### Install Development Tools (Optional)

For building ROS packages or development, install:

```bash
sudo apt update && sudo apt install ros-dev-tools
```

#### Install ROS 2

Update your apt repository caches and upgrade the system:

```bash
sudo apt update
sudo apt upgrade
```

##### Desktop Install (Recommended):

Includes ROS, RViz, demos, and tutorials:

```bash
sudo apt install ros-jazzy-desktop
```

##### ROS-Base Install (Bare Bones):

Includes communication libraries, message packages, and command-line tools. No GUI tools:

```bash
sudo apt install ros-jazzy-ros-base
```

#### Install Additional RMW Implementations (Optional)

Replace or add middleware (RMW) at runtime as needed. See the guide for managing multiple RMWs.

#### Setup Environment

Set up your environment by sourcing the following file:

```bash
# Replace ".bash" with your shell (e.g., setup.bash, setup.sh, setup.zsh)
source /opt/ros/jazzy/setup.bash
```

echo $ROS_DISTRO



#### Try Some Examples

1. Open one terminal, source the setup file, and run a C++ talker:

   ```bash
   source /opt/ros/jazzy/setup.bash
   ros2 run demo_nodes_cpp talker
   ```

2. Open another terminal, source the setup file, and run a Python listener:

   ```bash
   source /opt/ros/jazzy/setup.bash
   ros2 run demo_nodes_py listener
   ```

You should see the talker publishing messages and the listener responding with received messages. This verifies both the C++ and Python APIs are functioning correctly.
You can open gazebo simulation by: 

gz sim


pip3 install lark-parser
pip install catkin_pkg
pip install empy  
pip3 install scikit-build
pip3 install opencv-python

remember to turn off conda before running, said they are not get on well, but so far not problem. May have wrong path projection problems.
This package making requirement is outdated, remember to edit the <depend>gazebo_ros<depend> to <depend>ros_gz_sim<depend>
and clear the log files with:



mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/comprobo24/neato_packages.git
cd ~/ros2_ws
colcon build --symlink-install
source ~/ros2_ws/install/setup.bash


Edit your ~/.bashrc file so that your workspace is correctly loaded whenever you start a new terminal (note: if you are using a different shell, you may have to adjust this).

echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc