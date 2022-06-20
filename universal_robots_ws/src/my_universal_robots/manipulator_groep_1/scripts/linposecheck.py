 #! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg

from geometry_msgs.msg import Pose

rospy.init_node('lincheck')

moveit_commander.roscpp_initialize(sys.argv)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)


#get current position
curr_pose = Pose()
curr_pose = group.get_current_pose()

pose_target = Pose()
pose_target.orientation.w = curr_pose.pose.orientation.w
pose_target.orientation.x = curr_pose.pose.orientation.x
pose_target.orientation.z = curr_pose.pose.orientation.z
pose_target.orientation.y = curr_pose.pose.orientation.y
pose_target.position.x = curr_pose.pose.position.x
pose_target.position.y = curr_pose.pose.position.y
pose_target.position.z = curr_pose.pose.position.z

print(pose_target)