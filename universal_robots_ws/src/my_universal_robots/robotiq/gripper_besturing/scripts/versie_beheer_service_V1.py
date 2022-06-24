#!/usr/bin/python3

import rospy
from robotiq_2f_gripper_control.msg import Robotiq2FGripper_robot_output
from robotiq_2f_gripper_control.msg import _Robotiq2FGripper_robot_input  as inputMsg
from gripper_besturing.srv import gripperServiceMessage,gripperServiceMessageResponse
import roslib; roslib.load_manifest('robotiq_2f_gripper_control')

# Klasse aanmaken (met sub en pub)
class MyClass:
	def __init__(self, req):
		self.pub = rospy.Publisher('/Robotiq2FGripperRobotOutput', Robotiq2FGripper_robot_output, queue_size = 1)
		self.sub = rospy.Subscriber('/Robotiq2FGripperRobotInput', inputMsg.Robotiq2FGripper_robot_input, self.gripper_movement)
		self.open_of_dicht = req.open_of_dicht_gripper
		self.stoppen_sub = 0
		self.gripper_init = req.gripper_opstarten

	def gripper_movement(self, input):
		if self.stoppen_sub == 0:
			response = gripperServiceMessageResponse()
			print('--------------------------------')
			publish_var = Robotiq2FGripper_robot_output()
			rate = rospy.Rate(2)

			if self.gripper_init == 0:
				#Loop voor deactiveren gripper, programma wacht tot rACT op 0 staat. -> niet nodig als er gripper activatie wordt gebruikt!
				#Kan ook worden gefixed door een int mee te vragen met de service
				wait_for_active = 0
				while wait_for_active == 0:
					publish_var.rACT = 0
					wait_for_active = input.gACT
					self.pub.publish(publish_var)
					rate.sleep()
				print('[Systeem] Gripper is geactiveerd.')

			if self.open_of_dicht == 'dicht':
				publish_var.rPR = 255 # 0 is open, 255 is dicht
				print('[systeem] Gripper gaat dicht.')
			else:
				publish_var.rPR = 0 # 0 is open, 255 is dicht
				print('[systeem] Gripper gaat open.')

			# Voorbeeld van (op volgorde) positie, snelheid, kracht en GoTo.
			publish_var.rSP = 255
			publish_var.rFR = 255
			publish_var.rGTO = 1

			wait_for_rACT = 0
			while wait_for_rACT == 0:
				publish_var.rACT = 1		# rACT en publish moeten in een while loop staan ??
				self.pub.publish(publish_var)
				wait_for_rACT = input.gACT

			# stoppen van de subscriber
			self.stoppen_sub = 1
			response = gripperServiceMessageResponse(True,2,"Dit werkt niet zoals verwacht!")
			return response
		else:
			# ivm foutmelding
			pass

def run_service():
    rospy.init_node('bestruring_gripper_node')
    s = rospy.Service('gripper_open_of_dicht_doen', gripperServiceMessage, MyClass)
    print("Ready to take gripper command.")
    rospy.spin()

if __name__ == '__main__':
	run_service()
## Hieronder notes:
# De gripper gaat open en dicht, krijgt error message voor response vd klasse.
