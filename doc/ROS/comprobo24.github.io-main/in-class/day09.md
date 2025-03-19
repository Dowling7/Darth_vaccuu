---
title: "Intended Use // Computing Relative Motion"
toc_sticky: true
toc_data:
  - title: Today
    link: in-class/day09/#today
  - title: For Next Time
    link: in-class/day09/#for-next-time
  - title: Intended Use
    link: in-class/day09/#intended-use
  - title: Bayes Filter (Continued)
    link: in-class/day09/#bayes-filter-continued
  - title: Particle Filter and Computing Relative Motion
    link: in-class/day09/#particle-filter-and-computing-relative-motion
---

## Today
* Intended Use (For Your Consideration)
* Bayes Filter (Continued)
* Particle Filter and Computing Relative Motion
* Studio Time

## For Next Time
* [Form a team](https://docs.google.com/spreadsheets/d/1rE78CwfC8EZzauaegFujHMeQZMqxPuFwX2tCbE_3v44/edit?usp=sharing) and work on the [Robot Localization project](../assignments/robot_localization)
  * Demos due on **Thursday October 17th In-Class**
  * Code + Writeups due on **Friday October 18th 7PM**
* Read over the [Broader Impacts assignment Part 2](../assignments/broader_impacts), due on **November 5th at 7PM** 
  * Note -- discussions will happen on October 28th, October 31st, and November 4th; stay tuned!
* Consider whether there is [feedback you'd like to share about the class](https://forms.gle/giCwA1pkr4y3e4T37)
* If you might be interested in a recitation for CompRobo, we're [finding a time here](https://www.when2meet.com/?26799639-kquOs).
* **Extra Credit** An assignment to [reinforce probability fundamentals](../assignments/probability_basics/assignmentprobability_basics.pdf) is available to complete for extra credit (to be applied to the state estimation and localization unit). Due on **Friday October 18th 7PM** for those interested; [check the Canvas page for submission instructions](https://canvas.olin.edu/courses/822/assignments/13050).

## Intended Use (For Your Consideration)
As we've been discussing, the landscape of Search and Rescue robots is quite broad -- from clearly bespoke solutions to specific scenarios/teams, to general purpose robots. The latter cases are particularly interesting -- what makes a search and rescue robot...a search and rescue robot, if not its form/functionality?

There are multiple ways in which a technology is operationalized for a particular use case:
* By fundamental design (e.g., the form or functionality is entirely niche)
* By licensing or IP controls (e.g., commercial, non-commercial, open-source, closed-source)
* By market controls (e.g., only selling to certain buyers, lease/renting/buying models)
* By partnership (e.g., robots are provided only to trusted partners, potentially with a point-of-contact or dedicated engineer to monitor use)
* Maybe others! (if you can think of some, let us know and we can add them here)

As we implement our particle filters, and kick-off our machine vision unit in a few weeks, I invite you all to reflect on intended use, in particular:
* What license will you be using on GitHub for your projects; why?
* Can algorithms be designed to restrict their utility to certain applications; why or why not?
* In what way is an engineer responsible for considering _unintended use_ of their system? What actions should they take (or not)?
* Assuming that an algorithm is free to use, what evidence should be provided that it works as expected? How should limitations of the algorithm be communicated?

As part of the submission for the Machine Vision project, we'll be thinking about this in more detail. For now, this is food for thought!

## Bayes Filter (Continued) and Particle Filter Applications
Last time, we were looking at Bayes filters -- a class of algorithms (of which our particle filter is one!) that allows us to propagate our uncertainty about the world in time, and constrain it by using our observations. We're going to finish our discussion, and specifically think about how we actually deploy Bayesian Filter of any flavor on a real robot, and what it's implications are.

> Slides walking through our in-class derivation [here](https://docs.google.com/presentation/d/1ekeHfD7YOJLc6mHo8z4BHfnu2JCXtsvNfszsGDPM4Js/edit#slide=id.p), and a previous recording of the walkthrough by Paul Ruvolo can be watched [here](https://www.youtube.com/embed/l7CrjOTlioU).

Questions for consideration:
* What are the computational limitations of a Bayes Filter? How does particle filtering overcome those limitations?
* What are possible limitations of a particle filter? How might you overcome those limitations?
* How are you going to represent your motion model for the project?
* How are you going to represent your sensor model for the project?


## Particle Filter and Computing Relative Motion 
One part of your particle filter will involve [estimating the relative motion of your robot between two points in time as given by the robot's odometry](https://github.com/comprobo24/robot_localization/blob/main/robot_localization/pf.py). 

Suppose you are given the robot's pose at time $$t_1$$, and then again a measure at $$t_2$$. What are some ways that you might compute the robot's change in pose between these times? What coordinate system(s) do you want to work in? Work with the folks around you to discuss your ideas; discussing your conceptual overviews might be particularly helpful here!

> Note: Our [coordinate transforms activity](https://comprobo24.github.io/in-class/day05#coordinate-frames-and-coordinate-transforms-in-robotics) from a few classes ago might be inspirational for finding an approach here.

> Note: while probably not needed for dealing with 2D rotation and translation, the ``PyKDL`` library can be useful for converting between various representations of orientation and transformations (e.g., see [this section of the starter code](https://github.com/comprobo24/robot_localization/blob/main/robot_localization/helper_functions.py#L95)). This is also a helpful reminder -- there is skeleton and helper code you may want to be getting familiar with for your project...

### One Approach: Homogenous Transformation Matrices
One way to think about the relationship between poses $$t_1$$ and $$t_2$$ is through simple translation and rotation. Here is a [walkthrough of that technique](https://docs.google.com/presentation/d/1VMTZQf_sgIdbWxB_owbgZ7GP6-WaUCh7tuRjvRU42tM/edit?usp=sharing) as well as a video version from Paul:

> Note: a mistake is made in this video when writing the origin offset (at 8:37 into the video). This doesn't change the substance, but watcher beware!

<iframe width="560" height="315" src="https://www.youtube.com/embed/x7mRC0Gowe8?si=movGSLBJvod5ad06" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
