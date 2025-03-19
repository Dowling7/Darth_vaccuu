---
title: "Troubleshooting Tips"
toc_sticky: true
---

There are some troubleshooting tips located in other documents.  When I think someone is likely to encounter an error immediately upon doing something (e.g., setting up their computing environment), I've put the troubleshooting section directly in the document that describes that process.  This document is for troubleshooting things that don't fall into that category.

## Neato Node Won't Run or Build

You may get some weird errors complaining about being unable to import the symbol ``BASE_WIDTH`` from module ``neato_hybrid_driver.py``.  You may also be finding that your ``colcon build --symlink-install`` step fails.  If this this is the case, here are a few things to check that might get you back on track.

### Make sure Conda is not active

ROS2 and Anaconda don't play nicely together.  If you currently have Anaconda active (e.g., you see ``(base)`` at the beginning of your command prompt), you should probably deactivate Anaconda and rebuild your workspace.  You can deactivate conda using:

```bash
$ conda deactivate
```

If you want to avoid having to do this in every new terminal, you can add this to your ``~/.bashrc`` file.

Once you have done this, clean out your build folder and rebuild.

```bash
$ cd ros2_ws
$ rm -rf build log install
$ colcon build --symlink-install
$ source install/setup.bash
```

### Make sure you don't have a build in ``ros2_ws/src``

While I have not been able to reproduce this perfectly on my machine, I have seen some students who have difficulties running Neato node due to mistakenly having run ``colcon build`` in their ``~/ros2_ws/src`` directory (remember, you always want to run ``colcon build`` from ``~/ros_ws``.  To fix this issue, we will remove the all build files from ``~/ros2_ws/src`` and build again.

```bash
$ cd ~/ros2_ws/src
$ rm -rf build log install
$ cd ..
$ rm -rf build log install
$ colcon build --symlink-install
$ source install/setup.bash
```

## Topics Don't Show up

Perhaps you read in the [How to Use the Neatos Page](../How to/use_the_neatos) about a particular topic.  You are puzzled when you run ``ros2 topic list`` and you don't see a particular topic listed.  Here are some tips for troubleshooting.

### Make sure you are connected to a Neato or Neato Simulator

The Neato node or the Neato gazebo package need to be running in order for these topics to show up.  Perhaps you shutdown your Neato node or simulator?  Make sure they are running and try to view the topics again.
