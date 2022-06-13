#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg

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

        move_group = MoveGroupInterface("arm", "base_link")

        joints = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint",
                  "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]

        bak1 = [-0.1010, -2.1760, -0.9014, -1.6304, 1.5711, -0.1034]
        bak2 = [-0.1757, -1.6311, -1.6720, -1.4296, 1.5767, -0.1748]
        mag = [0.4328, -1.8104, -1.4624, -1.4597, 1.5894, 0.4328]
        vision = [-0.4414, -1.0941, -2.1131, -1.5163, 1.6127, -0.4760]

        poserequested = robotgoal.position.data

        if poserequested == "bak1":
            dest = bak1
        elif poserequested == "bak2":
            dest = bak2
        elif poserequested == "mag":
            dest = mag
        elif poserequested == "vision":
            dest = vision

        result = move_group.moveToJointPosition(joints, dest, 0.02)
        if result:
            if result.error_code.val == MoveItErrorCodes.SUCCESS:
                rospy.loginfo("Trajectory successfully executed!")
            else:
                rospy.logerr("Arm goal in state: %s",
                move_group.get_move_action().get_state())
        else:
            rospy.logerr("MoveIt failure! No result returned.")

        move_group.get_move_action().cancel_all_goals()

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
