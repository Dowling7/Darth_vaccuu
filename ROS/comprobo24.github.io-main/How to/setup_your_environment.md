---
title: "Setup Your Computing Environment"
toc_sticky: true
---

The teaching team will be using ROS2 Humble with Ubuntu 22.04, and we recommend you do the same.

> While there are other ways to install ROS on a computer (ROS2 for Windows, ROS2 through Docker, ROS2 through Windows Subsystem for Linux, ROS1), you really, really want to use Ubuntu running via dual boot (not as a virtual machine).  We have found that while these other setups work to varying degrees, there are always little issues that will crop up that will likely get in the way of your learning.  While setting up a dual boot takes some time, you will find that the payoff is quite big (both in terms of the smoothness of your experience and in learning how to interact with a Linux environment).

> Additionally, while the latest Ubuntu is 24.04 and latest stable version of ROS2 as of this offering of CompRobo is Jazzy, the latter's release was fewer than 4 months before the start of the F24 semester. This means that there are significantly fewer debugging resources available for this distro; this is particularly problematic because Jazzy is coupled with a significant API change for several key tools we use in this class (like Gazebo). As Humble will be supported through 2027, we strongly recommend using Humble for the easiest interaction with existing tools, ample online community resources, and a more time-tested distro. Humble is paired with 22.04 Ubuntu, making this the reasonable choice for linux distro for the time being.


## Setting up a Dual Boot

