#!/usr/bin/env python

import rospy
from robotiq_2f_gripper_control.msg import Robotiq2FGripper_robot_output
from robotiq_2f_gripper_control.msg import _Robotiq2FGripper_robot_input  as inputMsg
from gripper_besturing.srv import gripperServiceMessage,gripperServiceMessageResponse
import roslib; roslib.load_manifest('robotiq_2f_gripper_control')

def gripper_prog(req):
	pub = rospy.Publisher('/Robotiq2FGripperRobotOutput', Robotiq2FGripper_robot_output, queue_size = 1)
	publish_var = Robotiq2FGripper_robot_output()
	rate = rospy.Rate(0.5)

	# Eerste keer als programma opgestart moet worden, dan moet er een 'open/dicht 0' worden opgegeven!!!
	count_in_sec = 0
	wait_for_active = req.gripper_opstarten
	while wait_for_active == 0 and count_in_sec <= 2:
		publish_var.rACT = 0
		pub.publish(publish_var)
		rate.sleep()
		count_in_sec += 1
		print(count_in_sec)

	# Bepalen van waarden voor publish
	if req.open_of_dicht_gripper == 'dicht':
		publish_var.rPR = 255 # 0 is open, 255 is dicht
		print('[systeem] Gripper gaat dicht.')
	else:
		publish_var.rPR = 0 # 0 is open, 255 is dicht
		print('[systeem] Gripper gaat open.')
	# Voorbeeld van (op volgorde) positie, snelheid, kracht, go to, en activeren
	publish_var.rSP = 255
	publish_var.rFR = 90
	publish_var.rGTO = 1
	publish_var.rACT = 1
	pub.publish(publish_var) 	# Kan zijn dat publish het niet in een keer doet, dan moet de service nog een keer opgevraagd worden,
								# wordt gefixed door de 'open/dicht 0' op te geven de eerste keer (while loop, regel 16)

	# Wachten totdat alle input berichten gelezen zijn, daarna nog een rate.sleep() om itteratie fout te voorkomen.
	while subscriber_gOBJ == 0:
		pass
	rate.sleep()

	# Passed_or_failed bepalen
	error_bericht = 'Gripper NOT at requested position.'
	passed_or_failed = False
	if subscriber_gOBJ == 2 and count_in_sec <= 5 or subscriber_gOBJ == 3 and count_in_sec <= 5:
		passed_or_failed = True
		error_bericht = ''

	# Object_found bepalen
	object_found = False
	if subscriber_gOBJ == 1 or subscriber_gOBJ == 2:
		object_found = True

	# Error bericht bepalen
	if subscriber_gOBJ == 0:
		error_bericht += 'Itteration mistake, please run your command again.'
	elif subscriber_gFLT == 0 and passed_or_failed == True:
		error_bericht += ' No error to display.'
	elif subscriber_gFLT == 0 and passed_or_failed == False and object_found == True:
		error_bericht += ' Object detected when opening'
	elif subscriber_gFLT >=1 and subscriber_gFLT <= 7:
		error_bericht += ' Gripper has not been activated, input "open 0". '
	elif subscriber_gFLT >= 8:
		error_bericht += ' Major fault, please look up the gripper manual en check the /Robotiq2FGripperRobotInput topic.'

	# Response terug sturen
	response = gripperServiceMessageResponse(passed_or_failed, object_found, subscriber_gFLT, error_bericht)
	return response

def sub_testing(input):
	# Globale variabelen maken zodat deze kunnen worden gebruikt in def gripper_prog()
	global subscriber_gOBJ
	global subscriber_gACT
	global subscriber_gFLT
	subscriber_gFLT = input.gFLT	# Fout meldingen
	subscriber_gACT = input.gACT	# Activatie
	subscriber_gOBJ = input.gOBJ	# Doel/resultaat -> 0 = bezig, 1 = contact tijdens openen, 2 = contact tijdens dichtgaan, 3 = at req pos
	pass

def run_subscriber():
	sub = rospy.Subscriber('/Robotiq2FGripperRobotInput', inputMsg.Robotiq2FGripper_robot_input, sub_testing)

def run_service():
    rospy.init_node('bestruring_gripper_node')
    s = rospy.Service('gripper_open_of_dicht_doen', gripperServiceMessage, gripper_prog)
    print("Ready to take gripper command.")
    rospy.spin()

if __name__ == '__main__':
	subscriber_gACT = 0
	subscriber_gOBJ = 0
	subscriber_gFLT = 255
	run_subscriber()
	run_service()
