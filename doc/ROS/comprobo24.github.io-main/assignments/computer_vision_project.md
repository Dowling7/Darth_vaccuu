---

title: "Machine Vision Project"
toc_sticky: true
toc_h_max: 3
---

## Abstract

So far, you have successfully programmed robots using reactive control strategies and taken a deep dive into the robot localization problem. Next, you will be learning about machine vision and the role it plays in robotics. In contrast to previous project, this time you will have a great deal of freedom to shape your project towards your interests and learning goals.

## Learning Objectives
* Self-directed learning of a new robotics algorithm.
* Implementing a robotics system with minimal scaffolding.

## Teaming
For this project, you can work with one other student.  If you want to have a team of three, please talk to the instructors beforehand.

Please fill out <a href="https://docs.google.com/spreadsheets/d/1VirFJv8flcuBjE8HbtSx7HuS2RMWvL_LzAVdEjaajYA/edit?usp=sharing">this Google Sheet</a> when you have a project team and Github repo.


## Project Topic
Your project should be about machine vision and its intersection with robotics.  You will carry out that project either using a robot simulator, a computer vision dataset, the Neato, or some combination.

In your project proposal you will be coming up with an implementation plan.  That is, if you are using a particular algorithm to solve a problem, which parts of the algorithm will you implement, and which will you use pre-built implementations for?  Be strategic in these decisions to balance learning about algorithms with system building (e.g., programming the simulated Neatos (or another robot) to do something interesting).  You have substantial latitude in shaping your project to focus on the parts you really want to learn (e.g., system design versus basic understanding of algorithms). That said, we expect that you will do some exploration of algorithms as part of this project (which could include implementation or perhaps substantial learning about an algorithm or class of algorithms).

### Potential Algorithm Topics
* Object tracking or detection
* Image de-noising or correction; in-painting
* Image segmentation; semantic labeling
* Text recognition
* Gesture recognition
* Fiducial tracking and navigation
* Visual odometry or SLAM
* Structure from motion
* Neural rendering (radiance fields; Gaussian splats)
* Vision-Lidar or Vision-Inertial sensor fusion

(Note: there are some resources for these topics later in the document)

## Robot Platform and Data Pipelines

