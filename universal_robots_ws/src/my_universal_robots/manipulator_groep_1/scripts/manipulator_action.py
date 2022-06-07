#! /usr/bin/env python

import rospy
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

    def moverobot(self, robotgoal):
        if robotgoal.mode.data == 0:
            rospy.loginfo("mode = 0")
            #mode for moving to predefined positions

            move_group = MoveGroupInterface("arm", "base_link")

            joints = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint",
                      "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]

            bak1 = [-0.1010, -2.1760, -0.9014, -1.6304, 1.5711, -0.1034]
            bak2 = [-0.1757, -1.6311, -1.6720, -1.4296, 1.5767, -0.1748]
            mag = [0.4328, -1.8104, -1.4624, -1.4597, 1.5894, 0.4328]

            poses = [bak1, bak2, mag]

            while not rospy.is_shutdown():
                for i in poses:
                    result = move_group.moveToJointPosition(joints, i, 0.02)
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

if __name__ == '__main__':
    rospy.init_node('robotAction')
    controlUR5Class()
    rospy.spin()
