#! /usr/bin/env python

import rospy
import time
import actionlib
from manipulator_groep_1.msg import control_robotGoal, control_robotResult, control_robotAction, control_robotFeedback

# We create some constants with the corresponing vaules from the SimpleGoalState class
PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received

# initializes the action client node
rospy.init_node('hoofdprogramma_node')

#maak een action server client aan voor de manipulator module en wacht tot deze is opgestart
action_server_name_manipulator = '/control_robot'
client_manipulator = actionlib.SimpleActionClient(action_server_name_manipulator, control_robotAction)
client_manipulator.wait_for_server()
rospy.loginfo('Action Server Found...'+action_server_name_manipulator)