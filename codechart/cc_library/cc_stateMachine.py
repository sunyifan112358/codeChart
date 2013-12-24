__all__ = [
	'SM_State',
	'SM_Transition',
]

from codechart.cc_basic import *
import math

class SM_State(ComplexShape):
	'''States in state machine'''	
	def __init__(
			self,
			style = None, 
			x = 0, y = 0, 
			radius = 30,
			text = "IDLE"
		):
		super(SM_State, self).__init__(style, Point(x, y));

		self.style = self.style \
					.textHAlign("CENTER") \
					.textHFlush("CENTER") \
					.textVAlign("MIDDLE")

		e = Ellipse(self.style, x, y, radius);
		t = Text(
				self.style,
				x, y, 
				1.8 * radius,
				text
			);

		self.addShape(e, t);
		self.jointPoints = e.jointPoints

class SM_Transition(ComplexShape):
	''' A state transition line from state1 to state2'''
	def __init__(
			self,
			style = None,
			state1 = None, state2 = None,
			transitionCase = "Something",
			midPointModification = Point(0, 10),
			textPointModification = Point(0, 3),
			textRotate = None,
		):
		
		if state1 == None:
			state1 = SM_State(style, 0, 0, 30, "IDLE")
		if state2 == None:
			state2 = SM_State(style, 100, 100, 30, "IDLE2")
		if textRotate == None:
			textRotate = self.getTextRotate(state1.center, state2.center)

		midPoint = Point.center( state1.center, state2.center ); 
		midPointModified = midPoint.move(midPointModification)
		textPoint = midPointModified.move(textPointModification)

		super(SM_Transition, self).__init__(style, midPointModified)

		l1 = StraightLine(self.style, state1.center, midPointModified)
		l2 = StraightLine(self.style, state2.center, midPointModified)
	
		#self.addShape(state1, state2, l1, l2)
	
		p1 = l1.intersection(state1)[0]
		p2 = l2.intersection(state2)[0]
		
	
		curve = TensionCurve( self.style, (p1, midPointModified, p2) )
		self.style = self.style \
					.textVAlign("BOTTOM") \
					.textHAlign("CENTER") \
					.textHFlush("CENTER")
		text = Text(
				self.style.rotate(textRotate),
				textPoint.x,
				textPoint.y,
				None, 
				transitionCase
			)
		self.addShape(curve, text)

	def getTextRotate(self, p1, p2):

		xDiff = p2.x*1.0 - p1.x
		yDiff = p2.y*1.0 - p1.y

		degree =  math.degrees(math.atan(yDiff/xDiff))
		return degree

if __name__ == "__main__":
	SM_State.preview();
	SM_Transition.preview()
