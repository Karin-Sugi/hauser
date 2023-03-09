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