How2Shout has [a nice walkthrough of setting up your computer to dual boot](https://linux.how2shout.com/install-ubuntu-22-04-jammy-alongside-windows-10-dual-boot/). Note that this is a tutorial for installing 22.04 alongside Windows 10; however all the steps _will_ work for our recommended 22.04 and Windows 11 install. Note that the Olin IT group has also assembled a set of excellent [dual-boot instructions](https://wikis.olin.edu/linux/doku.php) (access to this page requires being on the network or connected via VPN).

Before starting a dual boot process, you'll want to have an Ubuntu 22.04 installer handy.  You can get an installer using the [How2Shout guide on creating a bootable installer](https://linux.how2shout.com/how-to-create-ubuntu-22-04-bootable-usb-drive-on-windows), following the [instructions set up by the Olin IT](https://wikis.olin.edu/linux/doku.php), or by using one of the thumb drives we have created for you to use. Look for them on the Neato rack in the classroom. 

A few quick notes:
* **INSTALL OPTIONS**: When installing Ubuntu, you _should_ select the options to **Download updates** and **Install third-party software**.
* **UPGRADING an Existing Ubuntu Distro**: If you have an older version of Ubuntu, you may be able to upgrade it.  That said, I have seen cases where this upgrade process has yielded a broken installation.  Here are some [instructions on upgrading](https://ubuntu.com/server/docs/upgrade-introduction) from the Ubuntu website.
* **PARTITIONING**: When installing Ubuntu you will likely need to **shrink your Windows partition** to make room for Ubuntu.  Sometimes this can be accomplished through the Ubuntu installer, if you are not able to shrink your partition in this way, we had success using [EaseUS Partition Manager](https://www.easeus.com/partition-manager/epm-free.html). Tutorials online also suggest using Ubuntu in "Try" mode and using the `gparted` manager to modify partitions. Or you can even manage your partitions through Windows before attempting an install. If you are having a problem setting up your partitions, please send us an e-mail.
* **SPACE ALLOCATION**: You should probably reserve about 64 GB of space for Ubuntu (if you are planning on using Ubuntu moving forward from this class, consider reserving 128 GB or more).


*Once you have a freshly installed copy of Ubuntu 22.04, perform the next steps on this page.*

### Troubleshooting

In previous years, a student reported an error message about needing to turn off RST to install Ubuntu.  The student was able to find a workaround.  If you have this or any other issue, please send an e-mail to someone on the teaching team.

Sometimes a "black screen of death" can occur when installing Ubuntu on top of a previously used partition (for instance, if you're upgrading an existing partition). If this happens, boot to a "safe mode" through Grub ("Advanced Options for Ubuntu" and selecting the safe-mode image). It is then recommended that you enable networking, then run the dpkg utility. If this doesn't resolve the black screen of death, please send an e-mail to someone on the teaching team.



## Make Sure Your NVIDIA Card is Setup

Depending on how you installed Ubuntu (for instance, if you did not opt for third-party software to be installed), you may not have the drivers for your NVIDIA graphics card.  To check whether you have the NVIDIA drivers installed, you can run the following command in a ```terminal``` window.

{% include codeHeader.html %}
```bash
nvidia-smi
```

If you have the drivers installed, you should see output similar to the following.
```bash
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

If you see a message that ``nvidia-smi`` is not installed, you can use [these instructions](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-22-04) to install it. 

> Note: NVIDIA drivers on Ubuntu are notoriously finicky. If you are having trouble getting them to work, please contact the teaching team. Also note that it is _totally fine_ for the purposes of all default class activities to not have access to a GPU (although it might be nice for some of your projects). There will be some time to figure this out if it doesn't go smoothly for you the first time.

## Setup Git
Coming into this class, you likely have already used some form of git version control, and have created a GitHub account. For a seamless experience using git and GitHub for this class, we recommend taking a moment to ensure you have added your GitHub credentials to your system and setting up SSH keys. 
* Setting up your GitHub account on Ubuntu: [this tutorial from the GitHub docs](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git) will walk you through the main steps
* Setting up SSH keys: [this tutorial from the GitHub docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) will walk you through generating a new SSH key for your Ubuntu machine and adding it to your GitHub account.


## Install ROS Humble

Follow [this tutorial](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html) (make sure to install ``ros-humble-desktop`` rather than ``ros-humble-ros-base``).  **Once you get to the section ``Next Steps'', you can come back to this document (don't follow those instructions in the tutorial).**

In addition to the ``ros-humble-desktop`` package, you should install these additional packages to allow you to stream video from the Neatos and interact with the Neato simulator.

{% include codeHeader.html %}
```bash
sudo apt-get update && sudo apt-get install -y ros-humble-gazebo-ros-pkgs \
	ros-humble-nav2-bringup \
	ros-humble-navigation2 \
	ros-humble-camera-info-manager \
	ros-humble-cartographer-ros \
	ros-humble-cartographer \
	ros-humble-gscam \
	git \
	python3-colcon-common-extensions \
	gstreamer1.0-plugins-good \
	gstreamer1.0-plugins-bad \
	gstreamer1.0-plugins-ugly \
	gstreamer1.0-libav gstreamer1.0-tools \
	gstreamer1.0-x \
	gstreamer1.0-alsa \
	gstreamer1.0-gl \
	gstreamer1.0-gtk3 \
	gstreamer1.0-qt5 \
	gstreamer1.0-pulseaudio \
	python3-pip \
	hping3
```

## Setup your Workspace with the Neato Packages

Next, you'll be creating a workspace, downloading the packages required to connect to the Neato, and building those packages.  You'll be learning more about what's going on in these steps later in the course, but if you are curious see [this ROS tutorial](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html).  

> Note: if you are trying to run this in a VM with an Apple Silicon Mac, you can try (again, not supported officially) the steps below but replace the line where you checkout the ``neato_packages`` with ``git clone -b no_gazebo https://github.com/comprobo24/neato_packages``.

{% include codeHeader.html %}
```bash
source /opt/ros/humble/setup.bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone git@github.com:comprobo24/neato_packages.git
cd ~/ros2_ws
colcon build --symlink-install
source ~/ros2_ws/install/setup.bash
```

You will probably get a warning when you execute this build that looks like this.
```bash
--- stderr: neato_node2                   
/usr/lib/python3/dist-packages/setuptools/command/easy_install.py:158: EasyInstallDeprecationWarning: easy_install command is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
---
```

This warning is benign and is [known to the ROS2 developers](https://github.com/ros2/ros2/issues/1362).

Edit your ``~/.bashrc`` file so that your workspace is correctly loaded whenever you start a new terminal (note: if you are using a different shell, you may have to adjust this).

{% include codeHeader.html %}
```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
```

### Set your ROS_DOMAIN_ID

ROS2 uses the environment variable ``ROS_DOMAIN_ID`` as a way to isolate various ROS2 environments.  Each student will have their own ROS_DOMAIN_ID assigned to them so that there is no cross talk between computers.  [Check on Canvas for your domain ID](https://olin.instructure.com/courses/592/pages/ros2-domain-ids) and add it to your ``.bashrc`` file using the following command.

{% include codeHeader.html %}
```bash
echo "export ROS_DOMAIN_ID=put-your-domain-id-here" >> ~/.bashrc
```

### Installing OpenCV and Streaming Support

Make sure you have installed ``pip3`` (this can be done through ``apt-get`` as shown earlier).

Install ``Sckit-Build`` and ``OpenCV``.

{% include codeHeader.html %}
```bash
pip3 install scikit-build
pip3 install opencv-python
```
> With Python 3.12+ you may encounter an "external packages" error when performing this step. In this instance, we suggest adding the ``--break-build-systems`` flag in order to force a system-wide install of these packages. However, in your future work, we recommend learning more about virtual environments (``venv``, ``anaconda`` and more!) which is increasingly the workflow suggested for Python projects.

Make sure ``hping3`` is setup so you can stream video from the robot.

{% include codeHeader.html %}
```bash
sudo setcap cap_net_raw+ep /usr/sbin/hping3
```

## Working with VSCode (Optional)

We'll be using VSCode when doing demonstrations in class.  If you'd like to use VSCode, you can use the [VSCode Ubuntu install instructions](https://code.visualstudio.com/docs/setup/linux) and then go through the steps in [Configure VS Code for ROS2](https://www.youtube.com/watch?v=hf76VY0a5Fk).

There is documentation on running [ROS code in the debugger under VSCode](https://github.com/ms-iot/vscode-ros/blob/master/doc/debug-support.md), but you might have better luck using the default Python debugging profile.
