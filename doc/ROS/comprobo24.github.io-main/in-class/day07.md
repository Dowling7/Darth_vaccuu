---
title: "Searching for What? // The Particle Filter for Robot Localization"
toc_sticky: true
toc_data:
  - title: Today
    link: in-class/day07/#today
  - title: For Next Time
    link: in-class/day07/#for-next-time
  - title: Searching for What?
    link: in-class/day07/#searching-for-what
  - title: The Particle Filter Algorithm
    link: in-class/day07/#the-particle-filter-algorithm
  - title: Project Kick-Off
    link: in-class/day07/#project_kickoff
---

## Today 

* Searching for What? 
* Particle Filter Conceptual Overview
* We're All Living in a 1D World! Part 2: Code Dissection
* Project Kick-Off

## For Next Time

* Work on the [Broader Impacts assignment Part 1](../assignments/broader_impacts), due on **Friday 27th at 1PM**.
* Complete the [Particle Filter Conceptual Overview](../assignments/robot_localization#conceptual-overview-due-9-22) (submitted individually!), due on **Tuesday October 1st at 1PM**.
* [Form a team](https://docs.google.com/spreadsheets/d/1rE78CwfC8EZzauaegFujHMeQZMqxPuFwX2tCbE_3v44/edit?usp=sharing) and review [a view of the finish line](../assignments/robot_localization#a-view-of-the-finish-line-and-getting-set-with-rviz)
* Consider whether there is [feedback you'd like to share about the class](https://forms.gle/giCwA1pkr4y3e4T37)

## Searching for What?
Let's take a moment to look at some ["Search and Rescue" literature](https://docs.google.com/document/d/1Kh-o200z_Mka8x0qxfmXLT8NUsOPwWfDQTfnHtcw02g/edit?usp=sharing) and discuss:
* Is what is being sought named in these papers?
* How often is a real robot or real environment shown in these papers?
* When referring to "search and rescue" what other applications may be listed? Or what specific organizations or scenarios are mentioned, if any?
* Who funded the work?
* Is the robot or robot system mostly a "searcher" or a "rescuer"?
* Do the papers make mention of how human operations specialists will interact with the robot?

## The Particle Filter Algorithm
We're going to kick-off this project with a bit more of analytical dive into a particle filter algorithm, then look at some sample code to ground our understanding in implementation. 

### What Does the Robot Know? What Can the Robot Sense?
In our lives, we "localize" by observing our surroundings, maybe checking our GPS location, and referencing a map of our area (either conceptual or actual) to claim "we are here." The robot needs to do the same thing in this project. We can assume the following about our robot:

1. It has a _map_ of the region it is in, but **it does not know where it is within that map**
2. It can observe the world through bumps and laser scans; those sensors are rigidly attached to the body of the robot. **These sensors are noisy**
3. It can explore the world by rolling around; it can **guesstimate how far it has rolled** by keeping track of its velocity and wheel turns.

### Coordinate Systems
There are several coordinate systems that we'll want to consider when localizing:
* ``map`` -- the coordinate system of the map/environment that the robot is in
* ``odom`` -- the coordinate system that _initializes where-ever the robot is_ and in which the robot's motion is tracked
* ``base_footprint`` -- the coordinate system that is attached the robot (where laserscans would be in reference to, for instance)

Which of these are static relationships? Dynamic? How would we think about updating any relationship between these frames?

### The Steps (At a High Level)
We're going to walk through the high-level steps of a particle filter, highlighting along the way the different opportunities for design choices you have as a software engineer. We'll be connecting with the video you watched prior to this class to discuss.

The key steps:
1. **Initialize** Given a pose (represented as $$x, y, \theta$$), compute a set of particles.
2. **Motion Update** Given two subsequent odometry poses of your robot, update your particles.
3. **Observation Update** Given a laser scan, determine the confidence value (weight) assigned to each particle.
4. **Guess** Given a weighted set of particles, determine the robot's pose.
5. **Iterate** Given a weighted set of particles, sample a new set.

Steps 3 and 5 are typically considered the "tricky" ones to implement. Let's take some time to brainstorm possible methods that could be adopted (at a high level) to solve these challenges.

## We're All Living in a 1D World! Part 2: Code Dissection
Group up with the folks around you, and have a look at the code for the ``simple_particle_filter`` demo we ran last class. Diagram out the code and topics...can you map different functions/classes of the code to the high-level steps we've outlined in class? What are you noticing about the implementation? What questions do you have about the techniques used?

## Project Kick-Off
Starting today, the particle filter project is a-go! There is [skeleton code available for this project](https://github.com/comprobo24/robot_localization), which I recommend you have a look at now. The rest of this class will be studio time for Broader Impacts Part 1 or starting your conceptual diagramming.
