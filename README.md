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
<img src="./S31image70.jpeg" alt="Sample Image" width="800">

Actually, you can not detect an object in the second picture, because it hides in the fog!

### Combining RGB with IR

To solve the issue my team came up with the idea to view IR pictures as a weighted heatmap for matching RGB pictures. Generally speaking, we convert infrared intensity values to colors, with higher values often represented by "hot" colors (e.g., red, yellow) and lower values by "cold" colors (e.g., blue) and combine those "new" pixels with RGB pixels.

Here is the example with the second picture!

<div style="text-align: left;">
  <img src="./S31Timage70.jpeg" title="Original image" width="800">
  <p><em>Figure 1: Infrared image.</em></p>
</div>

<div style="text-align: left;">
  <img src="./image.png" title="Original image" width="800">
  <p><em>Figure 2: Modified image.</em></p>
</div>

### Training dual Transformer

The model, proposed to solve the object detection task, can be found [here](https://huggingface.co/google/owlv2-base-patch16-ensemble).
