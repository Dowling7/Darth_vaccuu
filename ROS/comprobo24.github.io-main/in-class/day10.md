---
title: "Search And Rescue Algorithms II // Computing Motion and Likelihoods"
toc_sticky: true
toc_data:
  - title: Today
    link: in-class/day10/#today
  - title: For Next Time
    link: in-class/day10/#for-next-time
  - title: Search And Rescue Algorithms II
    link: in-class/day10/#search-and-rescue-algorithms-ii
  - title: Computing Motion
    link: in-class/day10/#computing-motion
  - title: Likelihood Models
    link: in-class/day10/#likelihood-models
  - title: Possible Extensions
    link: in-class/day10/#possible-extensions
---

## Today
* Search and Rescue Algorithms II (For your consideration)
* Studio Time and Breakout Sessions -- 
  * Computing Relative Motion
  * Likelihood Models
* Possible Project Extensions (For your consideration)
 
## For Next Time
* Work on the [Robot Localization project](../assignments/robot_localization)
  * Demos due on **Thursday October 17th In-Class**
  * Code + Writeups due on **Friday October 18th 7PM**
* Read over the [Broader Impacts assignment Part 2](../assignments/broader_impacts), due on **November 5th at 7PM** 
  * Note -- discussions will happen on October 28th, October 31st, and November 4th; stay tuned!
