#!/usr/bin/env python
import rospy
#import sys
#from std_msgs.msg import String

#from nav_msgs.msg import Odometry

from std_msgs.msg import UInt8
#from HMI_state.msg import programstate, programtype

class Arduino_HMI:
    def __init__(self):
        #super().__init__('arduino_HMI')
        self._ledstate = 0

    def callback(self, data):
        #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        #rospy.loginfo(data)
        self._ledstate = data

    def listener(self):
        rospy.Subscriber("/avans/buttons/state", UInt8, self.callback)

        # spin() simply keeps python from exiting until this node is stopped
        #rospy.spin()

    def publisher(self):
        pub = rospy.Publisher('/avans/leds/state', UInt8, queue_size=10)
        rate = rospy.Rate(10) # 10hz
        rospy.loginfo(self._ledstate)
        pub.publish(self._ledstate)
        rate.sleep()


def main():
    Arduino_connector = Arduino_HMI()
    #rospy.init(args=args)


    rospy.init_node("led")

    Arduino_connector.listener()
    Arduino_connector.publisher()

    rospy.spin()
    #rospy.shutdown()


if __name__ == '__main__':
    while not rospy.is_shutdown():
        main()