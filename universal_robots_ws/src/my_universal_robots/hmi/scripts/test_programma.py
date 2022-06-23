#!/usr/bin/env python
import rospy

#from std_msgs.msg import String

#from nav_msgs.msg import Odometry

from std_msgs.msg import UInt8

ledstate = 0

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    #rospy.loginfo(data)
    global ledstate
    ledstate = data
    
def listener():
    rospy.Subscriber("/avans/buttons/state", UInt8, callback)

     # spin() simply keeps python from exiting until this node is stopped
    #rospy.spin()

def publisher():
    pub = rospy.Publisher('/avans/leds/state', UInt8, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    global ledstate
    rospy.loginfo(ledstate)
    pub.publish(ledstate)
    rate.sleep()


if __name__ == '__main__':
    rospy.init_node("led")
    while not rospy.is_shutdown():
        listener()
        publisher()
