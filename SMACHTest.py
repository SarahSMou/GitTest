#!/usr/bin/env python

"""
state_controller.py
The 'main' node in the ROS network - it interfaces with several other nodes to keep track of the
robot's state constantly. This includes the robot's location, the position of its limbs, and how
much load it is carrying.
Completed states: 2, 4, 5, 14, 15, 19, 20, 24, 27(Ri5B)
Tested states: 2, 4
"""

import roslib; roslib.load_manifest('smach_tutorials')
import rospy
import smach
import smach_ros

from std_msgs.msg import String
from std_msgs.msg import Bool
from rdt_localization.msg import *


# STATE 1: Competition starts
class state1(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['s2'])
		self.counter = 0
	def execute(self, userdata):
		print(“State1”)
		return 's2'

# STATE 2: Machine connects to NUC
class state2(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['s3']
	def execute(self, userdata):
		print(“State2”)
		return ‘s3;
				     
# STATE 3: Initiate autonomy program
class state3(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['s4']
	def execute(self, userdata):
            	print(“State3”)
return 's4'
				     
# STATE 4: Deploy Lifting Arms
class state4(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['s5']
	def execute(self, userdata):			

		print(“State4”)
return 's5'

# STATE 5: Nuc localizes robot
class state5(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['s6']
	def execute(self, userdata):
		print(“State5”)
return 's6'   

# STATE 6: Machine moves to digging area
class state6(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['s7']
	def execute(self, userdata):

		print(“State6”)
                	return 's7'		     

# STATE 7: Drum begins to turn
class state7(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['s8']
	def execute(self, userdata):
                	print(“State7”)
return 's8'
				     
# STATE 8: Arms lower drum until contact
class state8(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['s9']
	def execute(self, userdata):
		print(“State8”) 
return 's9'
						     
# STATE 9: Linear actuators push drum down to dig
class state9(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['s10']
	def execute(self, userdata):
		print(“State9”)
return 'state10'
				     
				  	
# STATE 10: LINEAR ACTUATORS LIFT DRUM
class state10(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['s11', 's8'])
	def execute(self, userdata):
                	print(“State10”)
return 's11'
	
# STATE 11: Arms lift drum until it is just below surface level
class state11(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s12']) 
	def execute(self, userdata):
                	print(“State11”)
return 's12'
		
# STATE 12: Move forward until all wheels are in front of the hole
class state12(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s13']) 
	def execute(self, userdata):
                	print(“State12”)
return 's13'


# STATE 13: Lift arms into driving configuration
class state13(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s14']) 
	def execute(self, userdata):
            	print(“State13”)
return 's14'
	
# STATE 14: Drum stops spinning
class state14(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s0', 's15']) 
	def execute(self, userdata):                 		
print(“State14”)
return 's15'
                
            	
# STATE 15: Navigating from digging zone to deposition zone			
class state15(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s16']) 
	def execute(self, userdata):
		print(“State15”)
                	return 's16'
			
# STATE 16: Machine navigates to some distance from depo zone
class state16(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s17']) 
	def execute(self, userdata):
print(“State16”)
            	return 's17'
            	
# STATE 17: Orient with deposition bin
class state17(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s18']) 
	def execute(self, userdata):
		print(“State17”)
		return 's18'
            	
# STATE 18: Arms raise frame to upper limit
class state18(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s19']) 
	def execute(self, userdata):
		print(“State18”)
           		return 's19'
           
# STATE 19: Open storage bin door to release payload
class state19(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s20']) 
	def execute(self, userdata):
		print(“State19”)
                        return 's20'

# STATE 20: Close door
class state20(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s21']) 
	def execute(self, userdata):
		print(“State20”)
            	return 's21'

# STATE 21: Close door
class state21(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s22']) 
	def execute(self, userdata):
		print(“State21”)
return 's22'
            
# STATE 22: Lower linear actuators into driving configuration
class state22(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s23']) 
	def execute(self, userdata):
		print(“State22”)
return 's23'

# STATE 23: Lower arms into driving configuration
class state23(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s24']) 
	def execute(self, userdata):
print(“State23”)
return 's24'
                
# STATE 24: Navigate back/diagonally until April Tags sighted
class state24(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s4']) 
	def execute(self, userdata):
print(“State24”)
return 's4'  

# STATE Ri5B: Error state of obstacle detected
class state27(smach.State):
	def __init__(self):
         	smach.State.__init__(self, outcomes=['s5']) 
	def execute(self, userdata):
          		return 's5'
           

def main():
    # Creating a state machine
    sm = smach.StateMachine(outcomes=['']) # Outcome of State Machine should go here?
    
    # Open Container
    with sm:
	# Add States to the Container
	# smach.StateMachine.add('state0', state0(), transitions = {'s1': 'state1'})
	smach.StateMachine.add('state1', state1(), transitions = {'s2': 'state2'})
	smach.StateMachine.add('state2', state2(), transitions = {'s3': 'state3'})
	smach.StateMachine.add('state3', state3(), transitions = {'s4': 'state4'})
	smach.StateMachine.add('state4', state4(), transitions = {'s5': 'state5'})
	smach.StateMachine.add('state5', state5(), transitions = {'s6': 'state6'})
	smach.StateMachine.add('state6', state6(), transitions = {'s7': 'state7'})
	smach.StateMachine.add('state7', state7(), transitions = {'s8': 'state8'})
	smach.StateMachine.add('state8', state8(), transitions = {'s9': 'state9'})
	smach.StateMachine.add('state9', state9(), transitions = {'s10': 'state10'})
	smach.StateMachine.add('state10', state10(), transitions = {'s11': 'state11', 's8' : 'state8'})
	smach.StateMachine.add('state11', state11(), transitions = {'s12': 'state12'})
	smach.StateMachine.add('state12', state12(), transitions = {'s13': 'state13'})
	smach.StateMachine.add('state13', state13(), transitions = {'s14': 'state14'})
	smach.StateMachine.add('state14', state14(), transitions = {'s0': 'state0', 's15' : 'state15'})
	smach.StateMachine.add('state15', state15(), transitions = {'s16': 'state16'})
	smach.StateMachine.add('state16', state16(), transitions = {'s17': 'state17'})
	# smach.StateMachine.add('state17', state17(), transitions = {'s18': 'state18'})
	smach.StateMachine.add('state18', state18(), transitions = {'s19': 'state19'})
	smach.StateMachine.add('state19', state19(), transitions = {'s20': 'state20'})
	smach.StateMachine.add('state20', state20(), transitions = {'s21': 'state21'})
	smach.StateMachine.add('state21', state21(), transitions = {'s22': 'state22'})
	smach.StateMachine.add('state22', state22(), transitions = {'s23': 'state23'})
	smach.StateMachine.add('state23', state23(), transitions = {'s24': 'state24'})
	smach.StateMachine.add('state24', state24(), transitions = {'s4': 'state4'})
	smach.StateMachine.add('state27', state27(), transitions = {'s5': 'state5'})
				     
    outcome = sm.execute()

    # maybe return statements should be called outcome# instead of state#. Could perhaps lead to an error.
		


if __name__ == '__main__':
    main()
