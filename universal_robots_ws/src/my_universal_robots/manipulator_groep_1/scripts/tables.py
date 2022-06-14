#! /usr/bin/env python

import rospy
import xml.etree.ElementTree as ET

from geometry_msgs.msg import Pose

param_name = "/default_poses"

rospy.loginfo("program started!")
print("program started!")

#get parameter data
pose = Pose()

tree = ET.parse("../config/default_poses.xml")
root = tree.getroot()

for pos in root.findall("positie"):
    name = pos.get('name')

    print(name)

    value = pos.find("w").text 
    pose.orientation.w = float(value)        
    value = pos.find("x").text 
    pose.position.x = float(value)
    value = pos.find("y").text 
    pose.position.y = float(value)
    value = pos.find("z").text 
    pose.position.z = float(value)
    value = pos.find("Rx").text 
    pose.orientation.x = float(value)
    value = pos.find("Ry").text 
    pose.orientation.y = float(value)
    value = pos.find("Rz").text 
    pose.orientation.z = float(value)

    print("position is:\n")
    print(pose)


