---
title: "Broader Impacts Discussion Session 2 // Camera Calibration"
toc_sticky: true
toc_data:
  - title: Today
    link: in-class/day16/#today
  - title: For Next Time
    link: in-class/day16/#for-next-time
  - title: Broader Impacts Discussion Session 2
    link: in-class/day16/#broader-impacts-sess2
  - title: Camera Calibration
    link: in-class/day16/#camera-calib
---

## Today
* Session 2 of the Broader Impacts Discussions
* Camera Calibration (For Your Consideration)
* Studio Time

## For Next Time
* Work on the [Broader Impacts assignment Part 2](../assignments/broader_impacts), due on **November 5th at 7PM** 
  * Note -- the last discussion will happen on November 4th; you have been [randomly assigned one of these days to lead a discussion](https://docs.google.com/spreadsheets/d/1t2wJVq1ryEH47zOyPqVHE0VHtDHGa2fm6ehskNi13aA/edit?usp=sharing). You may swap slots with someone on a different day, but you have to let an instructor know. Thanks!
* Work on your [Machine Vision Project](../assignments/computer_vision_project).
    * In-class demos will be on **Monday November 11th**, and code/write-ups are due on **Tuesday November 12th at 7PM**.
    * Note that prospective students will be joining us in class on the 11th!
* Consider whether there is [feedback you'd like to share about the class](https://forms.gle/giCwA1pkr4y3e4T37)

## Broader Impacts Discussions
Today, some folks will be leading discussions on their broader impacts robots ([discussion leaders noted here](https://docs.google.com/spreadsheets/d/1t2wJVq1ryEH47zOyPqVHE0VHtDHGa2fm6ehskNi13aA/edit?usp=sharing)). 

> Discussants: Please choose a table / area of the room (or outside of the room!) for your discussion, and let the instructors know if there are any materials you'd like to have available for your discussion. A discussion slot will be ~25 minutes in length total; you will be signalled after 10 minutes (when you should be transitioning from presentation to discussion), and at the 5 minute warning.

> Participants: At the end of the discussion slot, please fill in [this reaction survey](https://forms.gle/JVBFzVozqZkGaTgf8). Your responses will be available to the teaching team and to discussants afterwards.

We'll have a brief debrief following the activity and before starting in on Studio time.

## Camera Calibration
One of the _essential_ practical aspects of machine vision is camera calibration: knowing the intrinsic and extrinsic parameters of your imaging system. 

* _Intrinsic Calibration_ refers to the sensor and lens characteristics of your imaging system; calibrating here allows you to correct for image distortions. This is a "projective transformation" between your camera coordinates and your image pixel coordinates.
* _Extrinsic Calibration_ refers to the way in which your imaging system is set up. For instance, if you have two cameras, this would include their relative poses to one another. This is a "rigid transformation" between your world coordinates and your camera coordinates.

### Pinhole Camera Model 
The "pinhole camera model" is among the most commonly used for performing basic camera calibration. These [slides for today](https://docs.google.com/presentation/d/1TA73TpNwUlf8uIJ36ABQTFcNlmwsK0gcNMrf7tZFPwI/edit?usp=sharing) go through the key details. Please use this as a resource!

### Camera Calibration Resources
Here are several different tutorials on how to do (intrinsic) camera calibration in ROS2:

* [Using the Camera Calibration module](https://navigation.ros.org/tutorials/docs/camera_calibration.html)
* [Using the Nav2 module](https://docs.ros.org/en/rolling/p/camera_calibration/tutorial_mono.html)
* [A Medium Post walk-through](https://medium.com/starschema-blog/offline-camera-calibration-in-ros-2-45e81df12555)

You can also checkout the [brief OpenCV demo](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html) if you'd like to just test this out on your webcam.

Note that you'll need checkerboards for this! Some are available in the classroom. If you'd like to print your own, [calib.io pattern generator](https://calib.io/pages/camera-calibration-pattern-generator) is an excellent resource!

### Additional Resources
* An article on <a-no-proxy href="https://www.ri.cmu.edu/pub_files/pub2/willson_reg_1993_1/willson_reg_1993_1.pdf"> What is the Center of an Image? </a-no-proxy> 
* <a-no-proxy href="https://www.youtube.com/watch?v=nOQvjG7Jbao"> Youtube lecture on pinhole camera model </a-no-proxy> (includes a fun demo on finding the focal length of your phone camera at around 7:30)
* MatLab has a nice [high-level explainer](https://www.mathworks.com/help/vision/ug/camera-calibration.html) with follow-on articles worth a look. 

