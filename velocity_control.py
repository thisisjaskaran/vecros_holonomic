#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Pose
import math

obstacles = [[]]
obst_rad = 0.0

dest = [0.0, 0.0, 0.0]
start = [10.0, 10.0, 10.0]

vel_dir_x = dest[0]-start[0]
vel_dir_y = dest[1]-start[1]
vel_dir_z = dest[2]-start[2]

mod = math.sqrt(vel_dir_x*vel_dir_x+vel_dir_y*vel_dir_y+vel_dir_z*vel_dir_z)


# variable_x = 0.0
# variable_y = 0.0
# variable_z = 0.0

# update_x = 0.0
# update_y = 0.0
# update_z = 0.0


# def update_callback(data):
#     global update_x
#     global update_y
#     global update_z
#     update_x = data.position.x
#     update_y = data.position.y
#     update_z = data.position.z

#     rospy.loginfo(rospy.get_caller_id() + 'Current Signal : (%f,%f,%f)',
#                   update_x, update_y, update_z)

def check_obstacle(x, y, z):
    for point in obstacles:
        if point[0]-


def pose_callback(data):
    global variable_x
    global variable_y
    global variable_z
    global update_x
    global update_y
    global update_z
    variable_x = data.position.x
    variable_y = data.position.y
    variable_z = data.position.z

    rospy.loginfo(rospy.get_caller_id() + 'Current Pose : (%f,%f,%f)',
                  variable_x, variable_y, variable_z)

    check_obstacle(variable_x, variable_y, variable_z)
    # print("Updating Pose...")

    # variable_x = variable_x+update_x
    # variable_y = variable_y+update_y
    # variable_z = variable_z+update_z

    # update_x = 0.0
    # update_y = 0.0
    # update_z = 0.0

    # rospy.loginfo(rospy.get_caller_id() + 'Updated Pose : (%f,%f,%f)',
    #               variable_x, variable_y, variable_z)

    # data.position.x = variable_x
    # data.position.y = variable_y
    # data.position.z = variable_z

    pub = rospy.Publisher('holonomic_pose', Pose, queue_size=10)
    rate = rospy.Rate(10)
    pub.publish((data))

    update = data
    update.position.x = update_x
    update.position.y = update_y
    update.position.z = update_z
    update.orientation.x = 0.0
    update.orientation.y = 0.0
    update.orientation.z = 0.0

    pub = rospy.Publisher('holonomic_signal', Pose, queue_size=10)
    rate = rospy.Rate(10)
    pub.publish((update))


def update_pose():
    rospy.init_node('velocity_control', anonymous=True)
    rospy.Subscriber('holonomic_updated_pose', Pose, pose_callback)
    # rospy.Subscriber('holonomic_signal', Pose, update_callback)
    rospy.spin()


if __name__ == '__main__':
    update_pose()
