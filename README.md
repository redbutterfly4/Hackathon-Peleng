# The technical task

Develop a system for automatically detecting and tracking a given object on a video with its definition
locations (x, y, z – 3D coordinates).

# Implementation

The problem can be divided into two subtasks: 
1. Develop a robust object tracking neural network, to fetch 2D coordinates of the object;
2. Develop a mathematical background for converting 2D representation into 3D.

## Object tracking

Train dataset consists of RGB and Infrared videos of 3 cameras with object moving in the same directions, except that cameras are placed in different locations. so that the object can dissapear from one or multiple cameras. Also there are different noise objects that make it hard to detect a target object in visual spectrum.

For example, look at the pictures!

<img src="./S13image17.jpeg" alt="Sample Image" width="800">

