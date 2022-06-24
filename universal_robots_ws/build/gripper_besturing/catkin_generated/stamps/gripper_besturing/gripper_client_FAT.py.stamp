#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from gripper_besturing.srv import * #import all service msgs

def add_two_ints_client(x, y):
    rospy.wait_for_service('gripper_open_of_dicht_doen')
    try:
        add_two_ints = rospy.ServiceProxy('gripper_open_of_dicht_doen', gripperServiceMessage)
        resp1 = add_two_ints(x, y)
        resp1List = [resp1.succes, resp1.found_object, resp1.error_nummer, resp1.error_tekst]
        return resp1List
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = str(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print('[Systeem] Service response: ' + str(add_two_ints_client(x, y)))
