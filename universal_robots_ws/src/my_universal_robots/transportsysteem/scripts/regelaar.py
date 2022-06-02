#! /usr/bin/env python

# importing packages
# Publischer die een empty message stuurt naar topic/start_band
# Subscriber die luisterd naar positie_band van massage type std_msgs/float32
# Als die waardes tussen 4,99 en 5,01 moet hij iets uitschrijven

import rospy
from std_msgs.msg import Empty, Float32

Escape = False
global Escape

def callback(msg): 
    if msg.data >= 498 and mst.data < 502
      Escape = True 

pub_band = rospy.Publisher('/start_band', Empty, queue_size=1)
start_band = Empty()
pub.publish(start_band)

while Escape == False:
   sub_band = rospy.Subscriber('/positie_band', Float32, callback)
 
print('Transportband is op positie.')

