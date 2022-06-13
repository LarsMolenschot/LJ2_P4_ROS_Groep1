#! /usr/bin/env python

import rospy
import xml.etree.ElementTree as ET

param_name = "/default_poses"

rospy.loginfo("program started!")
print("program started!")

if rospy.has_param(param_name):
    tables_param = rospy.get_param(param_name)

tree = ET.parse("default_poses.xml")
root = tree.getroot()

joints_2 = ["shoulder_pan", "shoulder_lift", "elbow",
                  "wrist_1", "wrist_2", "wrist_3"]

for pos in root.findall("positie"):
    #value = pos.find("shoulder_pan").text
    name = pos.get('name')
    
    if name == "bak1_1":
        for i in range(6):
            value = pos.find(joints_2[i]).text
            print(value)


