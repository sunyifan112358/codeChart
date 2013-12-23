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
			x = 0, y = 0, 
			radius = 30,
			text = "IDLE",
			style = None
		):
		super(SM_State, self).__init__(Point(x, y), style);

		Style.textHAlign("CENTER", instance = self.style)
		Style.textHFlush("CENTER", instance = self.style)
		Style.textVAlign("MIDDLE", instance = self.style)

		e = Ellipse(x, y, radius, style = self.style);
		t = Text(
				text, x, y, 0,
				radius*2*0.8, style = self.style
			);

		self.addShape(e, t);
		self.jointPoints = e.jointPoints

class SM_Transition(ComplexShape):
	''' A state transition line from state1 to state2'''
	def __init__(
			self,
			state1 = None, state2 = None,
			transitionCase = "Something",
			midPointModification = Point(0, 10),
			textPointModification = Point(0, 3),
			textRotate = None,
			style = None
		):
		
		if state1 == None:
			state1 = SM_State(0, 0, 30, "IDLE")
		if state2 == None:
			state2 = SM_State(100, 100, 30, "IDLE2")
		if textRotate == None:
			textRotate = self.getTextRotate(state1.center, state2.center)

		midPoint = Point.center( state1.center, state2.center ); 
		midPointModified = midPoint.move(midPointModification)
		textPoint = midPointModified.move(textPointModification)

		super(SM_Transition, self).__init__(midPointModified, style)

		l1 = StraightLine(state1.center, midPointModified)
		l2 = StraightLine(state2.center, midPointModified)
		
		p1 = l1.intersection(state1)[0]
		p2 = l2.intersection(state2)[0]

		curve = TensionCurve( self.style, (p1, midPointModified, p2) )
		Style.textVAlign("BOTTOM", self.style)
		Style.textHAlign("CENTER", self.style)
		Style.textHFlush("CENTER", self.style)
		text = Text(
				transitionCase, 
				textPoint.x,
				textPoint.y,
				textRotate,
				None,
				self.style
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