* Consider whether there is [feedback you'd like to share about the class](https://forms.gle/giCwA1pkr4y3e4T37)
* **Extra Credit** An assignment to [reinforce probability fundamentals](../assignments/probability_basics/assignmentprobability_basics.pdf) is available to complete for extra credit (to be applied to the state estimation and localization unit). Due on **Friday October 18th 7PM** for those interested; [check the Canvas page for submission instructions](https://canvas.olin.edu/courses/822/assignments/13050).


## Search And Rescue Algorithms II: EKF SLAM (For your consideration)
Last time we briefly talked about two flavors of SLAM algorithms, Kalman Filtering (or EKF) based, and Graph Based. Today, here is a bit more detail about EKF-based SLAM algorithms, for your consideration. Resources you may find useful include [this presentation by Cyrill Stachniss](http://ais.informatik.uni-freiburg.de/teaching/ws12/mapping/pdf/slam04-ekf-slam.pdf), and Chapter 10 of [Probabilistic Robotics](https://docs.ufpr.br/~danielsantos/ProbabilisticRobotics.pdf).

EKF SLAM is one of the earliest versions of a SLAM algorithm, used to solve the online SLAM problem. It requires:
* Feature-based maps (the terminology typically used is _landmarks_)
* That Gaussian noise is a reasonable assumption for motor and sensor uncertainty

### Goal of EKF SLAM
We've been focused on _localization_, which asks: where is my robot, given that I have a map? We've been representing this as a probability distribution:

$$bel(x_t) = \mathbb{P}(x_t|u_{1:t},z_{1:t})$$

where $$x_t$$ is my pose at some time $$t$$, and $$u$$ and $$z$$ are my robot actions and observations, respectively. Implicitly, we also have access to a map in this formulation. In SLAM, we have to consider that our _map is also unknown_ and so we want to solve a joint probability:

$$bel(x_t, \mathcal{M}) = \mathbb{P}(x_t,\mathcal{M}|u_{1:t},z_{1:t})$$

The map in our EKF world is a list of landmarks which are represented as poses in the world, each with uncertainty associated with them. Extended Kalman Filtering (EKF) allows us to track the uncertainty in our robot pose as well as each of our landmark poses; using a prediction and update step as established by a Bayesian filter. 

### Implementing EKF SLAM -- an interactive Python Notebook
Here is a [CoLab Notebook](https://colab.research.google.com/drive/1Sbm81zccVfqPNaV6w9rdGH56F1uCTUIF?usp=sharing) with a minimal EKF SLAM solution implemented for your review. (You will likely want to download this notebook and run it directly on your system, or from your particular CoLab account). Some key things to pay attention to as you review the code:
* What are the steps of the EKF SLAM algorithm? How do those compare to your Particle Filter? What's different?
* How does changing the noise parameters at the top impact how EKF-SLAM tracks the vehicle? The landmarks?

### Limitations and Design Considerations
* Absence of landmarks is not information that can be incorporated
* It's a linearization-based approach (but we live in a non-linear world)
* It has scaling challenges associated with the number of landmarks / size of a map
* Landmark detection and data association are _critical_ in EKF SLAM; ambiguous landmarks make this challenging
* What else?

### Connecting Back to Search and Rescue
* In what settings do you think that EKF SLAM may be an appropriate SLAM solution? In what settings would it be unsuitable?
* What risks may be associated with applying EKF SLAM to a search and rescue scenario? How might those risks be mitigated?
* What are key advantages to EKF SLAM?

## Breakout Sessions

### Particle Filter and Computing Relative Motion 
One part of your particle filter will involve [estimating the relative motion of your robot between two points in time as given by the robot's odometry](https://github.com/comprobo24/robot_localization/blob/main/robot_localization/pf.py). 

Suppose you are given the robot's pose at time $$t_1$$, and then again a measure at $$t_2$$. What are some ways that you might compute the robot's change in pose between these times? What coordinate system(s) do you want to work in? Work with the folks around you to discuss your ideas; discussing your conceptual overviews might be particularly helpful here!

> Note: Our [coordinate transforms activity](https://comprobo24.github.io/in-class/day05#coordinate-frames-and-coordinate-transforms-in-robotics) from a few classes ago might be inspirational for finding an approach here.

> Note: while probably not needed for dealing with 2D rotation and translation, the ``PyKDL`` library can be useful for converting between various representations of orientation and transformations (e.g., see [this section of the starter code](https://github.com/comprobo24/robot_localization/blob/main/robot_localization/helper_functions.py#L95)). This is also a helpful reminder -- there is skeleton and helper code you may want to be getting familiar with for your project...

#### One Approach: Homogenous Transformation Matrices
One way to think about the relationship between poses $$t_1$$ and $$t_2$$ is through simple translation and rotation. Here is a [walkthrough of that technique](https://docs.google.com/presentation/d/1VMTZQf_sgIdbWxB_owbgZ7GP6-WaUCh7tuRjvRU42tM/edit?usp=sharing) as well as a video version from Paul:

> Note: a mistake is made in this video when writing the origin offset (at 8:37 into the video). This doesn't change the substance, but watcher beware!

<iframe width="560" height="315" src="https://www.youtube.com/embed/x7mRC0Gowe8?si=movGSLBJvod5ad06" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


### Particle Filter and Likelihood Functions

One of the key steps of your particle filter is to compute the weight of each particle _based on how likely the sensor reading from the particle is, given the map_. There are tons of possible ways to compute this weight, but we recommend using a **likelihood field function**. Computing a likelihood field relies on the following steps:

1. Cast the sensor measurement into the world coordinate frame _relative to each particle's frame of reference_. 
2. Determine the closest obstacle in the map based on your sensor measurement location.
3. Compute the distance between your sensor reading and the closest obstacle.
4. Assign the likelihood of your sensor reading as the probability of your distance measurement + small stochastic noise.

The secret sauce here is in your closest obstacle identification, distance measurement probability, and your stochastic noise...let's consider the following:

### ``update_particles_with_laser``
The first step is to determine how the endpoints of the laser scan would fall within the map *if the robot were at the point specified by a particular particle*.  You can do this by drawing some pictures and pulling out your trigonometry skills!

Next, you will take this point and compare it to the map using the provided ``get_closest_obstacle`` function (hint: you may want to be getting familiar with [this code](https://github.com/comprobo24/robot_localization/blob/main/robot_localization/occupancy_field.py)). Once you have this value, you will need to compute some sort of number that indicates the confidence associated with it.  Finally, you will have to combine multiple confidence values into a single particle weight.

### Distance Confidence and Gaussian Distributions
A Gaussian (or normal) distribution is an incredibly useful probabilistic representation used widely in robotics; the reasons are:
* It has a closed-form solution for sampling
* It has a closed-form solution for assigning probability to a sample

 We're interested in using a Gaussian to allow us to represent our confidence in the _distance measurement_ we compute in the previous step. We'll draw out a picture to see how this manifests in our Neato world.

 Setting the _variance_ term in our Gaussian distribution sets the effective confidence bounds we have on distance. This is a parameter you can set experimentally or through an optimization based methodology (if you had a lot of data to work with!)

### Stochastic Noise
We know that our sensor readings are likely not perfect, and realistically, neither is the map. To account for some amount of error in those systems, we can add noise drawn from a Uniform distribution to our probability estimate.

### Consult Probabilistic Robotics for more Detail
Consider consulting [Probabilistic Robotics](https://docs.ufpr.br/~danielsantos/ProbabilisticRobotics.pdf) for more details on using range-finders and likelihood functions (Specifically chapter 6.4).

#### Limitations
This method ignores the information embedded in ranges that "max out" the sensor reading (the vehicle is in empty space). This method also requires tuning a few parameters for your noise and confidence probability functions.

#### Combining Multiple Measurements
We typically have more than one range measurement at any time (that's the power of a lidar!), so we need to consider ways to combine the likelihood of each of our scans to get to one particle weight. Some options may be:
* Average the PDF values across the measurements
* Multiply the PDF values across the measurements
* Something in between?

It turns out these different approaches are all used in various forms in within the particle filters in ROS.  For example, there is a really weird way of combining multiple measurements in the [ROS1 AMCL package](https://github.com/ros-planning/navigation/blob/a9bc9c4c35a55390963db1357926ec461fcff24c/amcl/src/amcl/sensors/amcl_laser.cpp#L293). See this [pull request](https://github.com/ros-planning/navigation/pull/462) for some interesting discussion of this method.

In ROS2, it seems they still have the [old method](https://github.com/ros-planning/navigation2/blob/7be609e67c5b8f7e54b3bc2bcd53d41e652c494e/nav2_amcl/src/sensors/laser/likelihood_field_model.cpp#L124) but there is [another method](https://github.com/ros-planning/navigation2/blob/main/nav2_amcl/src/sensors/laser/likelihood_field_model_prob.cpp) that seems more principled (but may perform worse?).

## Possible Extensions (For Your Consideration)
Here are some possible extensions on the particle filter if you'd like to pursue them.  In the open work time we can provide more detail on how these might work.

* I want to solve the robot kidnapping problem (unknown starting location)
* I want to reimplement the parts of the filter that were written for me (interactions with ROS)
* I want to experiment with laser scan likelihood functions
* I want to try to implement ray tracing instead of the likelihood field
* I want to understand in greater detail the connection between Bayes' filter and the particle filter
* I want to make my particle filter more computationally efficient
* I want to experiment with landmark-based likelihood functions
* I want to move my robot based on my pose uncertainty
