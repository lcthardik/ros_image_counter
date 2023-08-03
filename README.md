# ros_image_counter

All three nodes can be started using the launch file by the following command

```
roslaunch image_counter image_counter.launch

```

While using the package, I have used an internal webcam and all the images will be stored in a folder names "ros_saved_imgs" in the home directory. The .txt file will also be made and stored in the home directory with the name "ros_saved_img_paths.txt"

### To use the package, you can follow the following steps:
* Create a workspace and clone the package inside the *src* folder
* Use the catkin_make command
* Source the setup.bash file
* Use the above roslaunch command to run all three nodes

### RQT GRAPH
![RQT_GRAPH_IMAGE](https://github.com/lcthardik/ros_image_counter/blob/main/rqt_graph.jpg?raw=true "RQT_GRAPH")

### Demo Video Link is given below
[Youtube Link](https://youtu.be/bERxuLKBdCE)

#### *Important: I have used ROS Noetic Ninjemys*
