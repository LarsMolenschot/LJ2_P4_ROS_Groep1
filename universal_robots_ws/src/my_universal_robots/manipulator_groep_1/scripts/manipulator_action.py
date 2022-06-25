#! /usr/bin/env python

import sys
import copy
import rospy
import tf
import moveit_commander
import moveit_msgs.msg
import xml.etree.ElementTree as ET

from moveit_python import MoveGroupInterface
from std_msgs.msg import String
from moveit_msgs.msg import MoveItErrorCodes
from geometry_msgs.msg import Pose

from manipulator_groep_1.msg import control_robotFeedback, control_robotResult, control_robotAction

import actionlib

class controlUR5Class():

    def __init__(self):
            self.UR5_action = actionlib.SimpleActionServer('control_robot', control_robotAction, self.moverobot ,False)
            self.UR5_action.start()

            self.error_pub = rospy.Publisher('/manipulator_error',String, queue_size=1)

            self._success = control_robotResult()

            self._controlPose = Pose()

            self._planningtime = 5
            self._planattempts = 3
            self.tolorance = 0.0001

            rospy.loginfo("actionserver running!")

    def checkfinalpose(self):
        reached = True
        moveit_commander.roscpp_initialize(sys.argv)

        robot3 = moveit_commander.RobotCommander()
        scene3 = moveit_commander.PlanningSceneInterface()
        group3 = moveit_commander.MoveGroupCommander("arm")
        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

        #get the current position
        curr_pose = Pose()
        curr_pose = group3.get_current_pose()

        marge = 0.01

        if self._controlPose.position.x > curr_pose.pose.position.x + marge or self._controlPose.position.x < curr_pose.pose.position.x - marge:
            reached = False
        elif self._controlPose.position.y > curr_pose.pose.position.y + marge or self._controlPose.position.y < curr_pose.pose.position.y - marge:
            reached = False
        elif self._controlPose.position.z > curr_pose.pose.position.z + marge or self._controlPose.position.z < curr_pose.pose.position.z - marge:
            reached = False
        elif self._controlPose.orientation.x > curr_pose.pose.orientation.x + marge or self._controlPose.orientation.x < curr_pose.pose.orientation.x - marge:
            reached = False
        elif self._controlPose.orientation.y > curr_pose.pose.orientation.y + marge or self._controlPose.orientation.y < curr_pose.pose.orientation.y - marge:
            reached = False
        elif self._controlPose.orientation.z > curr_pose.pose.orientation.z + marge or self._controlPose.orientation.z < curr_pose.pose.orientation.z - marge:
            reached = False
        elif self._controlPose.orientation.w > curr_pose.pose.orientation.w + marge or self._controlPose.orientation.w < curr_pose.pose.orientation.w - marge:
            reached = False

        if reached == False or self.success == False:
            rospy.logerr("desired position not reached correctly!")
            error_msg = String()
            error_msg = "error"
            self.error_pub.publish(error_msg)

            self._success.succeeded.data = False

        else:
            rospy.loginfo("desired position reached!")

            self._success.succeeded.data = True


    def movepredefined(self, robotgoal):
        #mode for moving to predefined positions
        rospy.loginfo("mode = 0")
        rospy.loginfo("moving to predefined position %s", robotgoal.position.data)


        #create moveitcommander
        moveit_commander.roscpp_initialize(sys.argv)

        robot2 = moveit_commander.RobotCommander()
        scene2 = moveit_commander.PlanningSceneInterface()
        group2 = moveit_commander.MoveGroupCommander("arm")
        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

        #get the positions from default_poses.xml
        pose = Pose()

        tree = ET.parse("/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/src/my_universal_robots/manipulator_groep_1/config/default_poses.xml")
        root = tree.getroot()

        curr_pose = Pose()
        curr_pose = group2.get_current_pose()

        for pos in root.findall("positie"):
            name = pos.get('name')

            #set the desired position and the control position
            if str(name) == str(robotgoal.position.data):
                value = pos.find("w").text
                pose.orientation.w = float(value)
                self._controlPose.orientation.w  = float(value)

                value = pos.find("x").text
                pose.position.x = float(value)
                self._controlPose.position.x = float(value)

                value = pos.find("y").text
                pose.position.y = float(value)
                self._controlPose.position.y = float(value)

                value = pos.find("z").text
                pose.position.z = float(value)
                self._controlPose.position.z = float(value)

                value = pos.find("Rx").text
                pose.orientation.x = float(value)
                self._controlPose.orientation.x = float(value)

                value = pos.find("Ry").text
                pose.orientation.y = float(value)
                self._controlPose.orientation.y = float(value)

                value = pos.find("Rz").text
                pose.orientation.z = float(value)
                self._controlPose.orientation.z = float(value)

                self.success = True

                break
            self.success = False


        if self.success == False:
            rospy.logerr("position not defined, please pass a defined position")
            self.UR5_action.set_preempted()

        if self.success == True:
            rospy.loginfo("moving to: \n")
            rospy.loginfo(pose)

            #set planning settings
            group2.set_planner_id("RRTConnectkConfigDefault")
            group2.set_planning_time(self._planningtime)
            group2.set_num_planning_attempts(self._planattempts)
            group2.set_end_effector_link("tcp_link")
            group2.set_goal_tolerance(self.tolorance)

            #set the destination
            group2.set_pose_target(pose)

            #plan the route and move the robot
            plan2 = group2.plan()
            group2.go(wait=True)


    def movelineair(self, robotgoal):
        self.success = True

        moveit_commander.roscpp_initialize(sys.argv)

        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()
        group = moveit_commander.MoveGroupCommander("arm")
        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)


        #get current position
        curr_pose = Pose()
        curr_pose = group.get_current_pose()

        #transform from quartunnions to euler
        quaternion = (
        curr_pose.pose.orientation.x,
        curr_pose.pose.orientation.y,
        curr_pose.pose.orientation.z,
        curr_pose.pose.orientation.w)
        euler = tf.transformations.euler_from_quaternion(quaternion)

        eulerX = euler[0] + robotgoal.lineairpose.orientation.x
        eulerY = euler[1] + robotgoal.lineairpose.orientation.y
        eulerZ = euler[2] + robotgoal.lineairpose.orientation.z
        quaternion_new = tf.transformations.quaternion_from_euler(eulerX, eulerY, eulerZ)

        #transform from euler to quaternion

        #set the desired position
        pose_target = Pose()
        pose_target.orientation.w = quaternion_new[3]
        pose_target.orientation.x = quaternion_new[0]
        pose_target.orientation.z = quaternion_new[2]
        pose_target.orientation.y = quaternion_new[1]
        pose_target.position.x = curr_pose.pose.position.x + robotgoal.lineairpose.position.x
        pose_target.position.y = curr_pose.pose.position.y + robotgoal.lineairpose.position.y
        pose_target.position.z = curr_pose.pose.position.z + robotgoal.lineairpose.position.z
        #print("current pose:\n", curr_pose)
        print(pose_target)
        #set the controlpose to the desired position for error checking later
        self._controlPose.orientation.w =  robotgoal.lineairpose.orientation.w
        self._controlPose.orientation.x =  robotgoal.lineairpose.orientation.x
        self._controlPose.orientation.z =  robotgoal.lineairpose.orientation.z
        self._controlPose.orientation.y =  robotgoal.lineairpose.orientation.y
        self._controlPose.position.x = curr_pose.pose.position.x + robotgoal.lineairpose.position.x
        self._controlPose.position.y = curr_pose.pose.position.y + robotgoal.lineairpose.position.y
        self._controlPose.position.z = curr_pose.pose.position.z + robotgoal.lineairpose.position.z

        #set the planner settings
        group.set_planner_id("RRTConnectkConfigDefault")
        group.set_planning_time(self._planningtime)
        group.set_num_planning_attempts(self._planattempts)
        group.set_end_effector_link("tcp_link")
        group.set_goal_tolerance(self.tolorance)
        group.set_pose_target(pose_target)

        #move robot to the position
        plan1 = group.plan()
        group.go(wait=True)

    def moverobot(self, robotgoal):
        if robotgoal.mode.data == 0:
            self.movepredefined(robotgoal)
        elif robotgoal.mode.data == 1:
            self.movelineair(robotgoal)

        self.checkfinalpose()
        self.UR5_action.set_succeeded(self._success)



if __name__ == '__main__':
    rospy.init_node('robotAction')
    controlUR5Class()
    rospy.spin()
