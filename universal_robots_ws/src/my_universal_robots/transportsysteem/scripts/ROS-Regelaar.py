#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty, Float32, UInt8

def callbackStart():
    sub_state = rospy.Subscriber('/HMI', UInt8, callbackState)


def callbackState(state):
    pub_state = rospy.Publisher('/Stand_state', UInt8, queue_size=1)
    pub_state.publisch(state)

sub_start = rospy.Subscriber('/Start', Empty, callbackStart)
