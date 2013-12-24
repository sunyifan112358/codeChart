from codechart import *

class stateMachineTransmitter(ComplexShape):
	
	def __init__(
			self,
			x = 0, y = 0,
		):
		super(stateMachineTransmitter, self).__init__(
				None,
				Point(x, y)
			)
		
		self.style = self.style \
					 .textSize(24) \
					 .endArrow(5)
		stateRadius = 30;

		s1 = SM_State(
				self.style,
				0, 0, stateRadius, 
				'IDLE'
			);
		s2 = SM_State(
				self.style,
				130, -60, stateRadius, 
				'Detect preamble'
			); 
		s3 = SM_State(
				self.style,
				80, -180, stateRadius, 
				'Find data channel'
			);
		s4 = SM_State(
				self.style,
				-40, -170, stateRadius, 
				'Switch RX channel'
			);
		s5 = SM_State(
				self.style,
				-90, -80, stateRadius, 
				'Receive and send body to host',
			);

		t1 = SM_Transition(
				self.style,
				s1, s2, 
				"", 
				Point(0, 30), 
				Point(0, 5)
			)

		t2 = SM_Transition(
				self.style,
				s2, s1, 
				"No preamble",
				Point(0, -20),
				Point(-10, -5)
			)
		t3 = SM_Transition(
				self.style,
				s2, s3,
				"Find preamble",
				Point(20, 10),
				Point(10,-20)
			)
		t4 = SM_Transition(
				self.style,
				s3, s4,
				"",
				Point(0, -10),
				Point(0, 0)
			)
		t5 = SM_Transition(
				self.style,
				s4, s5,
				"",
				Point(-10, -10)
			)
		t6 = SM_Transition(
				self.style,
				s5, s1,
				"",
				Point(-20, 0)
			)
		
		self.addShape(s1, s2, s3, s4, s5);
		self.addShape(t1, t2, t3, t4, t5, t6)
	
if __name__ == '__main__':
	stateMachineTransmitter.save();

