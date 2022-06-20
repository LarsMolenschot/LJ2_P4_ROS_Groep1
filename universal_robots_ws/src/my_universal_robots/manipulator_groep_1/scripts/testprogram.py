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
rospy.init_node('robotaction_client')

action_server_name = '/control_robot'
client = actionlib.SimpleActionClient(action_server_name, control_robotAction)

# waits until the action server is up and running
rospy.loginfo('Waiting for action Server '+action_server_name)
client.wait_for_server()
rospy.loginfo('Action Server Found...'+action_server_name)

namesarray = ["bak1", "bak2","vision", "mag"]

for i in namesarray:
    # creates a goal to send to the action server
    goal = control_robotGoal()
    goal.position.data = i

    client.send_goal(goal)

    #do stuff while action server is running
    state_result = client.get_state()

    rate = rospy.Rate(1)

    rospy.loginfo("state_result: "+str(state_result))

    while state_result < DONE:
        rospy.loginfo("Doing Stuff while waiting for the Server to give a result....")
        rate.sleep()
        state_result = client.get_state()
        rospy.loginfo("state_result: "+str(state_result))

    rospy.loginfo("[Result] State: "+str(state_result))
    if state_result == ERROR:
        rospy.logerr("Something went wrong in the Server Side")
    if state_result == WARN:
        rospy.logwarn("There is a warning in the Server Side")

#rospy.loginfo("[Result] State: "+str(client.get_result()))
