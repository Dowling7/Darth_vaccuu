---
title: "Intro to Search and Rescue // A 1D Particle Filter"
toc_sticky: true
toc_data:
  - title: Today
    link: in-class/day06/#today
  - title: For Next Time
    link: in-class/day06/#for-next-time
  - title: An Intro to Search and Rescue
    link: in-class/day06/#intro-to-search-and-rescue
  - title: Conceptual Introduction to the Particle Filter
    link: in-class/day06/#conceptual-introduction-to-the-particle-filter
  - title: We’re all living in a 1D world!
    link: in-class/day06/#were-all-living-in-a-1d-world
---

## Today
* An Intro to Search and Rescue
* Conceptual Introduction to the Particle Filter
* We're all living in a 1D world! (a simple particle filter example)
* Studio Time

## For Next Time
* Work on the <a href="../assignments/warmup_project">the Warmup Project</a>.
  * The final warm-up project deliverables will be due **Tuesday 24th at 7PM**!
  * A rubric for the project is available [on Canvas](https://canvas.olin.edu/courses/822/assignments/13049).
* Work on the [Broader Impacts assignment Part 1](../assignments/broader_impacts), due on **Friday 27th at 1PM**.
* Read over the description of the [Robot Localization project](../assignments/robot_localization).
* For more reinforcement of the concepts behind the particle filter, watch this <a href="https://www.youtube.com/watch?v=aUkBa1zMKv4">video</a>.

## An Intro to Search and Rescue
State estimation and localization are absolutely fundamental to robotics -- in order to do useful work, we need to know where a robot is in relation to a world map or objects within an environment. Perhaps one of the most widely used application motivations for sophisticated state estimation and localization is "search and rescue" -- the act of mapping a space to seek a target object, that may also be retrieved (or marked for retrieval by specialized systems/people). 

[These slides](https://docs.google.com/presentation/d/1XXOwbKphKXfRPb68auAqU19UuMyBW6DK3wda2-Kgg1Q/edit?usp=sharing) give a sense of the "search and rescue" landscape in modern robotics as it relates to state estimation and localization.


## A Conceptual Introduction to the Particle Filter

How does a robot know where it is? We'll be doing an activity to introduce our next major topic in the class: robot localization. This is supposed to be a fun activity to get you thinking about the basic concepts of one tool for localization, the particle filter.

## We're all living in a 1D world!

Let's see how particle filtering might manifest computationally. To get the code for today you will need to make sure your environment is setup with matplotlib and scipy. If you want to check you can use

{% include codeHeader.html %}
```bash
pip3 show matplotlib scipy
```

If you get any warnings about package(s) not found, you can install them with ``pip3``.  For example, if you didn't have either package, you can use the following command to install the necessary libraries.

{% include codeHeader.html %}
```bash
pip3 install matplotlib scipy
```

Additionally, if you haven't done so yet, clone [the class activities are resources repo](https://github.com/comprobo23/class_activities_and_resources) into your ``ros2_ws/src`` folder.  If you've already cloned it, make sure to do a ``git pull origin main``.

Next, make sure to build your workspace and source your ``install/setup.bash`` file.

```bash
$ cd ~/ros2_ws
$ colcon build --symlink-install
$ source install/setup.bash
```
### Launch a Simulated World
To try things out, let's first startup a 1d simulation of the world. 

{% include codeHeader.html %}
```bash
ros2 run simple_filter simple_filter_world.py --ros-args -p walls:=[0.0,3.0]
```

Take a look at the topics that are being published.  What types of messages are there?  What topics correspond to which messages?  We'll go through this as a class.


### Launch a Particle Filter
Next, we will experiment with our first particle filter:

{% include codeHeader.html %}
```bash
ros2 run simple_filter simple_particle_filter.py --ros-args -p walls:=[0.0,3.0] -p nparticles:=100
```

A visualization should come up.  The visualization shows the position of all the particles, the particle weights, and the true position.  Additionally, a histogram is generated that shows the belief about where the robot is.

### Explore the World -- Where Are You?

You can move your robot around using the following ROS node:

{% include codeHeader.html %}
```bash
ros2 run simple_filter simple_controller.py
```

To use this node make sure the window that pops up has focus, and use the ``a`` key and the ``d`` keys to move around left to right, respectively.

What happens over time to your visualization?

Try different wall configurations to see what happens.  What happens as you change the number of particles?  What happens if the wall configuration of the simulator and the particle filter model don't match up? 

Construct a scenario where there is an inherent ambiguity in determining where the robot is.  How do you do this?  What happens when you run your particle filter?
