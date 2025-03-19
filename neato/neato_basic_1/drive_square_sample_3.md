---
title: "An example of a multi-threaded approach to a task that unfolds over time"
toc_sticky: true 
source1: "drive_square_sample_3/drive_square_3.py" 
---

## An example of a multi-threaded approach to a task that unfolds over time

This code provides a specific way to architect code that executes a task consisting of a sequence of steps (in this case driving a square).  This version uses a second thread to execute the high-level logic of this task.

This code is also in the Github repo on [class_activities_and_resources](https://github.com/comprobo24/class_activities_and_resources).

<a href="{{ page.source1 }}">Source: drive_square_sample_3.py</a>

{% highlight python %}
{% include_relative {{ page.source1 }} %}
{% endhighlight %}
