#! /usr/bin/env python

# importing packages
# Publischer die een empty message stuurt naar topic/start_band
# Subscriber die luisterd naar positie_band van massage type std_msgs/float32
# Als die waardes tussen 4,99 en 5,01 moet hij iets uitschrijven

import rospy
from std_msgs.msg import Empty, Float32

pub_band = rospy.Publisher('/start_band', Empty, queue_size=1)
#start_band = Empty()
pub_band.publish()
