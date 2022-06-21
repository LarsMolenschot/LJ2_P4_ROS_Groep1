#! /usr/bin/env python

from py_compile import main
import rospy
import time
import actionlib
from manipulator_groep_1.msg import control_robotGoal, control_robotResult, control_robotAction, control_robotFeedback
from hmi.msg import HMI_state
from geometry_msgs.msg import Pose
from std_msgs.msg import UInt8
from gripper_besturing.srv import *

# We create some constants with the corresponing vaules from the SimpleGoalState class


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

        self.PENDING = 0
        self.ACTIVE = 1
        self.DONE = 2
        self.WARN = 3
        self.ERROR = 4

        self.manipulator_goal = control_robotGoal()
        self.visionpose = Pose()
        self.manrate = rospy.Rate(1)
        rospy.loginfo("\n \n manipulator started! \n \n")

        # HMI
        # Maak een subscriber en publisher voor de HMI.
        # Declare variabelen voor de knoppen en functies.
        rospy.Subscriber("/avans/buttons/state", UInt8, self.HMICallback)
        self.pub = rospy.Publisher('/HMI', HMI_state, queue_size=1)
        rospy.loginfo("\n \nHMI publisher and subscriber made successfully\n \n")
        self._fout = False
        self._storing = False
        self._noodstop = False
        self._stop = False

        self._continu = True

        # Gripper
        # Connect to gripper service server, than activate gripper. (it will open and close)
        #rospy.wait_for_service('gripper_open_of_dicht_doen')
        #self._gripper_program = rospy.ServiceProxy('gripper_open_of_dicht_doen', gripperServiceMessage)
        #self._gripper_service_response = self._gripper_program('open', 0)
        rospy.loginfo("\n \n gripper started\n \n")

        #rospy.loginfo("in subscriber loop before while")
        #while not rospy.is_shutdown():
        #    rate = rospy.Rate(1)
        #    rospy.Subscriber("/avans/buttons/state", UInt8, self.HMICallback)
        #    rospy.loginfo("in subscriber loop")
        #    rate.sleep()

            

    def HMICallback(self, data):
        text = "in callback subscriber with data: "+ str(data.data)
        
        buttonstate = data.data

        if buttonstate == 8 and self._fout: # Noodstop en fout.
            self.stopProgram()
        elif buttonstate == 1: # 1 cyclus.
            rospy.logwarn(text)
            self.single()
        elif buttonstate == 2 and self._continu: # Continue cyclus.
            rospy.logwarn(text)
            self.continuous()
    
    def single(self):
        ""

    def continuous(self):
        rospy.loginfo("in continuous")
        #Manipulator naar home 
        self.manipulator_goal.mode.data = False
        self.manipulator_goal.position.data = "home"
        self.client_manipulator.send_goal(self.manipulator_goal)

        state_result = self.client_manipulator.get_state()

        while state_result < self.DONE:
            rospy.logwarn("moving to home")
            
            state_result = self.client_manipulator.get_state()
            rospy.loginfo("state_result: "+str(state_result))
            self.manrate.sleep()

        state_result = self.ACTIVE

        #Manipulator naar vision
        self.manipulator_goal.mode.data = False
        self.manipulator_goal.position.data = "vision"
        self.client_manipulator.send_goal(self.manipulator_goal)

        while state_result < self.DONE:
            rospy.logwarn("moving to vision")
            
            state_result = self.client_manipulator.get_state()
            rospy.loginfo("state_result: "+str(state_result))
            self.manrate.sleep()
        
        state_result = self.ACTIVE

        #Machinevision
        #self.visionpose.position.x = visionfeedback.x

        #Transportsysteem if vision geen object
        
        #Manipulator op positie vision
        self.manipulator_goal.mode.data = True

        self.manipulator_goal.lineairpose.position.x = 0.01
        self.manipulator_goal.lineairpose.position.y = 0.01
        self.manipulator_goal.lineairpose.position.z = 0

        self.manipulator_goal.lineairpose.orientation.x = 0
        self.manipulator_goal.lineairpose.orientation.y = 0
        self.manipulator_goal.lineairpose.orientation.z = 0
        self.manipulator_goal.lineairpose.orientation.w = 0
        self.client_manipulator.send_goal(self.manipulator_goal)

        while state_result < self.DONE:
            rospy.logwarn("moving to visionfeedback")
            
            state_result = self.client_manipulator.get_state()
            rospy.loginfo("state_result: "+str(state_result))
            self.manrate.sleep()

        state_result = self.ACTIVE

        #Manipulator naar beneden
        self.manipulator_goal.mode.data = True

        self.manipulator_goal.lineairpose.position.x = 0
        self.manipulator_goal.lineairpose.position.y = 0
        self.manipulator_goal.lineairpose.position.z = -0.01

        self.manipulator_goal.lineairpose.orientation.x = 0
        self.manipulator_goal.lineairpose.orientation.y = 0
        self.manipulator_goal.lineairpose.orientation.z = 0
        self.manipulator_goal.lineairpose.orientation.w = 0
        self.client_manipulator.send_goal(self.manipulator_goal)

        while state_result < self.DONE:
            rospy.logwarn("moving to down")
            
            state_result = self.client_manipulator.get_state()
            rospy.loginfo("state_result: "+str(state_result))
            self.manrate.sleep()

        state_result = self.ACTIVE

        #Gripper dicht
        #self._gripper_service_response = self._gripper_program('dicht', 1)
        rospy.loginfo("gripper gaat dicht")

        #Manipulator naar home 
        self.manipulator_goal.mode.data = False
        self.manipulator_goal.position.data = "home"
        self.client_manipulator.send_goal(self.manipulator_goal)

        state_result = self.client_manipulator.get_state()

        while state_result < self.DONE:
            rospy.logwarn("moving to home")
            
            state_result = self.client_manipulator.get_state()
            rospy.loginfo("state_result: "+str(state_result))
            self.manrate.sleep()

        state_result = self.ACTIVE

        #Manipulator naar sorteerpositie
        self.manipulator_goal.mode.data = False

        #if visionobject == "broek_groot"
        self.manipulator_goal.position.data = "bak1_1"
        #elif visionobject == "broek_groot"
            #self.manipulator_goal.position.data = "bak1_2"
        #elif visionobject == "broek_groot"
            #self.manipulator_goal.position.data = "bak1_3"
        #elif visionobject == "broek_groot"
            #self.manipulator_goal.position.data = "bak1_4"
        #elif visionobject == "broek_groot"
            #self.manipulator_goal.position.data = "bak2_1"
        #elif visionobject == "broek_groot"
            #self.manipulator_goal.position.data = "bak2_2"
        #elif visionobject == "broek_groot"
            #self.manipulator_goal.position.data = "bak2_3"
        #elif visionobject == "broek_groot"
            #self.manipulator_goal.position.data = "bak2_4"
        #else
            #self.manipulator_goal.position.data = home
            #error naar hmi
            #msg = HMI_state()
            #msg.programstate = "fout"
            #msg.programtype = "machinevision"
            #rospy.logwarn("no object found by vision")
            #self.pub.publish(msg)

        self.client_manipulator.send_goal(self.manipulator_goal)

        while state_result < self.DONE:
            rospy.logwarn("moving to positie vision voordef")
            
            state_result = self.client_manipulator.get_state()
            rospy.loginfo("state_result: "+str(state_result))
            self.manrate.sleep()

        state_result = self.ACTIVE

        #gripper open
        #self._gripper_service_response = self._gripper_program('open', 1)
        rospy.loginfo("gripper gaat open")

        #Manipulator naar bak2_4 
        self.manipulator_goal.mode.data = False
        self.manipulator_goal.position.data = "bak2_4"
        self.client_manipulator.send_goal(self.manipulator_goal)

        state_result = self.client_manipulator.get_state()

        while state_result < self.DONE:
            rospy.logwarn("moving to bak2_4")
            
            state_result = self.client_manipulator.get_state()
            rospy.loginfo("state_result: "+str(state_result))
            self.manrate.sleep()

        state_result = self.ACTIVE
        











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
        