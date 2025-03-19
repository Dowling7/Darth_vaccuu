---
title: "Broader Impacts Discussion Session 1 // Keypoints and Descriptors"
toc_sticky: true
toc_data:
  - title: Today
    link: in-class/day15/#today
  - title: For Next Time
    link: in-class/day15/#for-next-time
  - title: Broader Impacts Discussion Session 1
    link: in-class/day15/#broader-impacts-sess1
  - title: Keypoints and Descriptors
    link: in-class/day15/#keypoints-and-descriptors
---

## Today

* Session 1 of the Broader Impacts Discussions
* Keypoints, Descriptors, and Keypoint Matching (For Your Consideration)
* Studio Time

## For Next Time
* Work on the [Broader Impacts assignment Part 2](../assignments/broader_impacts), due on **November 5th at 7PM** 
  * Note -- discussions will happen on October 31st and November 4th; you have been [randomly assigned one of these days to lead a discussion](https://docs.google.com/spreadsheets/d/1t2wJVq1ryEH47zOyPqVHE0VHtDHGa2fm6ehskNi13aA/edit?usp=sharing). You may swap slots with someone on a different day, but you have to let an instructor know. Thanks!
* Work on your [Machine Vision Project](../assignments/computer_vision_project).
    * In-class demos will be on **Monday November 11th**, and code/write-ups are due on **Tuesday November 12th at 7PM**.
    * Note that prospective students will be joining us in class on the 11th!
* Consider whether there is [feedback you'd like to share about the class](https://forms.gle/giCwA1pkr4y3e4T37)


## Broader Impacts Discussions
Today, some folks will be leading discussions on their broader impacts robots ([discussion leaders noted here](https://docs.google.com/spreadsheets/d/1t2wJVq1ryEH47zOyPqVHE0VHtDHGa2fm6ehskNi13aA/edit?usp=sharing)). 

> Discussants: Please choose a table / area of the room (or outside of the room!) for your discussion, and let the instructors know if there are any materials you'd like to have available for your discussion. A discussion slot will be ~25 minutes in length total; you will be signalled after 10 minutes (when you should be transitioning from presentation to discussion), and at the 5 minute warning.

> Participants: At the end of the discussion slot, please fill in [this reaction survey](https://forms.gle/4ca9JKVPe3pbwFy1A). Your responses will be available to the teaching team and to discussants afterwards.

We'll have a brief debrief following the activity and before starting in on Studio time.


## Keypoints, Descriptors, and Keypoint Matching
These [slides on keypoints and descriptors](https://docs.google.com/presentation/d/1W5qOiU6j7BKMcFe0sz1O4hAH28Mn_Gop9aNaXafDN2g/edit?usp=sharing) provide a detailed look at this topic. As many projects in the class will likely build on the notion of keypoints/descriptors, we highly recommend using this as a resource to learn more!

To get a brief impression of keypoints, descriptors, and matching, there is some demonstration code available in the [``class_activities_and_resources`` repository](https://github.com/comprobo24/class_activities_and_resources) under the subdirectory ``keypoints_and_descriptors``. Since this directory is not a ROS package, you do *NOT* need to worry about running ``colcon build``. Remember to pull from upstream!

### Keypoint-based Tracking

You can use keypoints to track an object as it moves around in an image.  Go to the ``keypoints_and_desciptors`` directory and run the following command.

```bash
$ ./track_meanshift_keypoints.py
```

You should see an image from your computer's webcam appear on the screen.  Click the image once to pause it, a second time to mark the upper-left corner of the tracking image, and a third and final time to mark the lower-right corner of the tracking image.

At this point you should be able to move the object around and the program will attempt to track its position.

> What do you notice about the keypoints that are selected? What changes when you adjust the "corner threshold" and why? What changes when you adjust the "ratio threshold" and why?

> Look at the code for this example. What types of features are being used? What happens if you change them to one of the other common feature types (e.g., ORB -- check the slides and OpenCV documentation for others!)


### Matching Keypoints
You can use keypoints to match corresponding points in two images.  Go to the ``keypoints_and_desciptors`` directory and run the following command.

```bash
$ ./match_keypoints.py
```
Note that as you move the sliders around, you'll need to click on the image to refresh it.

> What do you notice about the keypoints that are selected? What changes when you adjust the "corner threshold" and why? What changes when you adjust the "ratio threshold" and why?

> Look at the code for this example. What types of features are being used? What happens if you change them to one of the other common feature types (e.g., ORB -- check the slides and OpenCV documentation for others!)


### Visualizing SIFT Descriptors
You can visualize the SIFT descriptors, which we used in the previous two demos. Go to the ``keypoints_and_desciptors`` directory and run the following command.

```
$ ./visualize_sift.py
```

This visualization is showing the SIFT descriptors as described in the slides.  The only thing that it doesn't do is rotate the descriptor relative to the dominant orientation.  Draw in the left pane by clicking and dragging, make sure that you understand why the SIFT descriptor changes the way that it does.  Note, that in order to reset the sketch, you need to hit the spacebar.

> What are the advantages of using SIFT descriptors? When might you not want to use a SIFT descriptor?


### Machine Learning-based Tracking
You may want to try out Magic Leap's model for keypoint identification and tracking.  They [have a repository](https://github.com/magicleap/SuperGluePretrainedNetwork) that is pretty easy to get going with.

> Why might using learned descriptors be attractive? What are challenges associated with using these descriptors?
