#! /usr/bin/env python

from py_compile import main
import rospy
import time
import actionlib
from manipulator_groep_1.msg import control_robotGoal, control_robotResult, control_robotAction, control_robotFeedback
from hmi.msg import HMI_state
from std_msgs.msg import UInt8

# We create some constants with the corresponing vaules from the SimpleGoalState class
PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received

# initializes the action client node

class MainProgramClass():
    def __init__(self):
        # Manipulator
        # maak een action server client aan voor de manipulator module en wacht tot deze is opgestart
        action_server_name_manipulator = '/control_robot'
        self.client_manipulator = actionlib.SimpleActionClient(action_server_name_manipulator, control_robotAction)
        self.client_manipulator.wait_for_server()
        rospy.loginfo("\n \n Action Server Found...'+action_server_name_manipulator \n \n")

        # HMI
        # Maak een subscriber en publisher voor de HMI.
        # Declare variabelen voor de knoppen en functies.
        rospy.Subscriber("/avans/buttons/state", UInt8, self.HMICallback)
        self.pub = rospy.Publisher('/HMI', HMI_state, queue_size=10)
        rospy.loginfo("\n \nHMI publisher and subscriber made successfully\n \n")
        self._fout = False
        self._storing = False
        self._noodstop = False
        self._stop = False

        self._continu = True
    
    def HMICallback(self, data):
        buttonstate = data

        if buttonstate == 8 and self._fout: # Noodstop en fout.
            self.stopProgram()
        elif buttonstate == 1: # 1 cyclus.
            self.single()
        elif buttonstate == 2 and self._continu: # Continue cyclus.
            self.continuous()
    
    def single(self):
        ""

    def continuous(self):
        ""

        #Deel 1 bepalen product en oppakken
        #Transportsysteem
        #Manipulator
        #Machinevision
        #Manipulator
        #Gripper

        #Deel 2 sorteren
        #Transportsysteem
        #Manipulator
        #Gripper









    def checkNoodstop(self):
        if self._noodstop == True:
            self.noodstop()

    def stopProgram(self):
        msg = HMI_state()
        msg.programstate = "fout"
        msg.programtype = "main"
        self.pub.publish(msg)
        rospy.loginfo("!!!--Emergency stop pressed--!!!")





        

if __name__ == '__main__':
    rospy.init_node('sorteerinstallatie')
    MainProgramClass()
    rospy.spin()
        