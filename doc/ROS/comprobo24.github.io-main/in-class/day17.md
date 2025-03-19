---
title: "Broader Impacts Discussion Session 3 // Image Segmentation"
toc_sticky: true
toc_data:
  - title: Today
    link: in-class/day17/#today
  - title: For Next Time
    link: in-class/day17/#for-next-time
  - title: Broader Impacts Discussion Session 3
    link: in-class/day17/#broader-impacts-sess3
  - title: Image Segmentation Basics
    link: in-class/day17/#sfm-basics
---
## Today

* Session 3 of the Broader Impacts Discussions
* Image Segmentation Basics (For Your Consideration)
* Studio Time

## For Next Time
* Turn in your materials from the [Broader Impacts assignment Part 2](../assignments/broader_impacts), due on **November 5th at 7PM** 
* Work on your [Machine Vision Project](../assignments/computer_vision_project).
    * In-class demos will be on **Monday November 11th**, and code/write-ups are due on **Tuesday November 12th at 7PM**.
    * Note that prospective students will be joining us in class on the 11th!
* Consider whether there is [feedback you'd like to share about the class](https://forms.gle/giCwA1pkr4y3e4T37)

## Broader Impacts Discussions
Today, some folks will be leading discussions on their broader impacts robots ([discussion leaders noted here](https://docs.google.com/spreadsheets/d/1t2wJVq1ryEH47zOyPqVHE0VHtDHGa2fm6ehskNi13aA/edit?usp=sharing)). 

> Discussants: Please choose a table / area of the room (or outside of the room!) for your discussion, and let the instructors know if there are any materials you'd like to have available for your discussion. A discussion slot will be ~25 minutes in length total; you will be signalled after 10 minutes (when you should be transitioning from presentation to discussion), and at the 5 minute warning.

> Participants: At the end of the discussion slot, please fill in [this reaction survey](https://forms.gle/8iwFzQXmtbPA8cCWA). Your responses will be available to the teaching team and to discussants afterwards.

We'll have a brief debrief following the activity and before starting in on Studio time.

## Image Segmentation Basics
During this unit we've been discussing classical methods for parsing images and extracting keypoints, creating descriptors, and performing the correspondence task. For your consideration today, here is a brief set of materials which cover the concept of _image segmentation_, which encompasses a variety of techniques with the goal of subdividing an image into regions.

Image segmentation techniques are commonly separated into three groups:
* **Instance Segmentation**: each pixel is assigned a "belonging instance" (e.g., every pedestrian in an image is separately sorted)
* **Semantic Segmentation**: each pixel is assigned a "belonging class" (e.g., a landscape is divided into sand, rock, tree, grass, sky, cloud, etc.)
* **Panoptic Segmentation**: each pixel is assigned a "belonging class" and individual instances of a class are further identified.

Each technique yields a slightly different output, which is important to consider when thinking about what downstream work you would like to do. For instance, in an object tracking scenario, being able to distinguish different types of objects, and identify a specific instance, may be important. Alternatively, in simple mapping, it may be enough to know the mixture of classes of objects in an environment.

Like everything in machine vision, there are classical and learned techniques that can be adopted to perform image segmentation.

### Classical Techniques
These classical techniques for image segmentation will likely look familiar to you -- they often leverage the same processes that we've been using to identify keypoints!

**Thresholding and Clustering** Using simple thresholding values on an image, we can isolate regions that "look similar" and assign them to various classes (by simply keeping track of what pixels meet certain criteria). Histogram methods are a variation on this technique. Enhancing this idea, we can process an image using a clustering algorithm, for instance, [K-Means Clustering](https://www.ibm.com/topics/k-means-clustering), to assign pixels to classes.

**Edge and Contour Detection** You can sort edges in an image (detected using gradient based methods that we might apply when looking for keypoints...) in order to assist with image segmentation. Hough transforms (for lines and for circles) look at edges and use a set of criteria to determine whether a set of edges are geometric matches to a target geometry. 

**Getting Advanced** Methods like variational partitioning, topic modeling, Markov random fields, and parameteric partial-differential equations, have all been adopted for processing images and extracting regions of interest. [The Wikipedia page](https://en.wikipedia.org/wiki/Image_segmentation) on Image Segmentation gives a nice overview of each of these in turn.


Some code tutorials or documentation you might find interesting here:
* OpenCV's Python [Tutorial on the Watershed Algorithm](https://docs.opencv.org/4.x/d3/db4/tutorial_py_watershed.html)
* OpenCV's Python [Tutorial on the GrabCut Method](https://docs.opencv.org/4.x/d8/d83/tutorial_py_grabcut.html)
* A Kaggle Walkthrough of [Image Segmentation with OpenCV](https://www.kaggle.com/code/mielek/image-segmentation-with-opencv)
* A tutorial on 4 methods of [Image Segmentation with OpenCV](https://machinelearningknowledge.ai/image-segmentation-in-python-opencv/)
* [K-Means Clustering in SKLearn](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.KMeans.html)
* [Hough Line Transform in OpenCV](https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html)
* [Hough Circle Transform in OpenCV](https://docs.opencv.org/3.4/d4/d70/tutorial_hough_circle.html)


### Learning / AI Techniques
Often, we want to segment an image, it is because there are particular "things" we're hoping to find. Learning-based techniques have really opened the door for advanced image segmentation that allows us to select for certain objects that may be challenging to heuristically select for using classical techniques (for instance, pedestrians in a busy street scene, objects in a cluttered kitchen, or specific types of animals in an environment we're monitoring).

[MathWorks has a nice explainer](https://www.mathworks.com/solutions/image-video-processing/semantic-segmentation.html) on semantic segmentation that is absolutely worth a read, including how you can use their toolboxes to performed learned segmentation.

Learned segmentation models often make use of _convolutional neural networks_ (CNNs). If you'd like to learn more about specific architectures, [Papers with Code](https://paperswithcode.com/task/semantic-segmentation) is an excellent resource for papers + repositories + datasets you can run. 