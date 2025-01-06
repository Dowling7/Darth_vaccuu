---
title: "Configuring a Raspberry Pi Image for the Neato"
---

<p align="center"> <img src="../website_graphics/neato_overview.jpeg" alt="A picture of a Neato robotic vacuum cleaner with a custom remote control interface based on Raspberry Pi" width="60%" height="60%">
</p>

The Neato setup requires a Raspberry Pi to act as a remote control interface between the student laptop and the robot. We have created a setup based on a Raspberry Pi with an accompanying 16x2 LCD panel (for displaying debug information regarding Wifi).

Once you've purchased [the relevant hardware](shopping_list) and completed the setup of the LCD panel (it requires about 30 minutes of soldering), you are ready to go.

## Configuring the Raspberry Pi Image

Starting with a MicroSD card with at least 8GB capacity, perform the following steps.

1. Flash the SD card with the latest version of Raspberry Pi OS Lite (the lite version will make sure you don't have a desktop environment installed).  The [Raspberry Pi Imager](https://www.raspberrypi.com/software/) software makes doing this a breeze.
2. Startup the Pi and go through the initial configuration.  You'll configure your keyboad and setup your login.  To use our software unmodified, choose ``pi`` as your login.
3. Login to your raspberry pi and execute the following command.  You'll be prompted to enter your Wifi SSID and password.
{% highlight console %}
$ source <(curl http://occam.olin.edu/install_pi)
{% endhighlight %}

## Operating Instructions

Once you've created the image, use one of the micro USB cables to connect the Neato to the Raspberry Pi.  Use the other micro USB cable to connect the USB battery pack to the power input port of the the Pi.  If you have a Raspberry Pi Cam module, you can connect that as well (currently, we dont' support the new rev 3 camera).  All other operating instructions are given in [the student-facing guide on operating the robots](use_the_neatos).
