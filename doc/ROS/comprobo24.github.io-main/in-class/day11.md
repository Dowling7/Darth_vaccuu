---
title: "Applied SAR Robotics // Debugging Strategies, Extensions, and Studio"
toc_sticky: true
toc_data:
  - title: Today
    link: in-class/day11/#today
  - title: For Next Time
    link: in-class/day11/#for-next-time
  - title: Applied Search and Rescue Robotics
    link: in-class/day11/#applied-sar
  - title: Particle Filter Debugging Techinques
    link: in-class/day11/#particle-filter-debugging-techinques
  - title: Extensions to the Particle Filter
    link: in-class/day11/#extensions-to-the-particle-filter
---

## Today
* Applied Search and Rescue Robotics (Discussion)
* Particle Filter Debugging Strategies (For Your Consideration)
* Extensions to the Particle Filter (For Your Consideration)
* Studio

## For Next Time
* Work on the [Robot Localization project](../assignments/robot_localization)
  * Demos due on **Thursday October 17th In-Class**
  * Code + Writeups due on **Friday October 18th 7PM**
* Read over the [Broader Impacts assignment Part 2](../assignments/broader_impacts), due on **November 5th at 7PM** 
  * Note -- discussions will happen on October 28th, October 31st, and November 4th; stay tuned!
