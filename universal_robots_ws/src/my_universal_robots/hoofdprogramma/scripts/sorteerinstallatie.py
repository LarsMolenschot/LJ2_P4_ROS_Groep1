#! /usr/bin/env python

from py_compile import main
import rospy
import time
import actionlib
from manipulator_groep_1.msg import control_robotGoal, control_robotResult, control_robotAction, control_robotFeedback
from hmi.msg import HMI_state
from geometry_msgs.msg import Pose
from std_msgs.msg import UInt8, Empty, Float32
from gripper_besturing.srv import gripperServiceMessage, gripperServiceMessageResponse
from vision_message.msg import vision_msg

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
        # Maak een subscriber en publisher voor de HMI en een subscriber voor de Arduino.
        # Declare variabelen voor de knoppen en functies.
        self.sub_arduino = rospy.Subscriber("/avans/buttons/state", UInt8, self.buttonCallback, queue_size=1) # Haalt de knop waarde op van het Arduino programma.
        self.pub_HMI = rospy.Publisher('/HMI', HMI_state, queue_size=1) # Stuurt de programma toestanden naar het HMI.
        self.sub_HMI = rospy.Subscriber('/HMI', HMI_state, self.HMICallback, queue_size=1) # Haalt de stop en noodstop waarde op.
        rospy.loginfo("\n \nHMI publisher and subscriber made successfully\n \n")
        self._fout = False
        self._storing = False
        self._noodstop = False
        self._stop = False
        self.hmi_msg = HMI_state() # Object van de message HMI_state

        self._continu = False
        self._activated = False #Zorgt ervoor dat functies niet opnieuw starten als het al gestart was.


        # Gripper
        # Connect to gripper service server, than activate gripper. (it will open and close)
        rospy.wait_for_service('/gripper_open_of_dicht_doen')
        self._gripper_program = rospy.ServiceProxy('/gripper_open_of_dicht_doen', gripperServiceMessage)
        self._gripper_service_response = self._gripper_program('open', 0)
        self.gripper_response = gripperServiceMessageResponse()

        self.gripper_response = self.add_two_ints_client('open', 0)
        rospy.loginfo("\n \n gripper started\n \n")


        # Transportsysteem
        # Maak een publisher aan die het startcommando voor het transportsysteem geeft
        # Maak een publisher aan die de huidige status van het HMI doorgeeft aan het transportsysteem
        # (Dit is om de Single of Continuous modus van het transportsysteem te bepalen)
        # Maak een subscriber aan die naar de positie van de transportband luistert

        self.pub_transportsysteem = rospy.Publisher('/Start_state', UInt8, queue_size=1)
        self.pub_HMI_transportsysteem = rospy.Publisher('/HMI_transportsysteem', UInt8, queue_size=1)

        self.huidige_positie = 0
        self.single_distance = 390
        self.continous_distance = 190
        rospy.loginfo("\n \n Transportsysteem started\n \n")

        # Vision
        # Beschrijving aangemaakte publishers subscribers enzovoort............................
        # maak var aan positie en rotatie
        self.poseX = 0
        self.poseY = 0
        self.poseRX = 0
        self.poseRY = 0
        self.poseRZ = 0
        self.poseRW = 0
        self.bakNaam = ""
        self.visionEscape = False
        rospy.loginfo("\n \n Vision started\n \n")



    # Led functies
    # Stuur gereed naar HMI module.
    def gereed(self):
        #self.hmi_msg = HMI_state()
        self.hmi_msg.programstate = "gereed"
        self.hmi_msg.programtype = "main"
        self.pub_HMI.publish(self.hmi_msg)  
    
    # Stuur in bedrijf naar HMI module.
    def inbedrijf(self):
        #self.hmi_msg = HMI_state()
        self.hmi_msg.programstate = "inbedrijf"
        self.hmi_msg.programtype = "main"
        self.pub_HMI.publish(self.hmi_msg)  

    # Stuur een storing naar HMI module
    def storing(self, module):
        #self.hmi_msg = HMI_state()
        self.hmi_msg.programstate = "storing"
        self.hmi_msg.programtype = module
        self.pub_HMI.publish(self.hmi_msg)  

    # Stuur een fout naar HMI module
    def fout(self, module):
        #self.hmi_msg = HMI_state()
        self.hmi_msg.programstate = "fout"
        self.hmi_msg.programtype = module
        self.pub_HMI.publish(self.hmi_msg)  

    # Knop functies
    # Reset de stop in het HMI.
    def stopReset(self):
        self.hmi_msg.stopreset = True
        self.pub_HMI.publish(self.hmi_msg)  

    # Controleert of de stopknop en noodstop is ingedrukt tijdens de cyclus.
    def HMICallback(self, data):
        self._stop = data.stop
        self._noodstop = data.noodstop

    # Haalt stopknoppen gegevens van HMI.
    def checkStop(self):
        self.sub_HMI = rospy.Subscriber('/HMI', HMI_state, self.HMICallback, queue_size=1)

    # Noodstop 
    def noodstop(self):
        rospy.logwarn("noodstop igedrukt")

    # Callback voor de knoppen en de loop van het hoofdprogramma.
    def buttonCallback(self, data):
        text = "in callback subscriber with data: "+ str(data.data)

        buttonstate = data.data

        self.checkStop()
        #rospy.logwarn(text)

        if buttonstate == 12: # Zet storing indicatie van Noodstop naar gereed bij reset noodstop.
            self.gereed()

        if self._noodstop: # Noodstop.
            rospy.logwarn(str(self._noodstop))
            self._continu = False
            self._activated = False
            self.noodstop()
            self.storing("main")

        elif self._fout: # Fout.
            #self.stopProgram()
            ""
        elif self._storing: # Storing.
            self.storing("main")
            #self.stopProgram()
            ""
        elif buttonstate == 1 and not self._activated: # 1 cyclus.
            rospy.logwarn(text)
            self.inbedrijf()
            self._activated = True
            self.single()
            self._activated = False
            self.gereed()
            
        elif (buttonstate == 2 and not self._activated) or self._continu and not self._stop: # Continue cyclus.
            rospy.logwarn(text)
            self.inbedrijf()
            self._continu = True
            self._activated = True
            self.continuous()

        elif (self._stop and self._activated): # Stop reset.
            rospy.logwarn("awaiting stop reset")
            self.stopReset()
            self._continu = False
            self.gereed()
            if self._stop == False:
                self._activated = False


    def pos_transportsyteemCallback(self, pos):
        self.huidige_positie = pos.data
        #rospy.loginfo(pos.data)

    def add_two_ints_client(self, gripper_bewegen, opstarten_vd_gripper):
        rospy.wait_for_service('gripper_open_of_dicht_doen')
        try:
            add_two_ints = rospy.ServiceProxy('gripper_open_of_dicht_doen', gripperServiceMessage)
            resp1 = add_two_ints(gripper_bewegen, opstarten_vd_gripper)
            resp1List = [resp1.succes, resp1.found_object, resp1.error_nummer, resp1.error_tekst]
            return resp1List
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

    def callbackVision(self ,dataImage):
        #rospy.logwarn(self.visionEscape)
        while self.visionEscape == False:

            self.poseX = dataImage.vision_positie.position.x
            self.poseY = dataImage.vision_positie.position.y
            self.poseRX = dataImage.vision_positie.orientation.x
            self.poseRY = dataImage.vision_positie.orientation.y
            self.poseRZ = dataImage.vision_positie.orientation.z
            self.poseRW = dataImage.vision_positie.orientation.w

            self.bakNaam = dataImage.object_naam.data

            rospy.logerr(self.bakNaam)
            self.visionEscape = True

    #---------------------------------------
    # ----------------SINGLE----------------
    #---------------------------------------
    def single(self):
        rospy.loginfo("in single")
        self.visionEscape = False

      #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #gripper gaat open -single
            rospy.loginfo("gripper gaat open")

            self.gripper_response = self.add_two_ints_client('open', 1)
            self.gripper_response = self.add_two_ints_client('open', 1)


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar home -single
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


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar vision -single
            self.manipulator_goal.mode.data = False
            self.manipulator_goal.position.data = "vision"
            self.client_manipulator.send_goal(self.manipulator_goal)

            while state_result < self.DONE:
                rospy.logwarn("moving to vision")

                state_result = self.client_manipulator.get_state()
                rospy.loginfo("state_result: "+str(state_result))
                self.manrate.sleep()

            state_result = self.ACTIVE


        for i in range(2):
        #controleer stopknop en noodstop
            self.checkStop()
            if self._noodstop == False:
                #Transportsysteem if vision geen object -single
                rospy.loginfo("Transportband aan")

                while self.pub_transportsysteem.get_num_connections()< 1:
                    rospy.loginfo('Waiting for subscriber')
                self.pub_transportsysteem.publish(1)

                self.sub_pos_transportband = rospy.Subscriber('/enc_pos', Float32, self.pos_transportsyteemCallback)

                while self.huidige_positie <= self.single_distance:
                    ""
                    #rospy.logwarn(self.huidige_positie)
                rospy.logwarn("transportband op positie")
                self.huidige_positie = 0

                time.sleep(5)


            #controleer stopknop en noodstop
            self.checkStop()
            if self._noodstop == False:
                #Machinevision -single
                #self.visionpose.position.x = visionfeedback.x
                rospy.loginfo("start vision")
                self.visionEscape = False
                self.bakNaam = ""
                self.sub_vision = rospy.Subscriber('/image_processor/vision_pose',vision_msg, self.callbackVision)

            time.sleep(2)
            
            if self.bakNaam == "":
                rospy.loginfo("nothing detected")
            else:
                rospy.loginfo("in break")
                break


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar boven -single
            self.manipulator_goal.mode.data = True

            self.manipulator_goal.lineairpose.position.x = 0
            self.manipulator_goal.lineairpose.position.y = 0
            self.manipulator_goal.lineairpose.position.z = 0.05

            self.manipulator_goal.lineairpose.orientation.x = 0
            self.manipulator_goal.lineairpose.orientation.y = 0
            self.manipulator_goal.lineairpose.orientation.z = 0
            self.manipulator_goal.lineairpose.orientation.w = 0
            self.client_manipulator.send_goal(self.manipulator_goal)

            while state_result < self.DONE:
                rospy.logwarn("moving up")

                state_result = self.client_manipulator.get_state()
                rospy.loginfo("state_result: "+str(state_result))
                self.manrate.sleep()

            state_result = self.ACTIVE


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator op positie vision -single
            self.manipulator_goal.mode.data = True

            self.manipulator_goal.lineairpose.position.x = self.poseX
            self.manipulator_goal.lineairpose.position.y = self.poseY
            self.manipulator_goal.lineairpose.position.z = 0

            self.manipulator_goal.lineairpose.orientation.x = self.poseRX
            self.manipulator_goal.lineairpose.orientation.y = self.poseRY
            self.manipulator_goal.lineairpose.orientation.z = self.poseRZ
            self.manipulator_goal.lineairpose.orientation.w = self.poseRW
            self.client_manipulator.send_goal(self.manipulator_goal)

            while state_result < self.DONE:
                rospy.logwarn("moving to visionfeedback")

                state_result = self.client_manipulator.get_state()
                rospy.loginfo("state_result: "+str(state_result))
                self.manrate.sleep()

            state_result = self.ACTIVE


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar beneden -single
            self.manipulator_goal.mode.data = True

            self.manipulator_goal.lineairpose.position.x = 0
            self.manipulator_goal.lineairpose.position.y = 0
            self.manipulator_goal.lineairpose.position.z = -0.055

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


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Gripper dicht -single
            self._gripper_service_response = self._gripper_program('dicht', 1)
            rospy.loginfo("gripper gaat dicht")
            self.gripper_response = self.add_two_ints_client('dicht', 1)
            self.gripper_response = self.add_two_ints_client('dicht', 1)


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar boven -single
            self.manipulator_goal.mode.data = True

            self.manipulator_goal.lineairpose.position.x = 0
            self.manipulator_goal.lineairpose.position.y = 0
            self.manipulator_goal.lineairpose.position.z = 0.05

            self.manipulator_goal.lineairpose.orientation.x = 0
            self.manipulator_goal.lineairpose.orientation.y = 0
            self.manipulator_goal.lineairpose.orientation.z = 0
            self.manipulator_goal.lineairpose.orientation.w = 0
            self.client_manipulator.send_goal(self.manipulator_goal)

            while state_result < self.DONE:
                rospy.logwarn("moving up")

                state_result = self.client_manipulator.get_state()
                rospy.loginfo("state_result: "+str(state_result))
                self.manrate.sleep()

            state_result = self.ACTIVE


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar home -single
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


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar bak 2_4 -single
            self.manipulator_goal.mode.data = False
            self.manipulator_goal.position.data = "bak2_4"
            self.client_manipulator.send_goal(self.manipulator_goal)

            state_result = self.client_manipulator.get_state()

            while state_result < self.DONE:
                rospy.logwarn("moving to home")

                state_result = self.client_manipulator.get_state()
                rospy.loginfo("state_result: "+str(state_result))
                self.manrate.sleep()

            state_result = self.ACTIVE

        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar sorteerpositie -single
            printtext = "\n \n" + self.bakNaam + "\n \n"
            rospy.logwarn(printtext)
            self.manipulator_goal.mode.data = False
            self.manipulator_goal.position.data = self.bakNaam
            self.client_manipulator.send_goal(self.manipulator_goal)

            state_result = self.client_manipulator.get_state()

            while state_result < self.DONE:
                rospy.logwarn("moving to home")

                state_result = self.client_manipulator.get_state()
                rospy.loginfo("state_result: "+str(state_result))
                self.manrate.sleep()

            state_result = self.ACTIVE

        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar beneden
            self.manipulator_goal.mode.data = True

            self.manipulator_goal.lineairpose.position.x = 0
            self.manipulator_goal.lineairpose.position.y = 0
            self.manipulator_goal.lineairpose.position.z = -0.14

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

        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #gripper open -single
            self._gripper_service_response = self._gripper_program('open', 1)
            rospy.loginfo("gripper gaat open")
            self.gripper_response = self.add_two_ints_client('open', 1)
            self.gripper_response = self.add_two_ints_client('open', 1)

        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar bak2_4 -single
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


        #reset variabelen op het einde van de cyclus.
        self.visionEscape = False
    
    #---------------------------------------
    # --------------CONTINIOUS--------------
    #---------------------------------------
    def continuous(self):
        rospy.loginfo("in continuous")
        self.visionEscape = False

        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #gripper gaat open
            rospy.loginfo("gripper gaat open")

            self.gripper_response = self.add_two_ints_client('open', 1)
            self.gripper_response = self.add_two_ints_client('open', 1)


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
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


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
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

        for i in range(2):
            #controleer stopknop en noodstop
            self.checkStop()
            if self._noodstop == False:
                #Transportsysteem if vision geen object
                rospy.loginfo("Transportband aan")

                while self.pub_transportsysteem.get_num_connections()< 1:
                    rospy.loginfo('Waiting for subscriber')
                self.pub_transportsysteem.publish(2)

                self.sub_pos_transportband = rospy.Subscriber('/enc_pos', Float32, self.pos_transportsyteemCallback)

                while self.huidige_positie <= self.continous_distance:
                    ""
                    #rospy.logwarn(self.huidige_positie)
                rospy.logwarn("transportband op positie")
                self.huidige_positie = 0

                time.sleep(5)


            #controleer stopknop en noodstop
            self.checkStop()
            if self._noodstop == False:
                #Machinevision
                #self.visionpose.position.x = visionfeedback.x
                rospy.loginfo("start vision")
                self.visionEscape = False
                self.bakNaam = ""
                self.sub_vision = rospy.Subscriber('/image_processor/vision_pose',vision_msg, self.callbackVision)
            
            time.sleep(2)
            
            if self.bakNaam == "":
                rospy.loginfo("nothing detected")
            else:
                rospy.loginfo("in break")
                break

        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar boven
            self.manipulator_goal.mode.data = True

            self.manipulator_goal.lineairpose.position.x = 0
            self.manipulator_goal.lineairpose.position.y = 0
            self.manipulator_goal.lineairpose.position.z = 0.05

            self.manipulator_goal.lineairpose.orientation.x = 0
            self.manipulator_goal.lineairpose.orientation.y = 0
            self.manipulator_goal.lineairpose.orientation.z = 0
            self.manipulator_goal.lineairpose.orientation.w = 0
            self.client_manipulator.send_goal(self.manipulator_goal)

            while state_result < self.DONE:
                rospy.logwarn("moving up")

                state_result = self.client_manipulator.get_state()
                rospy.loginfo("state_result: "+str(state_result))
                self.manrate.sleep()

            state_result = self.ACTIVE


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator op positie vision
            self.manipulator_goal.mode.data = True

            self.manipulator_goal.lineairpose.position.x = self.poseX
            self.manipulator_goal.lineairpose.position.y = self.poseY
            self.manipulator_goal.lineairpose.position.z = 0

            self.manipulator_goal.lineairpose.orientation.x = self.poseRX
            self.manipulator_goal.lineairpose.orientation.y = self.poseRY
            self.manipulator_goal.lineairpose.orientation.z = self.poseRZ
            self.manipulator_goal.lineairpose.orientation.w = self.poseRW
            self.client_manipulator.send_goal(self.manipulator_goal)

            while state_result < self.DONE:
                rospy.logwarn("moving to visionfeedback")

                state_result = self.client_manipulator.get_state()
                rospy.loginfo("state_result: "+str(state_result))
                self.manrate.sleep()

            state_result = self.ACTIVE


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar beneden
            self.manipulator_goal.mode.data = True

            self.manipulator_goal.lineairpose.position.x = 0
            self.manipulator_goal.lineairpose.position.y = 0
            self.manipulator_goal.lineairpose.position.z = -0.055

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


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Gripper dicht
            self._gripper_service_response = self._gripper_program('dicht', 1)
            rospy.loginfo("gripper gaat dicht")
            self.gripper_response = self.add_two_ints_client('dicht', 1)
            self.gripper_response = self.add_two_ints_client('dicht', 1)


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar boven
            self.manipulator_goal.mode.data = True

            self.manipulator_goal.lineairpose.position.x = 0
            self.manipulator_goal.lineairpose.position.y = 0
            self.manipulator_goal.lineairpose.position.z = 0.05

            self.manipulator_goal.lineairpose.orientation.x = 0
            self.manipulator_goal.lineairpose.orientation.y = 0
            self.manipulator_goal.lineairpose.orientation.z = 0
            self.manipulator_goal.lineairpose.orientation.w = 0
            self.client_manipulator.send_goal(self.manipulator_goal)

            while state_result < self.DONE:
                rospy.logwarn("moving up")

                state_result = self.client_manipulator.get_state()
                rospy.loginfo("state_result: "+str(state_result))
                self.manrate.sleep()

            state_result = self.ACTIVE


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
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


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar bak 2_4
            self.manipulator_goal.mode.data = False
            self.manipulator_goal.position.data = "bak2_4"
            self.client_manipulator.send_goal(self.manipulator_goal)

            state_result = self.client_manipulator.get_state()

            while state_result < self.DONE:
                rospy.logwarn("moving to home")

                state_result = self.client_manipulator.get_state()
                rospy.loginfo("state_result: "+str(state_result))
                self.manrate.sleep()

            state_result = self.ACTIVE

        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar sorteerpositie
            printtext = "\n \n" + self.bakNaam + "\n \n"
            rospy.logwarn(printtext)
            self.manipulator_goal.mode.data = False
            self.manipulator_goal.position.data = self.bakNaam
            self.client_manipulator.send_goal(self.manipulator_goal)

            state_result = self.client_manipulator.get_state()

            while state_result < self.DONE:
                rospy.logwarn("moving to home")

                state_result = self.client_manipulator.get_state()
                rospy.loginfo("state_result: "+str(state_result))
                self.manrate.sleep()

            state_result = self.ACTIVE

        self.checkStop()
        if self._noodstop == False:
            #Manipulator naar beneden
            self.manipulator_goal.mode.data = True

            self.manipulator_goal.lineairpose.position.x = 0
            self.manipulator_goal.lineairpose.position.y = 0
            self.manipulator_goal.lineairpose.position.z = -0.14

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


        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
            #gripper open
            self._gripper_service_response = self._gripper_program('open', 1)
            rospy.loginfo("gripper gaat open")
            self.gripper_response = self.add_two_ints_client('open', 1)
            self.gripper_response = self.add_two_ints_client('open', 1)

        #controleer stopknop en noodstop
        self.checkStop()
        if self._noodstop == False:
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


        #reset variabelen op het einde van de cyclus.
        self.visionEscape = False



if __name__ == '__main__':
    rospy.init_node('sorteerinstallatie')
    MainProgramClass()
    rospy.spin()
