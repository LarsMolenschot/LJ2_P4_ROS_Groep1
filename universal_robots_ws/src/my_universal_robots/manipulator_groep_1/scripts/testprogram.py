#! /usr/bin/env python

import rospy
import tf

quaternion = tf.transformations.quaternion_from_euler(0, 1.57, 0)
print (quaternion)
