---
title: "Search and Rescue Algorithms I // Robot State Estimation and Bayes"
toc_sticky: true
toc_data:
  - title: Today
    link: in-class/day08/#today
  - title: For Next Time
    link: in-class/day08/#for-next-time
  - title: Search and Rescue, SLAM Part 1
    link: in-class/day08/#search-and-rescue-slam-part-1
  - title: Bayesian Filtering and the Particle Filter
    link: in-class/day08/#bayesian-filtering-and-the-particle-filter
---

## Today

* Search and Rescue Algorithms I: An Intro to SLAM
* Bayesian Filtering (and the Particle Filter)

## For Next Time

* Complete the [Particle Filter Conceptual Overview](../assignments/robot_localization#conceptual-overview-due-9-22) (submitted individually!), due on **Tuesday October 1st at 1PM**
* [Form a team](https://docs.google.com/spreadsheets/d/1rE78CwfC8EZzauaegFujHMeQZMqxPuFwX2tCbE_3v44/edit?usp=sharing) and work on the [Robot Localization project](../assignments/robot_localization)
  * Demos due on **Thursday October 17th In-Class**
  * Code + Writeups due on **Friday October 18th 7PM**
* Read over the [Broader Impacts assignment Part 2](../assignments/broader_impacts), due on **November 5th at 7PM** 
  * Note -- discussions will happen on October 28th, October 31st, and November 4th; stay tuned!
* Consider whether there is [feedback you'd like to share about the class](https://forms.gle/giCwA1pkr4y3e4T37)


## Search and Rescue Algorithms 1: SLAM
_Simultaneous Localization and Mapping_ or SLAM, is perhaps one of THE most quintessential algorithms in modern robotics today. The premise is simply that we would like the robot to know where it is _even if there is not a reference map_. In search and rescue applications, this is a powerful skill -- since even in urban environments there is potential for the landscape to have changed sufficiently that a known map is worthless. 

But how does a robot know where it is...without knowing where it is?

[Cyrill Stachniss](https://scholar.google.com/citations?user=8vib2lAAAAAJ&hl=en) has a quick 5-minute overview of SLAM worth a watch (FWIW he is also involved in some of the most widely used SLAM algorithms and computational representations in robotics used today): [Explainer](https://youtu.be/BuRCJ2fegcc).

As outlined in the video, there are two implemented pieces to a SLAM algorithm -- a front-end (takes the data and turns it into some useful representation), and a back-end (which tries to compute the location of the robot within a map).

The three different backend approaches mentioned -- EKF, Particle, and Graph-based SLAM -- are not only different implementations/techniques, but also represent both _online_ and _offline_ techniques. Online techniques are computed in practical time while a robot is underway. Offline techniques are generally much slower to compute; maybe even computed after a robot has run a mission. All of these methods can be used online (in some fashion), but it's worth noting that Graph-Based approaches are also often run _offline_.

Let's take a look at the conceptual difference between:
* an [EKF-based online approach](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=4fcf1d9c8c0f86ba318738c6531bbdcfb094f85b) (take a look at page 10)
  * watch a simple demo [here](https://www.youtube.com/watch?v=vGXQ537gHCg)
* a [graph-based offline approach](http://ais.informatik.uni-freiburg.de/teaching/ss13/robotics/slides/16-graph-slam.pdf) (slides 1-10 give a reasonable gist)
  * watch a simple demo [here](https://www.youtube.com/watch?v=E6IvbjZA7Ao) (note when the map "squiggles")

> For way more math, have a look at this [Graph-Based SLAM tutorial paper](http://www2.informatik.uni-freiburg.de/~stachnis/pdf/grisetti10titsmag.pdf).


Some questions to consider:
* What may be some limitations to each of these SLAM algorithms?
  * When might an offline algorithm be appropriate? When not? 
  * When might an online algorithm be appropriate? When not?
* In what scenarios or environments do you think any SLAM algorithm will have a hard time navigating in?
* Which steps in the pseudocode do you want to learn more about?
* What might a SAR designer want to consider when selecting a SLAM algorithm to use? 


## Bayesian Filtering and the Particle Filter

> Legacy notes about Bayes Filters and the Particle Filter from Paul Ruvolo are available: [as a video lecture](https://www.youtube.com/embed/l7CrjOTlioU) and as [physical notes](updated_bayes_filter.pdf). 

For your projects, you're implementing a particle filter, which is a subclass of algorithm under the more general category of _Bayesian filters_. A Bayesian filter is a recursive, or sequential, algorithm -- for localization, this means that the robot's state estimate is refined iteratively as observations or actions are taken.

There is a bit of vocabulary to know before we get started:
* Markov process: a chain of events in which the probability of each event depends only on the state of the previous event ("what happens next only requires me to think about what's happening now")
  * This is a useful _assumption_ about the way the world works, because now we don't have to consider the entire history of a robot, just what happened most recently.
* Monte Carlo algorithms: repeated random sampling is used to estimate a solution to a complex (often nonlinear) problem

We're going to walk through the steps of the Bayesian filter:
```
Steps of a Bayesian Filter:
1) Initialize with an estimate of the first pose
2) Take an action, and predict the new pose based on the motion model
3) Correct the pose estimate, given an observation
4) Repeat steps 2 and 3, ad nauseum (or until your robot mission is over)
```

### Prediction
During the prediction step, the current estimated pose of the robot is updated based on a _motion model_. The motion model captures how a control input may be mapped to the real world (what noise may be applied, for instance). Prediction will always increase the uncertainty we have about where the robot is in the world (unless we have perfect motion knowledge). Prediction asks: given where I think I am, where will I end up after I take this action?

### Correction
To reduce (or attempt to reduce) our uncertainty, we can look around us with an _observation model_ (which will also capture noise in our measurements). Correction asks: given what I am measuring, what is my likely pose based on my estimate of where I may be?

### Mathematical Details
We'll walk through the mathematical details of this for a simple world in which a robot can open and close a door, and can measure whether a door is open or closed. This example is borrowed from [Probabilistic Robotics](https://docs.ufpr.br/~danielsantos/ProbabilisticRobotics.pdf); a highly influential book in modern robotics.

### The Particle Filter
A Bayesian filter, in its purest form, asks us to work with continuous probability distributions, and that is computationally challenging (nigh intractable) most of the time for practical robotics problems. The particle filter addresses these computational challenges by allowing us to _draw samples from our probability distributions_ and apply our prediction and correction steps to each of those samples in order to get an empirical estimate of a new probability distribution. In this way, the particle filter is a Monte Carlo algorithm, and leverages the law of large numbers to "converge" towards the optimal answer. (You can get a sense about why sampling works to find complex distributions by [playing with this applet](http://chi-feng.github.io/mcmc-demo/app.html?algorithm=GibbsSampling&target=banana)).