* Consider whether there is [feedback you'd like to share about the class](https://forms.gle/giCwA1pkr4y3e4T37)
* **Extra Credit** An assignment to [reinforce probability fundamentals](../assignments/probability_basics/assignmentprobability_basics.pdf) is available to complete for extra credit (to be applied to the state estimation and localization unit). Due on **Friday October 18th 7PM** for those interested; [check the Canvas page for submission instructions](https://canvas.olin.edu/courses/822/assignments/13050).

## Applied Search and Rescue Robotics
We've been briefly discussing this unit about Search and Rescue as an umbrella application area for robotics. We've had a look at the landscape of the field, skimmed some technical papers, and highlighted some key related algorithms. Today, we're going to discuss practical design choices when looking towards deploying SAR robots, and what their implications might be.

> Before digging into this discussion today, I want to pause to acknowledge the ongoing hurricane-related emergencies in the US Southeast. Our discussion today will touch on FEMA, search and rescue scenarios, and how to best serve vulnerable populations; and it is impossible and irresponsible not to recognize the thematic connections with ongoing events. Students who may feel affected by the content are welcome to step out at any point.

### Setting Standards
In the US, the Federal Emergency Management Agency (FEMA), Homeland Security, and the Department of Defense are among the largest customers of SAR robots. In partnership with NIST (the National Institute of Standards and Technology), the guidelines for an effective/useable SAR system for urban environments has been defined ([you can read more here](https://www.nist.gov/system/files/documents/el/isd/ks/Prelim_Requirements_Report.pdf)) and covers the following:

* Human-System Interaction (23 requirements)
* Logistics (10 requirements)
* Operating Environment (5 requirements)
* System (physical robot) (65 requirements; 32 of which are for sensing)

One of the fascinating things about these requirements is that "Human-System Interaction" primarily covers the _robot operator_ but not the interaction with a possible human rescuee. In your small groups, consider the following questions from the perspective of a NIST engineer tasked with setting requirements for a SAR robot (I recommend picking one or two to focus on):

* What would/should official standards for Human-System Interaction cover for the rescuee of a SAR robot? 
  * You may want to consider: interfaces (virtual, sensory, or physical); accessibility; meta-safety; inclusivity...
* How would these standards interact with your robot's sensors? Algorithms?
  * You may want to consider: role of automation/autonomy; consequences of perceptual limitations; edge-cases for perception choices; introduction of bias (implicit or explicit); verifiability; explainability...
* Who should be involved in co-designing this set of standards for this group of stakeholders?
  * The current standards were set based on several workshops with experts in the field (peep the list in the linked report above...notice anything interesting about this group?)
* What tests would need to be designed to assess whether a robot met these standards?


## Particle Filter Debugging Techniques

### Using Python Debugger ``pdb``

In order to use ``pdb`` you'll want to change your workflow a little bit.  Instead of launching your particle filter and the map server through the ``test_pf.py`` launch file, you will be starting the map server separately and then launching your particle filter through your Python IDE (e.g., VSCode).

You can start the ``map_server`` using the following command:

{% include codeHeader.html %}
```bash
ros2 launch robot_localization launch_map_server.py map_yaml:=path-to-map-yaml 
```

If all went well, you will see the following output.

```bash
[INFO] [launch]: All log files can be found below /home/pruvolo/.ros/log/2022-10-07-11-30-28-273830-pruvolo-Precision-3551-7847
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [lifecycle_manager-2]: process started with pid [7851]
[INFO] [map_server-1]: process started with pid [7849]
[lifecycle_manager-2] [INFO] [1665156628.380768047] [lifecycle_manager]: Creating
[map_server-1] [INFO] [1665156628.382319035] [map_server]: 
[map_server-1] 	map_server lifecycle node launched. 
[map_server-1] 	Waiting on external lifecycle transitions to activate
[map_server-1] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-1] [INFO] [1665156628.382390679] [map_server]: Creating
[lifecycle_manager-2] [INFO] [1665156628.385117900] [lifecycle_manager]: Creating and initializing lifecycle service clients
[lifecycle_manager-2] [INFO] [1665156628.385653406] [lifecycle_manager]: Starting managed nodes bringup...
[lifecycle_manager-2] [INFO] [1665156628.385678064] [lifecycle_manager]: Configuring map_server
[map_server-1] [INFO] [1665156628.385812580] [map_server]: Configuring
[map_server-1] [INFO] [map_io]: Loading yaml file: gauntlet.yaml
[map_server-1] [DEBUG] [map_io]: resolution: 0.05
[map_server-1] [DEBUG] [map_io]: origin[0]: -1.36
[map_server-1] [DEBUG] [map_io]: origin[1]: -3.09
[map_server-1] [DEBUG] [map_io]: origin[2]: 0
[map_server-1] [DEBUG] [map_io]: free_thresh: 0.25
[map_server-1] [DEBUG] [map_io]: occupied_thresh: 0.65
[map_server-1] [DEBUG] [map_io]: mode: trinary
[map_server-1] [DEBUG] [map_io]: negate: 0
[map_server-1] [INFO] [map_io]: Loading image_file: ./gauntlet.pgm
[map_server-1] [DEBUG] [map_io]: Read map ./gauntlet.pgm: 71 X 76 map @ 0.05 m/cell
[lifecycle_manager-2] [INFO] [1665156628.391201344] [lifecycle_manager]: Activating map_server
[map_server-1] [INFO] [1665156628.391262492] [map_server]: Activating
[lifecycle_manager-2] [INFO] [1665156628.391473752] [lifecycle_manager]: Managed nodes are active
```

Now that the ``map_server`` is running, you can start the debugger through ``VSCode`` (as an example) by selecting ``Run`` and then ``Start with Debugging``.  Next, choose ``Python`` as your debugging configuration.  Make sure you have set the focus of ``VSCode`` to your ``pf.py`` script before doing this.  You can now set breakpoints or inspect your program's state in the event of a crash.

### Debugging Using Matplotlib

Sometimes it's easier to get a quick and dirty visualization going using a familiar tool like matplotlib.  You could consider using this for things like plotting particle weights or motion updates.

### Create Tests for Class Functions
You can create test scripts that confirm the logic in certain key functions of your particle filter using exemplar inputs with outputs you can hand compute.

### Use ROS2 Commandline Tools
Tools like `tf2`, `topic list/echo`, `node list`, and `rqt` are all really useful for checking on the status of your network. 

### Grab a Bagfile
In the midst of debugging some tricky logic error, it can be nice to be able to see all the data at once (not just visually, but quantitatively) and parse it using graphing tools, text editors, or other process. You can record a bagfile of your system in action, then convert that to .csv files per topic, putting them in an easy to interact with form for plotting, parsing, etc. with your standard set of tools like `pandas` or `matplotlib`. 


## Extensions to the Particle Filter

### Make your particle filter more efficient computationally

Advice:
* Find the critical path (what runs the most often and therefore what would give the biggest return on your investment of work).
* The ``OccupancyField`` class has support for processing multiple points simultaneously (vectors of $$(x,y)$$ coordinates).
* Matrix multiplication is your friend (how can a multiplication remove a loop?)
* Benchmark sections of your code by adding timers to see if your efforts are paying off.

### Experiment with laser scan likelihood functions

Advice:
* Look in the Probabilistic Robotics book to see read about ``z_hit``, ``z_random``, etc.

### Robot Kidnapping Problem

Advice:
* Make your code faster first (it will let you use more particles)
* You may need to come up with ways to initialize the particle cloud in smart ways
* Past comprobo projects may provide good clues (look at examples from the [localization assignment](../assignments/robot_localization)). 

### Connection Between the Particle Filter and the Bayes Filter

Advice:
* The core idea is this concept of sequential importance sampling (SIS).  The writeup of this are pretty technical, but you may start with this resource from [Columbia by Frank Wood](http://www.stat.columbia.edu/~fwood/Tutorials/sequential_monte_carlo.pdf). You can also check out section 4.2 of the [Probabilistic Robotics book](https://docs.ufpr.br/~danielsantos/ProbabilisticRobotics.pdf). 
