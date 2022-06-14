#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import xml.etree.ElementTree as ET

from moveit_python import MoveGroupInterface
from moveit_msgs.msg import MoveItErrorCodes
from geometry_msgs.msg import Pose

from manipulator_groep_1.msg import control_robotFeedback, control_robotResult, control_robotAction

import actionlib

class controlUR5Class():

    _success = control_robotResult

    def __init__(self):
            self.UR5_action = actionlib.SimpleActionServer('control_robot', control_robotAction, self.moverobot ,False)
            self.UR5_action.start()

            self.defaultposition = Pose()
            self.defaultposition.orientation.w = 1.000000
            self.defaultposition.orientation.x = 0.000000
            self.defaultposition.orientation.z = 0.000000
            self.defaultposition.orientation.y = 0.000000
            self.defaultposition.position.x = 0.28
            self.defaultposition.position.y = -0.11
            self.defaultposition.position.z = 0.46

            rospy.loginfo("actionserver running!")

    def movepredefined(self, robotgoal):
        rospy.loginfo("mode = 0")
        rospy.loginfo("moving to predefined position %s", robotgoal.position.data)
        #mode for moving to predefined positions

        #create moveitcommander
        moveit_commander.roscpp_initialize(sys.argv)

        robot2 = moveit_commander.RobotCommander()
        scene2 = moveit_commander.PlanningSceneInterface()
        group2 = moveit_commander.MoveGroupCommander("arm")
        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

        #get the positions from default_poses.xml
        pose = Pose()

        tree = ET.parse("../config/default_poses.xml")
        root = tree.getroot()

        curr_pose = Pose()
        curr_pose = group2.get_current_pose()

        for pos in root.findall("positie"):
            name = pos.get('name')
            print(str(name))
            rospy.loginfo(str(robotgoal.position.data))

            if str(name) == str(robotgoal.position.data):
                value = pos.find("w").text 
                pose.orientation.w = float(value)        
                value = pos.find("x").text 
                pose.position.x = float(value)
                value = pos.find("y").text 
                pose.position.y = float(value)
                value = pos.find("z").text 
                pose.position.z = float(value)
                value = pos.find("Rx").text 
                pose.orientation.x = float(value)
                value = pos.find("Ry").text 
                pose.orientation.y = float(value)
                value = pos.find("Rz").text 
                pose.orientation.z = float(value)

        rospy.loginfo("moving to: \n")
        rospy.loginfo(pose)

        #set planning settings
        group2.set_planner_id("RRTConnectkConfigDefault")
        group2.set_planning_time(10)
        group2.set_num_planning_attempts(20)
        group2.set_end_effector_link("tcp_link")
        group2.set_goal_tolerance(0.01)

        #set the destination
        group2.set_pose_target(pose)

        #plan the route and move the robot
        plan2 = group2.plan()
        group2.go(wait=True)
        
        self._success = True
        self.UR5_action.set_succeeded(self._success)

    def movelineair(self, robotgoal):
        moveit_commander.roscpp_initialize(sys.argv)

        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()
        group = moveit_commander.MoveGroupCommander("arm")
        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)


        #get current position
        curr_pose = Pose()
        curr_pose = group.get_current_pose()

        pose_target = Pose()
        pose_target.orientation.w = curr_pose.pose.orientation.w + robotgoal.lineairpose.orientation.w
        pose_target.orientation.x = curr_pose.pose.orientation.x + robotgoal.lineairpose.orientation.x
        pose_target.orientation.z = curr_pose.pose.orientation.z + robotgoal.lineairpose.orientation.z
        pose_target.orientation.y = curr_pose.pose.orientation.y + robotgoal.lineairpose.orientation.y
        pose_target.position.x = curr_pose.pose.position.x + robotgoal.lineairpose.position.x
        pose_target.position.y = curr_pose.pose.position.y + robotgoal.lineairpose.position.y
        pose_target.position.z = curr_pose.pose.position.z + robotgoal.lineairpose.position.z

        group.set_planner_id("RRTConnectkConfigDefault")
        group.set_planning_time(5)
        group.set_num_planning_attempts(10)
        group.set_end_effector_link("tcp_link")
        group.set_goal_tolerance(0.01)
        group.set_pose_target(pose_target)

        #move robot to the position
        plan1 = group.plan()

        group.go(wait=True)

        self._success = True
        self.UR5_action.set_succeeded(self._success)

    def moverobot(self, robotgoal):
        if robotgoal.mode.data == 0:
            self.movepredefined(robotgoal)
        elif robotgoal.mode.data == 1:
            self.movelineair(robotgoal)



if __name__ == '__main__':
    rospy.init_node('robotAction')
    controlUR5Class()
    rospy.spin()