* One option is to continue to work with the Neato. In class, you'll see the Neato camera setup and go through a simple demo of how to use the images to control a robot.
* You may want to use an external dataset for your project. Here are some possible starting points. 
    * <a-no-proxy href="https://www.visualdata.io/discovery">Visual Data</a-no-proxy> and [Papers with Code](https://paperswithcode.com/datasets?mod=images) has a nice collection of computer vision datasets and projects.
    * If you want a huge (but very cool) dataset for self-driving vehicles, consider using Waymo's <a-no-proxy href="https://waymo.com/open/">Open Dataset</a-no-proxy>
    * If you're interested in machine learning for robot control, you might consider building off some of <a-no-proxy href="https://github.com/comprobo18/robot_learning/network/members">the datasets (and code) from the 2018 Robot Learning project</a-no-proxy> You also might want to check out <a-no-proxy href="https://docs.google.com/presentation/d/1ZZBZotRITt42OIpwC-jiFYWu-h27rZ1PzhctPyRYgng/edit">the Google Slides presentation summarizing their results</a-no-proxy>.
    * Pick any open dataset of imagery in a domain of interest to you (e.g., for ocean biology [FathomNet](https://fathomnet.org/fathomnet/#/) is a nice option; for city landscapes [Cityscapes](https://paperswithcode.com/dataset/cityscapes) could be good; for food check out [Food-101](https://paperswithcode.com/dataset/food-101)...and so on!)
    * A lot these datasets are big and fancy, but don't be afraid to start with smaller, more classic datasets. That's a great way to learn without having to deal with the greater complexity that comes with some of this data.

## Deliverables

There are four deliverables for this project.

### Project Proposal (due 10/22)

At a minimum, please include the answers to the following questions. You should include enough detail for us to be able to give you useful feedback. [Submit your proposal on canvas](https://canvas.olin.edu/courses/822/assignments/13674).

* Who is on your team?
* What is the main idea of your project?
* What are your learning goals for this project?
* What algorithms or computer vision areas will you be exploring?
* What components of the algorithm will you implement yourself, which will you use built-in code for?  Why?
* What is your MVP?
* What is a stretch goal?
* What do you view as the biggest risks to you being successful (where success means achieving your learning goals) on this project?
* What might you need from the teaching team for you to be successful on this project?

### In-class Presentation / Demo (11/11)

We'd like each team to spend about 10 minutes presenting what they did for this project. You can structure the presentation in whatever manner you'd like, however, you should try to meet these goals:

* Explain the goal of your project
* At a high-level explain how your system works
* Demonstrate your system in action (either in a video [recommended] or live). If your system doesn't work completely yet, that is fine, try to show at least one component of your system in action.
* This presentation / demo should be very informal. This presentation will be assessed in a purely binary fashion (basically did you do the things above).

Please [submit your presentation on canvas](https://canvas.olin.edu/courses/822/assignments/13675).

### Code (Due 11/12)

* You should turn in your code and writeup via Github. [Submit a link on canvas when you're all set](https://canvas.olin.edu/courses/822/assignments/13676)!

### Writeup (Due 11/12)

In your ROS package create a ``README.md`` file to hold your project writeup.  Your writeup should touch on the following topics. We expect this writeup to be done in such a way that you are proud to include it as part of your professional portfolio. As such, please make sure to write the report so that it is understandable to an external audience.  Make sure to add pictures to your report, links to Youtube videos, embedded animated Gifs (these can be recorded with the tool ``peek``).

* What was the goal of your project?  Since everyone is doing a different project, you will have to spend some time setting this context.
* How did you solve the problem (i.e., what methods / algorithms did you use and how do they work)?  As above, since not everyone will be familiar with the algorithms you have chosen, you will need to spend some time explaining what you did and how everything works.
* Describe a design decision you had to make when working on your project and what you ultimately did (and why)? These design decisions could be particular choices for how you implemented some part of an algorithm or perhaps a decision regarding which of two external packages to use in your project.
* What if any challenges did you face along the way?
* What would you do to improve your project if you had more time?
* Did you learn any interesting lessons for future robotic programming projects? These could relate to working on robotics projects in teams, working on more open-ended (and longer term) problems, or any other relevant topic.


## Resources and Potential Project Directions

### Resources

Some picks (good starting points for machine learning flavored computer vision projects):
  - [UZH FPV Drone Racing Dataset](https://fpv.ifi.uzh.ch/datasets/):  Get OpenVins or GTSAM running to do some pose estimation.  Try to implement or compute the optical flow between image frames.
  - [KITTI Autonomous Car Dataset](https://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark).  Implement or use YOLO or other CNN to do 2D object detection for AV environment (e.g., [this tutorial](https://github.com/windowsub0406/KITTI_Tutorial)). Some form of 360 video to BEV model similar to [this tutorial](https://jamycheung.github.io/360BEV.html).
  - Some Foundation Model (e.g., [Segment Anything](https://github.com/facebookresearch/segment-anything)).  Try to run and use the SAM model for some structured navigation task with the neatos (e.g., detect stop signs...)
  - Try to run [VINT](https://visualnav-transformer.github.io/) on the Neato


In-Class Activities from Past CompRobo Offerings and Other Tutorials
* <a-no-proxy href="https://drive.google.com/file/d/0B0UHkPLHsgyoZnBSZ0FiSjZGRDA/view?usp=sharing">Object Tracking</a-no-proxy>
* <a-no-proxy href="https://drive.google.com/file/d/0B0UHkPLHsgyoTTBHLWl1c3FqRnM/view?usp=sharing">3D Structure from Motion</a-no-proxy>
* <a-no-proxy href="https://drive.google.com/file/d/0B0UHkPLHsgyocndyTDI2U2I1M1k/view?usp=sharing">Image Filtering</a-no-proxy>
* <a-no-proxy href="https://sites.google.com/site/comprobofall14/home/labs/day-18?authuser=0">Object Recognition</a-no-proxy> (the instructions on running the code are out of date, but the ideas might help).
* <a-no-proxy href="http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython">Convert ROS image messages to OpenCV using CvBridge</a-no-proxy>
* <a-no-proxy href="https://vision.in.tum.de/teaching/ss2013/visnav2013">Visual Navigation for Flying Robots</a-no-proxy> is a course on said topic.  The linked page includes lectures and even some bag files.
* <a-no-proxy href="https://automaticaddison.com/working-with-ros-and-opencv-in-ros-noetic/">Connecting a webcam to ROS and OpenCV</a-no-proxy>
* <a-no-proxy href="https://www.crcv.ucf.edu/papers/Object%20Tracking.pdf">An overview of methods for object tracking</a-no-proxy>
* <a-no-proxy href="https://docs.google.com/presentation/d/1ZZBZotRITt42OIpwC-jiFYWu-h27rZ1PzhctPyRYgng/edit?usp=sharing">Slides from the CompRobo Learning Project 2018 Class Report Out</a-no-proxy>
* <a-no-proxy href="https://www.cs.ccu.edu.tw/~damon/photo/,OpenCV/,Mastering_OpenCV.pdf">Mastering OpenCV with Practical Computer Vision Projects</a-no-proxy>
* Visual odometry resources (<a-no-proxy href="http://www.cvlibs.net/software/libviso/">one example</a-no-proxy>)
* <a-no-proxy href="https://docs.opencv.org/master/da/d22/tutorial_py_canny.html">Canny edge detection</a-no-proxy>
* <a-no-proxy href="https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html">Template matching</a-no-proxy>
* <a-no-proxy href="https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html">Hough line transform</a-no-proxy>
* <a-no-proxy href="https://docs.opencv.org/master/d1/db7/tutorial_py_histogram_begins.html">Basics of histograms</a-no-proxy> and <a-no-proxy href="https://docs.opencv.org/3.4/d4/d1b/tutorial_histogram_equalization.html">histogram equalization</a-no-proxy>
* <a-no-proxy href="https://scipy.github.io/old-wiki/pages/Tentative_NumPy_Tutorial">Basic Numpy tutorials</a-no-proxy>
* <a-no-proxy href="https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_table_of_contents_gui/py_table_of_contents_gui.html">GUI Features in OpenCV</a-no-proxy>
* <a-no-proxy href="https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#basic-ops">Basic Operations on Images</a-no-proxy>
* <a-no-proxy href="https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html#image-arithmetics">Arithmetic Operations on Images</a-no-proxy>
* <a-no-proxy href="https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html">Corner Detection</a-no-proxy>
* <a-no-proxy href="https://scipy.github.io/old-wiki/pages/Numpy_Example_List.html">Numpy Examples List</a-no-proxy>

### Past projects to draw from

* Machine Vision Projects from Fall 2022
   * [Plant Vision](https://github.com/jonaskaz/plant-vision)
   * [Visual Odometry](https://github.com/jackiezeng01/comprobo-computervisionproject)
   * [Robot Soccer](https://github.com/hnvakil/soccer_computer_vision)
   * [Self-guided Robot Nerf Turret Shooter](https://github.com/gabbyblake/computer_vision)
   * [Controlling a Drone](https://github.com/TigeyJewellAlibhai/uav-control/tree/main)
   * [Visual Odometry](https://github.com/jerWenger/Visual_Based_Odometry)
   * [Neato Fetch](https://github.com/ayushchakra/neato-fetch)
   * [Neato Following Another Neato](https://github.com/SeunguLyu/NeatoFollowingNeato)
   * [Fiducial Tracking 1](https://github.com/kviiim/fiducial_tracking)
   * [Fiducial Tracking 2](https://github.com/MetaKor/comprobo_fiducial)
   * [Stereo Vision](https://github.com/krish-suresh/comprobo_cv_project)
   * [Hand Gesture Recognition](https://github.com/AlexisWu-01/compRobo22_computer_vision)
 
* <a-no-proxy href="https://docs.google.com/presentation/d/1ZZBZotRITt42OIpwC-jiFYWu-h27rZ1PzhctPyRYgng/edit">Robot Learning Report out 2018</a-no-proxy>

* Computer Vision Project Writeups from 2017
   * <a-no-proxy href="https://github.com/arpanrau/self_driving_neato/blob/master/WriteUp.md">Self Driving Neato</a-no-proxy>
   * <a-no-proxy href="https://github.com/BrennaManning/computer_vision_2017/blob/master/writeup.pdf">Computer Vision Emotion Detection</a-no-proxy>
   * <a-no-proxy href="https://github.com/HALtheWise/comprobo-fast-localizer/blob/master/final_report.pdf">Visual Localization</a-no-proxy>
   * <a-no-proxy href="https://github.com/shanek21/cv_motion_prediction">Predicting Paths of Tracked Objects</a-no-proxy>
   * <a-no-proxy href="https://github.com/krusellp/neato_keeper/blob/master/Neato_Keeper.pdf">Neato Keeper</a-no-proxy>
   * <a-no-proxy href="https://github.com/kzhang8850/lane_follower">Lane Follower</a-no-proxy>
   * <a-no-proxy href="https://github.com/CompRoboMealVision/meal_recognition">Meal Recognition</a-no-proxy>
   * <a-no-proxy href="https://github.com/jsutker/computer_vision_2017/blob/master/pacneato/scripts/Pacneato_Writeup.md">Pac Neato</a-no-proxy>
   * <a-no-proxy href="https://github.com/jovanduy/computer_vision_2017">Neato Augmented Reality Parking</a-no-proxy>
