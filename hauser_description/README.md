This is the urdf files of bulldozing robot: hauser based on husky

# folder tree
	robot_description
    |―― README.md
	|―― CMakeList.txt
	|―― package.xml
	|―― meshes  <--ロボットの形状や色を表現するCOLLADAファイル
		|―― chassis_base.dae
		|―― chassis_top.dae
		|―― top_plate.dae
		|―― wheel.dae
		
	|―― models/robot   <--ロボットを構成するxacroファイルをすべてまとめる
        |―― robot.urdf.xacro
		|―― husky.urdf.xacro
	|―― urdf    <--urdfまたはxacroファイル(マクロ)
		|―― common.xacro
		|―― chassis
		    |―― chassis.urdf.xacro
		|―― wheel
			|―― wheel.urdf.xacro
			|―― wheel.gazebo.xacro
			|―― wheel.transmission.xacro
		|―― blade
			|―― blade.urdf.xacro
            |―― blade.gazebo.xacro
		|―― sensors
            |―― imu.xacro.urdf
			|―― imu.gazebo.urdf
			|―― realsense.xacro.urdf
			|―― realsense.gazebo.urdf

# How to use
This code use urdf files of realsense2_description package. You MUST download realsense-ros-pkg which includes the description.

1. [install librealsense](https://tomson784.github.io/ros_practice/realsense_ros/install.html)
2. install ros rappers
```
$ cd ~/hauser_ws/src
$ sudo apt install ros-melodic-ddynamic-reconfigure
$ git clone https://github.com/IntelRealSense/realsense-ros.git
$ cd realsense-ros/
$ git checkout `git tag | sort -V | grep -P "^2.\d+\.\d+" | tail -1`
$ cd ../../
$ catkin init
$ catkin clean
$ catkin config --cmake-args -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release
	$ catkin build
$ source devel/setup.bash
		
$ roslaunch realsense2_camera rs_camera.launch
```