#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt8
from hmi.msg import HMI_state

class Arduino_HMI:
    def __init__(self):
        self._programstate = "gereed" # Status van het programma.
        self._programtype = "main" #  Wat onderdeel van het programma data stuurt naar de HMI.
        self._leds = 1 # Variabele dat de leds zal besturen op de shield.

    # Update de leds op de arduino-shield.
    def send_leds(self):
        pub = rospy.Publisher('/avans/leds/state', UInt8, queue_size=10)
        rate = rospy.Rate(10) # 10hz
        pub.publish(self._leds)
        rate.sleep()

    # Callback functie om informatie van het hoofdprogramma te krijgen.
    def ledCallback(self, data):
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

    # Informatie ophalen en verwerken van het hoofdprogramma.
    def retrieve_program_data(self):
        rospy.Subscriber("/HMI", HMI_state, self.ledCallback)

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

    def publish_node(self):
        rate = rospy.Rate(10) # 10hz
        pub = rospy.Publisher('/HMI', HMI_state, queue_size=10)
        pub.publish()
        rate.sleep()

# Main programma van de Human Machine Interface programma.
def main():
    rospy.init_node("arduino_connector")
    Arduino_connector.publish_node()
    Arduino_connector.retrieve_program_data()
    Arduino_connector.send_leds()

if __name__ == '__main__':
    Arduino_connector = Arduino_HMI()
    while not rospy.is_shutdown():
        main()