#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty, Float32, UInt8

escape = False

rospy.init_node("Start_Transportsysteem")

def callbackStart(self):
    rospy.loginfo('callbackStart')
    sub_state = rospy.Subscriber('/HMI', UInt8, callbackState, queue_size=1)
    global escape
    escape = False

def callbackState(msg):
    global escape
    if escape == False:
        state = msg
        rospy.loginfo('callbackState')
        while pub_state.get_num_connections() < 1:
            ""
        pub_state = rospy.Publisher('/Start_state', UInt8, queue_size=1)
        pub_state.publish(state)
        escape = True


sub_start = rospy.Subscriber('/Start', Empty, callbackStart)

rospy.spin()
