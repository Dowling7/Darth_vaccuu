---
title: "Using the Neatos"
toc_sticky: true
---

This document will help use the physical Neato as well as its simulated counterpart.  Before going through these instructions, make sure that you have already <a href="../How to/setup_your_environment">setup your computing environment</a>.


# Connecting to the Physical Neatos

This semester marks another year of physical Neatos to CompRobo! These robots were used in 2018, then made a triumphant return in 2023. A [TurtleBot4 Lite](https://www.robotshop.com/en/clearpath-robotics-turtlebot-4-lite-mobile-robot.html) may also be occasionally available for this class as well.


## Normal Usage

### Step 1: Find a Neato!

The Neatos will be stored in or just outside the classroom (MAC113).  This semester we are using the [Botvac series](https://neatorobotics.cn/wp-content/themes/neato-2015/assets/images/robot-vacuums/botvac-d75/botvac-d75_medium.jpg) Neatos.

Checklist:

1. Make sure the Neato's batteries are charged.  To test this, pull the Neato away from it's charging station and hit the big button next to the Neato's display.  The display should turn on and stay on revealing a battery capacity indicator (if the robot complains about the dirtbin being out, just press on the little button where the dirtbin would normally be).  Make sure the battery capacity is close to full.


### Step 2: Get a Battery USB Battery Pack for the Raspberry Pi

The batteries are all stored on the racks in the classroom.

Checklist:
1. The battery indicator light should be at least level 2 (preferably full)


### Step 3: Connect the USB battery pack to the Raspberry Pi's USB cable.

It should take about 1 minute for the robot to be ready to use (see step 4 for a final checklist).

<p align="center">
<img alt="a picture of a neato in the on state" src="../website_graphics/neato_with_battery.jpg" width="40%"/>
</p>

Checklist:

1. If you are using one of the cables with a small flat connector, make sure it is inserted in the proper direction (yes, it is possible to put it in backwards)


### Step 4: Connecting to the Neato from Your Laptop

Checklist before performing this step:

1. Raspberry pi display backlight is illuminated and not flashing on and off (see troubleshooting section for what to do if this is not the case)
2. Raspberry pi display shows that the Neato is connected to the OLIN-ROBOTICS network and has an IP address asssigned to it
3. Raspberry pi display shows that the signal strength of the Neato's connection is at least 45 (the max is 99 for the wifi adapters with attached antennas and 70 for the ones without).   If the signal strength is very low see troubleshooting section for information on what to do.
4. Your laptop is connected to the OLIN-ROBOTICS (the password for the network is available from our Canvas homepage [here](https://canvas.olin.edu/courses/822)).  A good sanity check is to make sure you can ping the robot.  You can run ping from the Ubuntu terminal by typing ping IP_ADDRESS_OF_YOUR_ROBOT (if the connection is working you will see the time for each packet to round trip back to your computer).

In a new terminal, connect to the robot:

{% include codeHeader.html %}
```bash
ros2 launch neato_node2 bringup.py host:=IP_OF_ROBOT
```

Where IP_ADDRESS_OF_YOUR_ROBOT is the IP address displayed on the raspberry Pi.  To verify that everything is working properly, try the following steps.

### Moving the Neato around

Open the teleop keyboard node.  Instructions on sending various velocity commands are given then by the on-screen terminal output.  The maximum speed of the neato is $$0.3 \frac{m}{s}$$.

{% include codeHeader.html %}
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

### Viewing Images from the camera

> NOTE: not all Neatos will have a camera installed.

Startup ```rqt```.

{% include codeHeader.html %}
```bash
rqt
```

From the "plugins" menu, select the "visualization" submenu, and then choose "image view".  In the drop down list, select the image topic ``camera/image_raw``.

## Neato ROS Topics

This documentation gives the high-level purpose of each topic.  To explore more, you can use the following command to get more information.

```bash
$ ros2 topic info /topic-name
```

If you want to know more about a message you see in the output of ``ros2 topic info`` you can use the following command.

```bash
$ ros2 interface show msg_package_name/msg/MessageName
```

### ``accel``

This is the linear acceleration of the Neato in units of earth's gravities.
 
### ``bump``

This topic contains four binary outputs corresponding to each of the Neato's four bump sensors.  The individual fields are:

* ``left_front``
* ``left_side``
* ``right_front``
* ``right_side``

### ``cmd_vel``

You publish to this topic to set the robot's velocity.  The ``linear.x`` direction sets forward velocity and ``angular.z`` sets the angular velocity.

### ``odom``

This tells you the robot's position relative to its starting location as estimated by wheel encoders.  You can get this inforation more flexibly through the ROS ``tf2`` module, but this is a relatively easy way to get started.

### ``projected_stable_scan``

This provides the LIDAR measurements (think of these as detected obstsacles or objects from the environment).  In contrast to the ``scan`` topics, these measurements are in the odometry frame (rather than relative to the robot) and are in Cartesian rather than polar coordinates.  There is no need to use this topic, but for some applications it is nice to have.

### ``scan``

These are the measurements of the Neato's LIDAR.  This diagram should help you with the project. It shows the angles for the laser range data coming from the Neato and how it maps onto the Neato's physical layout.

<p align="center">
<img alt="A Diagram of the Neato's Lidar" src="../website_graphics/lidar.png"/>
</p>

The LaserScan message consists of a number of attributes:

```bash
$ ros2 interface show sensor_msgs/msg/LaserScan
# Single scan from a planar laser range-finder #
# If you have another ranging device with different behavior (e.g. a sonar
# array), please find or create a different message, since applications
# will make fairly laser-specific assumptions about this data

std_msgs/Header header # timestamp in the header is the acquisition time of
	builtin_interfaces/Time stamp
		int32 sec
		uint32 nanosec
	string frame_id
                             # the first ray in the scan.
                             #
                             # in frame frame_id, angles are measured around
                             # the positive Z axis (counterclockwise, if Z is up)
                             # with zero angle being forward along the x axis

float32 angle_min            # start angle of the scan [rad]
float32 angle_max            # end angle of the scan [rad]
float32 angle_increment      # angular distance between measurements [rad]

float32 time_increment       # time between measurements [seconds] - if your scanner
                             # is moving, this will be used in interpolating position
                             # of 3d points
float32 scan_time            # time between scans [seconds]

float32 range_min            # minimum range value [m]
float32 range_max            # maximum range value [m]

float32[] ranges             # range data [m]
                             # (Note: values < range_min or > range_max should be discarded)
float32[] intensities        # intensity data [device-specific units].  If your
                             # device does not provide intensities, please leave
                             # the array empty.
```

Most of these attributes you can ignore for the purposes of this assignment. The one that you will really need to dig into is ranges. The ranges attribute provides 361 numbers where each number corresponds to the distance to the closest obstacle as detected by the laser scan at various angles relative to the robot. Each measurement is spaced exactly 1 degree apart. The first measurement corresponds to 0 degrees in the image of the Neato above. As the degrees in the image go up, so to does the index in the ranges array. Where does 361 come from? The last measurement (index 360) is the same as the first (index 0). Why do we do this craziness?!? We have to do this to adhere to some ROS conventions around LaserScan data that will be important later in the class. For now, you can safely ignore the last measurement (index 360).

### ``stable_scan``

This gives the same data as ``scan`` except the timestamp is automatically adjusted to keep the detected points stable in the odometry frame.  This topic is really only need with the physical Neato robot where the precise timing of the LIDAR is not available due to hardware limitations.

### ``tf``

This is provided by the [tf2 module](https://docs.ros.org/en/galactic/Tutorials/Intermediate/Tf2/Introduction-To-Tf2.html) to update the relationhsip between various coordinate systems.  Typically you don't subscribe to it directly but instead use the Python tf module.

### ``tf_static``

This is provided by the [tf2 module](https://docs.ros.org/en/galactic/Tutorials/Intermediate/Tf2/Introduction-To-Tf2.html) to update the relationhsip between various coordinate systems.  Typically you don't subscribe to it directly but instead use the Python tf module.




## Putting the Neato Away

### Step 1: Turn Raspberry Pi Off

To do this, use the buttons on the Raspberry Pi.  First, press down until you see the text "Press select to Shutdown".  Next, press select to shut the Pi down.  Note: the button press detection code is a bit finicky, be persistent!


### Step 2: Wait for the Pi to completely power off, and then disconnect the battery.

This is really important.  If you pull the power to the Pi to soon, the SD card can become corrupted. As the Pi shutsdown you will see the green light flash as the red light stays on persistently.  At some point you will see the green light flash on and off at regular intervals (about once a second).  Once these flashes are over and you see no more activity for the green LED, the Pi is completely off.  At this point it is safe to pull the USB cable from the battery (do not remove the end of the cable attached to the Pi).

### Step 3: Put Away Your Toys

Place the Neato back in it's charging dock.  Connect the USB battery pack up to the charger.



<p align="center">
<img alt="a picture of the Botvac's charger" src="../website_graphics/neato_botvac_charger.jpg" width="40%"/>
</p>
<p align="center">
<i>The BotVac charger (notice the lip on the bottom)</i>
</p>

Checklist:

1. Make sure the two metal connectors on the back of the Neato have made contact with the charging station.
2. Make sure the USB battery is charging (the lights on the battery should turn on momentarily when you plug it in).

## Troubleshooting

### Symptom: Both the red and green LEDs on the raspberry pi are illuminated and not flashing.

Likely cause: the Pi was unable to boot from its SD card.

* Solution 1: the first thing to check is that the Raspberry Pi's SD card is fully inserted into the Raspberry Pi.  See the image below for the location of the SD card.  You will know it is fully inserted if you push on the card and it clicks into place.
* Solution 2: if the card is fully inserted, the SD card may have become corrupted (possibly because some people didn't properly shut down the Raspberry Pi!).  To remedy this, grab an SD card from the green container located in the plastic drawers in AC112.  Put the old SD card in the red container in the same plastic drawer.

### Symptom: the raspberry Pi display's backlight is flashing on and off.

Likely cause: the Pi cannot connect to the robot via the USB cable.

Solution: sometimes the Neato will turn off due to inactivity.  Press the large button near the Neato display to wake it up.  If that doesn't work try unplugging and replugging the USB cable from the raspberry Pi (DO NOT unplug the USB cable from the side connected to the Neato).  If that doesn't work, shutdown and then reboot the Pi.  If none of this works, the robot battery might be dead.  Try recharging the robot.  While the robot is recharging, switch to another robot.

### Symptom: the Wifi signal strength indicator on the Raspberry Pi is below 40 even though you are right near an access point.

Likely cause: The Pi has connected to an access point that is not the closest one (this will sometimes happen).

Solution: Assuming the Pi display is at the screen showing the IP address, press right to enter the network setup menu.  OLIN-ROBOTICS should be highlighted with an asterisk.  Press right again to reconnect the Pi to the Wifi.  If it doesn't work the first time, try one more time.  If it doesn't work then, switch to a new robot.



# Running the Simulator

<p align="center">
<img alt="screenshot of a Neato in an empty simulated environment" src="../website_graphics/neato_gazebo.png"/>
</p>

Here are the instructions for using the robot simulator.  The current plan is to use the simulator for in-class activities.  This decision is based on the amount of chaos that would ensue in such a large class if every group had their own robot.  If we get to the point where the physical robots are working super smoothly, we can revisit this idea.

## What is a Robot Simulator?

Without getting into too much detail, a robot simulator is software that simulates a robot interacting with some sort of environment.  As such, a simulator will typically provide the following major functionality.

* It will provide a means to specify the physical layout of the robot's environment (e.g., the location of obstacles, the physical properties of various surfaces).
* It will provide a means to specify a robot model (e.g., the robot's sensors, actuators, mass, inertia, etc.).
* It will provide simulated sensor data (i.e., what *would* the robot's sensors have reported if the robot were in a particular environment in a particular location).
* It will provide a means to execute simulated motor commands (i.e., it will let you tell the robot to move).
* It will provide a way to visualize the simulation state (e.g., as a graphical rendering).

One nice thing about ROS is that the usage of a publish and subscribe structure provides a very clean separation between the robot itself and code that you will write to program the robot.  For instance, you can write a motor control node that sends commands to the topic ``cmd_vel``.  This program can work with any real or simulated robot so long as it subscribes to the ``cmd_vel`` topic and executes the appropriate motor command in response to the messages it receives (e.g., the motor command might involve moving a real motor or it might involve moving a simulated robot).

### Differences with RViz

Oftentimes students will be confused as to what the difference is between RViz and a robot simulator.  RViz allows you to visualize a robot's sensor data.  As such, RViz has a graphical interface that can look a lot like the graphical interface of the robot simulator.  In contrast, RViz does not have any means to execute a simulated motor command or generate simulated sensor data: it can only display the data that it receives.

We will be using the popular Gazebo software for robot simulation.  Gazebo is a very powerful and customizable simulator that will be especially useful in this online (virtual) version of the course.

## Starting the Simulator

You can launch your robot in many different simulated worlds.  To start your robot in an obstacle course environment, run the following command (this will probably look familiar).

{% include codeHeader.html %}
```bash
ros2 launch neato2_gazebo neato_gauntlet_world.py
```

<p>If all went well, you will see a bunch of output stream by and a visualization that looks like the following.</p>

<p align="center">
<img alt="screenshot of a Neato in the simulated obstacle course" src="../website_graphics/gauntlet_gazebo.png"/>
</p>

<p>If you want to create your own world, you can put the Turtlebot in an empty world and then follow our instructions for <a href="#populating-the-simulated-world">populating your own world</a>.</p>

## Using the Gazebo Graphical Interface

The Gazebo website has a [guide on using Gazebo's graphical interface](http://gazebosim.org/tutorials?cat=guided_b&tut=guided_b2).

## Available Topics

This documentation gives the high-level purpose of each topic.  To explore more, you can use the following command to get more information.

```bash
$ ros2 topic info /topic-name
```

If you want to know more about a message you see in the output of ``rostopic`` you can use the following command (note that the ``-r`` flag can be ommitted if you want to the mesasges nested within the top-level message to be expanded).

```bash
$ ros2 interface show msg_package_name/msg/MessageName
```

### ``accel``

This is the linear acceleration of the Neato in meters per second squared along each axis of the Neato.  This same information is included in the ``imu`` topic (although there it is nested further).

### ``bump``

This topic contains four binary outputs corresponding to each of the Neato's four bump sensors.  In the simulator, all bump sensors are either on or off (no differentiation is made between the bump sensors).

### ``bumper``

This is an internal topic to Gazebo.  If you are curiouts, you can look at the output as you run into something, but you don't need to worry about it in this class.

### ``camera/image_raw``

These are the images coming from the simulated camera.

### ``clock``

This is the simulator clock.  This is useful for executing commands based on elapsed time.  It is preferable to use this clock rather than the wall clock (your computer's system clock) since the simulation might not run at the same rate as realtime.  You don't typically want to subscribe to this topic directly.  Instead, if you have a ``rclpy.node.Node`` subclass (common), you can grab the current time through ``self.get_clock().now()``.

### ``cmd_vel``

You publish to this topic to set the robot's velocity.  The ``linear.x`` direction sets forward velocity and ``angular.z`` sets the angular velocity.

### ``imu``

This is the simulated IMU (intertial measurement unit).  It has linear acceleration and angular velocity.

### ``joint_states``

These tell you the total rotation (in radians) of each wheel.  Note that this is a "ground truth" value, meaning that it is not estimated from sensors but instead comes from Gazebo.  In a scenario with a real robot, you wouldn't have access to this.

### ``odom``

This tells you the robot's position relative to its starting location as estimated by wheel encoders.  You can get this inforation more flexibly through the ROS tf module, but this is a relatively easy way to get started.

### ``projected_stable_scan``

This provides the LIDAR measusrements (think of these as detected obstsacles or objects from the environment).  In contrast to the ``scan`` topics, these measurements are in the odometry frame (rather than relative to the robot) and are in Caretesian rather than polar coordinates.  There is no need to use this topic, but for some applications it is nice to have.

### ``rosout``

This is a topic provided by ROS.  See the [ROS docs on ``rosout``](http://wiki.ros.org/rosout)for more information.

### ``scan``

These are the measurements of the Neato's LIDAR.  See the documentation for the physical Neato for more details.


### ``stable_scan``

These are the measurements of the Neato's LIDAR.  For the physical Neato, this will have a different time stamp than ``scan``, but for the simulated Neato it is identical to the ``scan`` topic.  See the documentation for the physical Neato for more details.

### ``tf``

This is provided by the [tf2 module](https://docs.ros.org/en/galactic/Tutorials/Intermediate/Tf2/Introduction-To-Tf2.html) to update the relationhsip between various coordinate systems.  Typically you don't subscribe to it directly but instead use the Python tf module.

### ``tf_static``

This is provided by the [tf2 module](https://docs.ros.org/en/galactic/Tutorials/Intermediate/Tf2/Introduction-To-Tf2.html) to update the relationhsip between various coordinate systems.  Typically you don't subscribe to it directly but instead use the Python tf module.

## Using Rviz with the Simulator

Once the simulator is running, you can setup ``rviz2`` the same way you would for the physical Neato.

## Shutting Down the Simulator

Go to the terminal where you launched Gazebo and hit control-c.

## Support for Multiple Neatos (beta)

We now have beta support for connecting to two (or more) Neatos simultaneously.  There are a few rough edges right now, but all of the functionality is available.  To get started, you'll have to switch your ``neato_packages`` branch over to ``multiagent_support`` and then rebuild ``ros2_ws`` (eventually we will merge the ``multiagent_support`` branch into ``main``).

```bash
$ cd ~/ros2_ws/src/neato_packages
$ git pull
$ git checkout multiagent_support
$ cd ~/ros2_ws
$ colcon build --symlink-install
$ source install/setup.bash
```

You can now connect to the Neatos using the following commands (making these shorter is one of the rough edges we are hoping to smooth out).  

Launch the first Neato.

```bash
$ ros2 launch neato_node2 bringup_multi.py host:=neato1-ip-address-here robot_name:=robot1 udp_video_port:=5002 udp_sensor_port:=7777 gscam_config:='udpsrc port=5002 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264  ! videoconvert'
```

Launch the second Neato (if you are interested in generalizing this to more than 2 Neatos, take note of the things that change between the invocations other than the Neato IP addresses, e.g., the port numbers).

Launch the second Neato.

```bash
$ ros2 launch neato_node2 bringup_multi.py host:=neato2-ip-address-here robot_name:=robot2 udp_video_port:=5003 udp_sensor_port:=7778 gscam_config:='udpsrc port=5003 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264  ! videoconvert'
```

If all goes well, you should see the following topics.

```bash
$ ros2 topic list
/robot1/accel
/robot1/bump
/robot1/camera/camera_info
/robot1/camera/image_raw
/robot1/camera/image_raw/compressed
/robot1/camera/image_raw/compressedDepth
/robot1/camera/image_raw/theora
/robot1/cmd_vel
/robot1/joint_states
/robot1/odom
/robot1/projected_stable_scan
/robot1/robot_description
/robot1/scan
/robot1/stable_scan
/robot2/accel
/robot2/bump
/robot2/camera/camera_info
/robot2/camera/image_raw
/robot2/camera/image_raw/compressed
/robot2/camera/image_raw/compressedDepth
/robot2/camera/image_raw/theora
/robot2/cmd_vel
/robot2/joint_states
/robot2/odom
/robot2/projected_stable_scan
/robot2/robot_description
/robot2/scan
/robot2/stable_scan
/rosout
/tf
/tf_static
```

Notice how the topics are now nested underneath the namespace ``robot1`` and ``robot2``.

To test this out, you can launch the teleop node with a remapping rule to have it control either the first or second robot.

Control the first robot:
```bash
$  ros2 run teleop_twist_keyboard teleop_twist_keyboard cmd_vel:=robot1/cmd_vel
```

Control the second robot:
```bash
$  ros2 run teleop_twist_keyboard teleop_twist_keyboard cmd_vel:=robot2/cmd_vel
```

The coordinate frames have also been modified.  For example, ``odom`` becomes ``robot1odom`` or ``robot2odom`` depending on which robot you are working with.

A simple test to do with multiple Neatos is to drive them in unison!

<iframe width="560" height="315" src="https://www.youtube.com/embed/nVWZCXykC80" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
