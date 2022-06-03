#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial')

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 1.0
pose_target.orientation.x = 0
pose_target.orientation.z = 0
pose_target.orientation.y = 0
pose_target.position.x = 0.28
pose_target.position.y = -0.11
pose_target.position.z = 0.46

#group.set_planner_id("SBLKconfigdefault")
group.set_planner_id("RRTConnectkConfigDefault")
group.set_planning_time(10)
group.set_num_planning_attempts(5)
group.set_end_effector_link("tcp_link")
group.set_pose_target(pose_target)

plan1 = group.plan()

group.go()



moveit_commander.roscpp_shutdown()
