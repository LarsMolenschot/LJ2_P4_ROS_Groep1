#! /usr/bin/env python

# importing packages
# Publischer die een empty message stuurt naar topic/start_band
# Subscriber die luisterd naar positie_band van massage type std_msgs/float32
# Als die waardes tussen 4,99 en 5,01 moet hij iets uitschrijven

import rospy
import time
from std_msgs.msg import Empty, Float32
rospy.init_node('a')
R=rospy.Rate(0.1)


pub_band = rospy.Publisher('/Start', Empty, queue_size=1)
#start_band = Empty()

c = pub_band.get_num_connections()
rospy.loginfo(c)
while pub_band.get_num_connections() < 1:
    ""

c = pub_band.get_num_connections()
rospy.loginfo(c)
pub_band.publish()
#rospy.spin()
#R.sleep()
