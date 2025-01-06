---
title: "Reading a Technical Research Paper // Debugging, Proportional Control, and ROS Parameters"
toc_sticky: true
toc_data:
  - title: Today
    link: in-class/day04/#today
  - title: For Next Time
    link: in-class/day04/#for-next-time
  - title: Reading a Technical Research Paper
    link: in-class/day04/#technical-research-paper
  - title: Brainstorming Robot Debugging Strategies
    link: in-class/day04/#brainstorming-robot-debugging-strategies
  - title: ROS and Threading
    link: in-class/day04/#ros-and-threading
  - title: ROS Params and Proportional Control
    link: in-class/day04/#proportional-control
---

## Today
* Reading a Technical Research Paper (For Your Consideration)
* Robot Debugging Strategies (Group Exercise)
* ROS and Threading (Code Walk-Through)
* ROS Params and Proportional Control (Coding Exercise)
* Studio Time

## For Next Time
* Work on the <a href="../assignments/warmup_project">the Warmup Project</a>.  There is an intermediate checkpoint due on **Tuesday 17th at 1PM** ([assignment page on Canvas here](https://canvas.olin.edu/courses/822/assignments/13048)).
  * If you haven't already, please list your team and a link to your Github on the [Teaming Sheet](https://docs.google.com/spreadsheets/d/1ZIrGQ0a1rUCSRbk-eYSmbnXTedQA_49HQXRUSJu2z4Y/edit?gid=0#gid=0).
  * The final warm-up project deliverables will be due **Monday 23rd at 7PM**!
  * A rubric for the project is available [on Canvas](https://canvas.olin.edu/courses/822/assignments/13049).
* Work on the [Broader Impacts assignment Part 1](../assignments/broader_impacts), due on **Friday 27th at 1PM** (changed date!)

## Reading a Technical Research Paper (For Your Consideration)
As you progress through this class, you may want to consider reading technical papers to gather ideas for algorithms to test, open-source code to integrate into your solutions, or academic perspectives for your Broader Impacts assignment. Technical writing is its own art form, as is reading a piece of technical writing. Here is how I read a technical paper when I'm trying to learn more about a certain technique or field:
* **Start with the Abstract and Intro, then read the Conclusion.** To get a real sense for what a research paper is really about (what its core contribution is, the motivation of the work, and how it is related to other work in the field broadly) you should consider reading it out of order. The Abstract, Introduction, and Conclusion sections will hit the key points of the paper, and help you understand what details you might want to learn more about as you read the rest.
* **Read Every Figure Caption.** In the best papers, figures serve as a pictorial representation of the methods and the results. 
* **Read the Results.** Get a sense for how an algorithm or method performs. Do you trust in the performance metrics? Are the results statistically significant? Do the results align with the motivation of the work? If the results don't pass a "sniff check" then you might consider moving on to another paper.
* **Read the Methods.** This is often the most technical parts of a technical paper, and may include pseudocode, mathematical derivations and proofs, or system diagrams. If you've gotten to this step, it's worth skimming this section first, then reading it a second time in considerably more detail. Marking up a print copy or PDF version is recommended -- taking notes helps to process the material and generate questions that you can follow-up on with other reading or experimentation of your own.
* **Read the Related Works.** This is where you see all the fundamental work that the algorithm you're reading about was built on (helpful if you want to learn more about some methods in the paper) and contemporary work that the algorithm may compare itself too (helpful if you want to look at different strategies to solve the same / similar problems).
* **Skim the Whole Paper End-to-End.** Finish reading a paper by giving it a final skim in order, paying attention to the headings, key contribution statements, and how each section feeds into the next. This gives you a nice sense of the complete body of the work, helps you reassess the Results and Conclusion sections with more information from the Methods section, and can help you summarize the paper in your notes.

 Here are a few technical papers on state estimation and localization (our next unit!!) that may be interesting launch-points to learning more about these topics:
 * [ORB-SLAM: A Versatile and Accurate Monocular SLAM System](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7219438&casa_token=WVatKv5yIlgAAAAA:hJr0vy9MMdOkC6xrXPaYf-Yn91nXjGZRsqraEj-6UrRg656-j564yYNUooPZ2EOqKGghpSVj66E) by Mur-Artal et al., 2015
 * [Real-Time Loop Closure in 2D LIDAR SLAM](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7487258&casa_token=G_B93iYLcQYAAAAA:dCwVkq4rnNN28ojorfB5krmbOr3oETCstdLSrSoSleAORaElFFhyrZ3j1xKx8gRifKlFBhbMiNo) by Hess et al., 2016
 * [Back to the Feature: Learning Robust Camera Localization from Pixels to Pose](https://openaccess.thecvf.com/content/CVPR2021/papers/Sarlin_Back_to_the_Feature_Learning_Robust_Camera_Localization_From_Pixels_CVPR_2021_paper.pdf) by Sarlin et al., 2021
 * [Autonomous Navigation System of Greenhouse Mobile Robot Based on 3D Lidar and 2D Lidar SLAM](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.815218/full) by Jiang et al., 2022

 Technical papers can be searched for in Library databases, [Google Scholar](https://scholar.google.com/), professional organization archives of journals and/or conferences (e.g., [IEEE Xplore](https://ieeexplore.ieee.org/Xplore/home.jsp)), or in open archives (e.g., [arXiv](https://arxiv.org/) -- Note that open archives are open...so not all work here may be peer-reviewed!). 


## Brainstorming Robot Debugging Strategies
Debugging is the act of incrementally testing code for accurate behavior and tracing errors back through the system to resolve them. You may have encountered some [debugging strategies in SoftDes](https://softdes.olin.edu/docs/readings/unit-testing-basics/). Some generic strategies for debugging software carry over to robotics programming, while novel methods may need to be included given the interaction software has with hardware. 

### Group Discussion
Take 10 minutes to come up with some debugging strategies for writing robotics code with the folks around you, then we'll share out to the class. As a motivating example, let's consider the part of <a href="../assignments/warmup_project">the Warmup Project</a> where you have to create a person follower.

Here are some areas to consider in the debugging / development lifecycle:
1.  How do you ensure your code is correct (implements the strategy you expected)?
2.  How do you test your approach to see if it performs the task effectively (e.g., follows a person)?
3.  How might you tune the parameters of your approach to make it perform as best possible?


## ROS and Threading
A "thread" is an independent flow of execution in a computer program; "threading" refers to creating multiple concurrent pathways for execution. When using ROS2, the concept of threading can arise in multiple ways, but one common one is when we utilize our subscription callbacks _and_ create running loops within our code.

We'll go over some points regarding how ROS2 deals with different threads of execution.  In order to structure our work, we're going to be looking at two pieces of sample code:

> Note: you might find looking at these pieces of code quite useful for the Warm-Up Project!

* [Drive Square Sample 1](../Sample_code/drive_square_sample_1): Single-Threaded Task Execution in ROS2
  * [C++ Version](../Sample_code/drive_square_sample_2) for those interested.
* [Drive Square Sample 2](../Sample_code/drive_square_sample_3): Multi-Threaded Task Execution in ROS2

Why would we want to perform threading, as opposed to timing (as we have been)?
* **Avoiding "blocked" callbacks**: in sequential execution, the callbacks are executed one at a time, and blocked from being triggered until the previous has finished. If we happen to put a lot of "work" in a callback, we could delay execution down the line. Threading avoids this issue (kinda...in Python there isn't truly a way for parallel processing, but nonetheless execution can _overlap_ which can be incredibly helpful.).
* **Timing can be fraught**: if we sent a timer, then anything in that loop must execute within that time or weird / unintended behavior can occur. Threading allows callbacks to occur at their own time.
* **Threading gives us control of information flow**: within ROS2, the use of threading allows us the flexibility to choose what callbacks occur when in execution (and therefore what work or data is consistently protected from deadlocking).

If you want to learn more, [this conversation on the ROS discourse](https://discourse.ros.org/t/how-to-use-callback-groups-in-ros2/25255) is an excellent source!

## Proportional Control

So far we've programmed robots to choose between a small set of motor commands (move forward, stop, etc.) based on sensor readings.  Today, we will be experimenting with setting the motor command proportional to the error between the robot's current position and the desired position.

To get the idea, program the Neato to adjust its position so that it is a specified (target) distance away from the wall immediately in front of it. The Neato's forward velocity should be proportional to the error between the target distance and its current distance. It's tricky to get the sign correct, run through a few mental simulations to make sure the robot will move in the right direction. 

> Note: you might be interested in adapting this in your Warm-Up project wall-follower or person-follower code!

To get started, create a package somewhere in your ``ros2_ws/src`` directory for your work.  In this example, we can put the package directly in ``ros2_ws/src/class_activities_and_resources`` directory then rebuild the workspace:

```bash
$ cd ~/ros2_ws/src/class_activities_and_resources
$ ros2 pkg create in_class_day04 --build-type ament_python --node-name wall_approach --dependencies rclpy std_msgs geometry_msgs sensor_msgs neato2_interfaces
$ cd ~/ros2_ws
$ colcon build --symlink-install
$ source ~/ros2_ws/install/setup.bash
```

You may have noticed at this point that ROS requires a certain amount of [boiler-plate code](https://en.wikipedia.org/wiki/Boilerplate_code) to get going.  If you are having trouble with this, or would rather skip ahead to the proportional control part, [you can grab some starter code for ``wall_approach.py``](../Sample_code/wall_approach_starter).

A helpful tool for visualizing the results of your program is to use <a-no-proxy href="https://docs.ros.org/en/humble/Concepts/About-RQt.html">rqt</a-no-proxy>.  First, start up the GUI:

```bash
$ rqt
```

Next, go to ``plugins -> visualization -> plot``.

Type ``/scan/ranges[0]`` (if that is in fact what you used to calculate forward distance) into the topic field and then hit `+`. 

> Tip: to change the zoom in the plot, hold down the right mouse button and drag up or down on the body of the plot (it's pretty finicky, but it does work).

You can use this link to find [a sample solution to this task](https://github.com/comprobo24/class_activities_and_resources/blob/main/in_class_day04_solutions/in_class_day04_solutions/wall_approach.py).

### Getting Fancy: ROS Params

To make a node more configurable, you can use ROS Params, which allow us pass in arguments to a node from the commandline (or control them through tools like `rqt`). This is super powerful, because it can let you, in real time, adjust your robot performance and behavior without killing, re-writing, and re-running your nodes. For proportional control, we could set our proportional coefficient and our wall distance in this way.
* See the [ros param command line tools documentation](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters.html) for more information
* [Code for accessing parameters in Python documentation from The Robotics BackEnd](https://roboticsbackend.com/rclpy-params-tutorial-get-set-ros2-params-with-python/) (which might be a bit easier to parse than the [official one](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Using-Parameters-In-A-Class-Python.html)). 

For instance, if you follow the documentation you can create a node similar to our [sample solution, ``wall_approach_fancy.py``](https://github.com/comprobo24/class_activities_and_resources/blob/main/in_class_day04_solutions/in_class_day04_solutions/wall_approach_fancy.py) that supports the following customization via the command line:

```bash
$ ros2 run in_class_day04_solutions wall_approach_fancy --ros-args -p target_distance:=1.5 -p Kp:=0.5
```

Here is a demo of the script, ``wall_approach_fancy.py`` that uses ROS parameters as well as the tool ``dynamic_reconfigure`` for easy manipulation of various node parameters.
> Note that in order to support ``dynamic_reconfigure`` in your nodes, you have to call ``add_on_set_parameters_callback`` and implement an appropriate callback function (see sample solution for more on this).

![An animated Gif that shows a robot attempting to maintain a particular distance from a wall](day04images/wall_approach_fancy_ros2.gif).
