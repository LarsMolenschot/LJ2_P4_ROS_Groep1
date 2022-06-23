#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty, Float32, UInt8

escape = False
escape2 = False

rospy.init_node("Start_Transportsysteem")

def callbackStart(self):
    rospy.loginfo('callbackStart')
    global escape2
    while escape2 == False:
        sub_state = rospy.Subscriber('/HMI_transportsysteem', UInt8, callbackState, queue_size=1)
        global escape
        escape = False

def callbackState(msg):
    global escape
    global escape2
    escape = True

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
