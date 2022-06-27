#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt8
from hmi.msg import HMI_state

class Arduino_HMI:
    def __init__(self):
        self._programstate = "gereed" # Status van het programma.
        self._programtype = "main" #  Wat onderdeel van het programma data stuurt naar de HMI.
        self._leds = 1 # Variabele dat de leds zal besturen op de shield.
        self._buttons = 0 # Variabele dat aan geeft welke knop is ingedrukt.
        self._stop = False
        self._noodstop = False
        self._stopreset = False
        #self._noodstopreset = False

    # Update de leds op de arduino-shield.
    def send_leds(self):
        pub = rospy.Publisher('/avans/leds/state', UInt8, queue_size=10)
        rate = rospy.Rate(10) # 10hz
        pub.publish(self._leds)
        rate.sleep()

    # Callback functie om informatie van het hoofdprogramma te krijgen.
    def buttonCallback(self, data):
        self._buttons = data.data

    # Callback functie om informatie van het hoofdprogramma te krijgen.
    def hmiCallback(self, data):
        self._stopreset = data.stopreset

        if data.programstate and data.programtype:
            self._programstate = data.programstate
            self._programtype = data.programtype
        elif data.programstate and not data.programtype:
            self._programstate = data.programstate
            self._programtype = ""
        elif not data.programstate and data.programtype:
            self._programstate = ""
            self._programtype = data.programtype

    # Stuurt een message naar de terminal over een storing of fout.
    def errormessage(self, programstate, programtype):
        # String Variabele voor de errormessage.
        errortext = ""
        if programstate == "fout":
            errortext = "fout in [" + programtype + "]"
        elif programstate == "storing":
            errortext = "storing in [" + programtype + "]"

        rospy.loginfo(errortext)

    def Check_buttons(self):
        rospy.Subscriber("/avans/buttons/state", UInt8, self.buttonCallback)
        buttons = self._buttons
        stopreset = self._stopreset
        #noodstopreset = self._noodstopreset

        if buttons == 4:
            self._stop = True
        elif stopreset == True:
            self._stop = False

        if buttons == 8:
            self._noodstop = True
        elif buttons == 12:
            self._noodstop = False

        #elif noodstopreset == True:
        #    self._noodstop = False
        #    self._noodstopreset = False

    # Informatie ophalen en verwerken van het hoofdprogramma.
    def retrieve_program_data(self):
        rospy.Subscriber("/HMI", HMI_state, self.hmiCallback)

        # Vaste variabelen voor de programma status en type.
        programstate = self._programstate 
        programtype = self._programtype
        leds = 0

        #Bepaald de leds van het programma type
        if not programstate or not programtype:
            leds = 3
            errortext = "storing in hmi, geen programma state of type gegeven"
            rospy.loginfo(errortext)
        elif programstate == "gereed":
            leds = 1
        elif programstate == "inbedrijf":
            leds = 2
        elif programstate == "storing":
            leds = 3
        elif programstate == "fout" and programtype == "main":
            leds = 4
        elif programstate == "fout" and programtype == "transportsysteem":
            leds = 8
        elif programstate == "fout" and programtype == "manipulator":
            leds = 16
        elif programstate == "fout" and programtype == "machinevision":
            leds = 32
        elif programstate == "fout" and programtype == "gripper":
            leds = 64
        else:
            leds = 3
            errortext = "storing in hmi, verkeerde programma state: [" +  self._programstate + "]\nprogramma states zijn: gereed, inbedrijf, storing, fout"
            rospy.loginfo(errortext)
    
        # Error message afhandeling
        if programstate == "storing" or programstate == "fout":
            self.errormessage(programstate, programtype)

        # Update leds variabele
        self._leds = leds

    #Published de HMI topic
    def publish_HMItopic(self):
        rate = rospy.Rate(10) # 10hz
        pub = rospy.Publisher('/HMI', HMI_state, queue_size=1)
        msg = HMI_state()
        msg.stop = self._stop
        msg.noodstop = self._noodstop
        #rospy.loginfo(str(msg))
        pub.publish(msg)
        rate.sleep()

# Main programma van de Human Machine Interface programma.
def main():
    rospy.init_node("arduino_connector")
    Arduino_connector.Check_buttons()
    Arduino_connector.publish_HMItopic()
    Arduino_connector.retrieve_program_data()
    Arduino_connector.send_leds()

if __name__ == '__main__':
    Arduino_connector = Arduino_HMI()
    while not rospy.is_shutdown():
        main()
