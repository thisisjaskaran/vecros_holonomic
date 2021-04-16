# vecros_holonomic

After installing ROS, create new workspace. In terminal 1
```
mkdir -p ~/holonomic_ws/src
cd ~/holonomic_ws/
catkin_make
source devel/setup.bash
```
In terminal 2
```
roscore
```
In terminal 1
```
cd src
git clone https://github.com/thisisjaskaran/vecros_holonomic.git
chmod 770 dynamics.py
chmod 770 velocity_control.py
./dynamics.py
./velocity_control.py
```
Currently the code for velocity_control.py will give some error as it isn't complete.
