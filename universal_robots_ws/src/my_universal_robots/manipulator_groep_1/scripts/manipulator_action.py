#! /usr/bin/env python

import rospy
from moveit_python import MoveGroupInterface
from moveit_msgs.msg import MoveItErrorCodes

rospy.init_node('moveit_python_tutorial', anonymous=True)

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
