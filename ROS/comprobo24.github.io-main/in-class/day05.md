---
title: "Frameworks for Challenging Discussions // Coordinate Frames"
toc_sticky: true
toc_data:
  - title: Today
    link: in-class/day05/#today
  - title: For Next Time
    link: in-class/day05/#for-next-time
  - title: Warm-Up Project Check-In
    link: in-class/day05/#warmup-checkin
  - title: Coordinate Frames and Coordinate Transforms in Robotics
    link: in-class/day05/#coordinate-frames-and-coordinate-transforms-in-robotics
---

## Today
* Warm-Up Project Check-In
* Frameworks for Challenging Discussions (For Your Consideration)
* Coordinate Frames and Coordinate Transforms in Robotics (Guided Group Exercise)
* Studio Time

## For Next Time
* Work on the <a href="../assignments/warmup_project">the Warmup Project</a>.
  * The final warm-up project deliverables will be due **Monday 23rd at 7PM**!
  * A rubric for the project is available [on Canvas](https://canvas.olin.edu/courses/822/assignments/13049).
* Work on the [Broader Impacts assignment Part 1](../assignments/broader_impacts), due on **Friday 27th at 1PM**.

## Warm-Up Project Check-In
You all have assembled some great slides sharing what you've learned so far. Let's have a look: [Slides](https://docs.google.com/presentation/d/1IHTUBZ_jFnrjzV8K1kR34gl9X0XaGKAZjoRqxMrcg9U/edit?usp=sharing)

## Frameworks for Challenging Discussions (For Your Consideration)
In the next phase of your Broader Impacts project, you'll be asked to host an in-class discussion on your selected robot to gather different perspectives on the robotic system and its context. Discussions about perspective, context, values, and ethics can sometimes be tricky -- perhaps there is conflict among participants, or it is challenging for everyone to engage fully with a topic. To assist you in hosting your discussions, the following may be of interest:
* **Combine different discussion techniques** -- consider the use of individual quiet brainstorming, round-robin sharing, and open dialog; during what parts of a discussion might these be useful to your group? When could switching techniques change the energy of the discussion?
* **Focus on collaborative generation** -- one way to invite multiple voices is to create a mechanism that feels collaborative; if the aim of the discussion is to generate multiple perspectives on an idea, then you are inviting everyone participating in the discussion to share or experiment with different ideas and be open to hearing other ideas. This would be the opposite of focusing a discussion on a single perspective or trying to determine the "optimal" way to think about something together. 
* **Ask expansive questions** -- inviting intellectual curiosity in a discussion can assist with navigating conflict (conflict isn't bad, it just needs to be managed!). Asking expansive questions (e.g., what possibilities exist? what's the state space look like?) as opposed to questions that attempt to "narrow in" on a particular perspective/answer/topic can assist the group in becoming more creative and open to ideas.
* **Set discussion norms** -- for long discussions, it can be nice from the start to set norms for a discussion. If this can be done collaboratively, all the better! Having a framework that explicitly talks about the goals of a discussion, appropriate engagement with a discussion, and actions participants can take to address violations to the framework, can be a really useful technique in professional settings for talking about challenging topics productively.
* **Don't be afraid to pivot** -- if a discussion is getting off the rails, or you're reading the room and think that a conversation may turn unproductive, consider switching to a different discussion tactic, tabling a topic for later and moving to another question, or naming the conflict that you are seeing and allowing for meta-conversation about that conflict. 
* **Critique over criticism** -- it will be natural for folks to come with different perspectives on a topic. If conflict were to arise between perspectives, encourage critique of the ideas rather than criticism of those that hold those perspectives. Critique requires asking questions, trying to learn more, and building/improving upon an idea, whereas criticism is meant to highlight negatives and tear a perspective down.
* **Focus on evidence-based claims** -- discussions are most intellectually full when ideas that are shared are coupled with evidence that can be collaboratively inspected. Inviting opinions and feelings into a conversation is welcome, but ask participants to enrich those ideas with grounded personal anecdotes as their form of evidence.


## Coordinate Frames and Coordinate Transforms in Robotics

> Likely you've encountered the notion of multiple coordinate systems before at some point in your academic career.  Depending on your path through Olin, you may already be familiar with the mechanics of how to map vectors between different coordinate systems (either in 2D or 3D).  In this exercise, you'll get a chance to refresh some of this knowledge and to also gain a conceptual understanding of how the notion of multiple coordinate systems plays out in robotics.

### `tf2` and You

Last time, we encountered a funny logistical matter when using Rviz2 to visualize our /my_point topic -- we needed to change our "Fixed Frame" from /map to /odom. What's going on? These are two different _coordinate frames_ ROS2 uses to track a robot in a world. There are actually loads of coordinate frames we might want to be thinking about in robotics. (And you [can read more about how ROS has thought about coordinate transforms here](https://www.ros.org/reps/rep-0105.html)).

Let's get a sense for how we might encounter more coordinate transforms in ROS2 by walking through [this tutorial](https://docs.ros.org/en/humble/Tutorials/Intermediate/Tf2/Introduction-To-Tf2.html). ROS2 uses a utility called `tf2` in order to track the relationships between various entities in a world. When we walk through this tutorial, we'll be seeing how to inspect all the different transforms that are going on.

### Creating a `world` coordinate frame

Understanding the math behind what `tf2` is doing for us can be super helpful -- especially when we start thinking about debugging robot behavior, adding sensors to our robots, and interacting in increasingly complex environments.

Suppose your Neato is at position 3.0m, 5.0m with a heading of 30 degrees (where counter-clockwise rotation is positive) in a coordinate system called ``world``.  Draw a picture.  Make sure to label the axes of the ``world`` coordinate system (don't worry about the z-axis).In robotics, we frequently need to express the position of various entities (e.g., obstacles, goal locations, other robots, walls, doorways, etc.).  While we could express all of these positions in terms of the coordinate system ``world``, in many situations this will be cumbersome.

**Exercise:** Taking the Neato as an example, make a list of the coordinate systems that you feel would be convenient to define.  For each coordinate system, define its origin and give a few examples of entities that would be natural to express in that coordinate system. 

### ``base_link``

Next, we'll define ``base_link``, which will serve as our robot-centric coordinate system.  The origin of this coordinate system will be at the midpoint of the line connecting the robot's wheels.  The x-axis will point forwards, the y-axis will point to the left, and the z-axis will point up.  Update your drawing to indicate the position of the ``base_link`` coordinate axes (again, don't worry about the z-axis).

Now that we have defined our new coordinate system, we'd like to be able to take points expressed in this coordinate system and map them to the ``world`` coordinate system (and vice-versa).  In order to do this, we need to specify the relationship between these two coordinate systems.  A natural way to specify the relationship between two coordinate systems is to specify the position of the origin of one coordinate system in the other as well as the directions of the coordinate axes of one frame in the other.  Going back to our original example we can say that the coordinate axes of the Neato's ``base_link`` coordinate system are at position 3.0m, 5.0m with a rotation of 30 degrees relative to the coordinate axes of the ``world`` coordinate frame.  We usually think of this information as defining the transformation from ``world`` to ``base_link``.  It turns out that with just this information, we can map vectors between these two coordinate systems.

### From ``base_link`` to ``world``

**Exercise:** Determine the coordinates of a point located at (1.0m, 0.0m) in the ``base_link`` coordinate system in the ``world`` coordinate system.  First draw the point on the board to make sure everyone agrees what its location is.  Once you've determined your answer, how can you tell if you are right?

**Exercise:** Determine the coordinates of a point located at (0.0m, 1.0m) in the ``base_link`` coordinate system in the ``world`` coordinate system.  First draw the point on the board to make sure everyone agrees what its location is.  Once you've determined your answer, how can you tell if you are right?

**Exercise:** Determine the coordinates of a point located at (x, y) in the ``base_link`` coordinate system in the ``world`` coordinate system.  If you are having trouble operationalizing your answer in terms of equations, you can define it in terms of high-level operations (e.g., translations, rotations, etc.).


### From ``world`` to ``base_link``

There are multiple ways to tackle this one.  We think it's easiest to do algebraically (with your good-old i-hat and j-hat notation), but you can do it in terms of geometry / trigonometry too.  Don't get too hung up on the mechanics, try to understand conceptually how you would solve the problem.

**Exercise:** Determine the coordinates of a point located at (0.0m, 1.0m) in the ``world`` coordinate system in the ``base_link`` coordinate system.  First draw the point on the board to make sure everyone agrees what its location is.  Once you've determined your answer, how can you tell if you are right?

**Exercise:** Determine the coordinates of a point located at (1.0m, 0.0m) in the ``world`` coordinate system in the ``base_link`` coordinate system.  First draw the point on the board to make sure everyone agrees what its location is.  Once you've determined your answer, how can you tell if you are right?

**Exercise:** Determine the coordinates of a point located at (x, y) in the ``world`` coordinate system in the ``base_link`` coordinate system.  If you are having trouble operationalizing your answer in terms of equations, you can define it in terms of high-level operations (e.g., translations, rotations, etc.).


### Possible Notation

Sometimes, it can be helpful to lead with notation.  Other times, it can obfuscate and confuse.  Here is some notation that you could use to reason about and define coordinate systems. If this is useful to you, please go for it!

$$\begin{eqnarray}
\mathbf{p}_{/W} &\triangleq& \mbox{a point, p, expressed in coordinate system W} \\
\mathbf{p}_{/N} &\triangleq& \mbox{a point, p, expressed in coordinate system N} \\
\hat{\mathbf{i}}_{N} &\triangleq& \mbox{a unit vector in the i-hat direction of coordinate system N} \\
\hat{\mathbf{j}}_{N} &\triangleq& \mbox{a unit vector in the j-hat direction of coordinate system N} \\
\hat{\mathbf{r}}_{W\rightarrow N} &\triangleq& \mbox{a vector pointing from the origin of W to the origin of N} \\
\mathbf{r}_{W \rightarrow N / N} &\triangleq& \hat{\mathbf{r}}_{W\rightarrow N}\mbox{ expressed in coordinate system N} \\
\hat{\mathbf{i}}_{N/W} &\triangleq& \hat{\mathbf{i}}_{N}\mbox{ expressed in coordinate system W} \\
\hat{\mathbf{j}}_{N/W} &\triangleq& \hat{\mathbf{j}}_{N}\mbox{ expressed in coordinate system W}\end{eqnarray}$$


### Static Versus Dynamic Coordinate Transformations

The relationship between some coordinate systems are dynamic (meaning they change over time) and some are static (meaning they are constant over time).

**Exercise:**  Assume that our Neato robot can move about in the ``world`` by using its wheels.  Is the relationship between ``world`` and ``base_link`` static or dynamic?  Given the coordinate systems you came up with earlier, list some examples of coordinate system relationships that are static and some that are dynamic.

