__all__ = [
	'FC_Process',
	'FC_Decision',
	'FC_Terminator'
];

from codechart.cc_basic import *

class FC_Process(ComplexShape):

	def __init__(
				self, 
				style = None,
				x=0, y=0, 
				width=40, height=30, 
				text="Statement",
			):
		super(FC_Process, self).__init__(style, Point(x, y));

		self.style = self.style \
					.textHAlign("CENTER") \
					.textHFlush("CENTER") \
					.textVAlign("MIDDLE")

		s = Rectangle(
				self.style, 
				x, y, 
				width, height
			);
		t = Text(
				self.style,
				x, y, 
				width * 0.9, 
				text
			)

		self.addShape(s, t);
		self.jointPoints = s.jointPoints

class FC_Decision(ComplexShape):

	def __init__(
				self,
				style = None, 
				x = 0, y = 0,
				width = 40, height = 30,
				text = "Selection",
				textYes = "Yes", textYesPos = "BOTTOM",
				textNo = "No", textNoPos = "RIGHT",
			):
		super(FC_Decision, self).__init__(style, Point(x,y));

		self.x = x;
		self.y = y;
		self.width = width;
		self.height = height;

		self.style = self.style \
					.textHAlign("CENTER") \
					.textHFlush("CENTER") \
					.textVAlign("MIDDLE")

		dia = Diamond(self.style, x, y, width, height)
		t = Text(
				self.style,
				x, y, 
				width*0.7, 
				text
			)

		self.style = self.style.textHAlign("LEFT");

		if textYesPos != "NONE":
			yP = self.getTextPosPoint(textYesPos);
			tYes = Text(
					self.style, 
					yP.x, yP.y,
					None,
					textYes
				);
			self.addShape(tYes)

		if textNoPos != "NONE":
			nP = self.getTextPosPoint(textNoPos);
			tNo = Text(
					self.style,
					nP.x, nP.y,
					None,
					textNo
				);
			self.addShape(tNo)

		self.addShape(dia, t)

		self.jointPoints = dia.jointPoints

	def getTextPosPoint(self, posString):
		if posString != "NONE":
			shift = 0.1 * self.style.getTextSize()
			if posString == "LEFT":
				self.style = self.style \
						.textVAlign("BOTTOM") \
						.textHAlign("RIGHT")
				yesX = self.x - self.width/2 + shift
				yesY = self.y + shift
			elif posString == "RIGHT":
				self.style = self.style \
						.textVAlign("BOTTOM") \
						.textHAlign("LEFT")
				yesX = self.x + self.width/2 + shift
				yesY = self.y + shift
			elif posString == "TOP":
				self.style = self.style \
						.textVAlign("BOTTOM") \
						.textHAlign("LEFT")
				yesX = self.x + shift
				yesY = self.y + self.height/2 + shift
			elif posString == "BOTTOM":
				self.style = self.style \
							.textVAlign("TOP") \
							.textHAlign("LEFT") 
				yesX = self.x + shift
				yesY = self.y - self.height/2 - shift
			else:
				raise ValueError(
						"Invalid posString: " + posString + 
						" Select from LEFT, RIGHT, TOP, BOTTOM and NONE"
					)
			return Point(yesX, yesY)
		else:
			return None

class FC_Terminator(ComplexShape):
	def __init__(
				self,
				style = None,
				x = 0, y = 0,
				width = 40, height = 30,
				text = r'BEGIN',
			):
		super(FC_Terminator, self).__init__(style, Point(x,y));

		self.x = x;
		self.y = y;
		self.width = width;
		self.height = height;

		self.style = self.style \
					.textHAlign("CENTER") \
					.textHFlush("CENTER") \
					.textVAlign("MIDDLE")

		rr = RoundedRect(
				self.style,
				x, y, 
				width, 
				height, 
				border_radius =  height/2.0,
			)
		t = Text(
				self.style,
				x, y, width*0.8, 
				text
			)

		self.addShape(rr, t)

		self.jointPoints = rr.jointPoints

if __name__ == "__main__":
	FC_Process.preview()
	FC_Terminator.preview()
	FC_Decision.preview()
