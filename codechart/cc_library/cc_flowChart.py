__all__ = [
	'FC_Process',
	'FC_Decision',
	'FC_Terminator'
];

from cc_basic import *

class FC_Process(ComplexShape):

	def __init__(
				self, 
				x=0, 
				y=0, 
				width=4, 
				height=3, 
				text="Statement"
			):
		super(FC_Process, self).__init__(Point(x, y));

		Style.textHAlign ("CENTER", instance = self.style);

		s = Rectangle(x, y, width, height, style = self.style);
		t = Text(
			text, 
			x, 
			y, 
			width*0.9/self.style.textSize, 
			style = self.style
		);

		self.addShape(s, t);

		self.jointPoints = s.jointPoints

class FC_Decision(ComplexShape):

	def __init__(
					self,
					x = 0,
					y = 0,
					width = 100,
					height = 40,
					text = "Selection",
					textYes = "Yes",
					textYesPos = "BOTTOM",
					textNo = "No",
					textNoPos = "RIGHT"
				):
		super(FC_Decision, self).__init__(Point(x,y));

		self.x = x;
		self.y = y;
		self.width = width;
		self.height = height;

		Style.textHAlign("CENTER", instance = self.style);


		dia = Diamond(x, y, width, height, style=self.style)
		t = Text(text, x, y, width*0.7/self.style.textSize, style=self.style)

		Style.textHAlign("LEFT", instance = self.style);

		if textYesPos != "NONE":
			yP = self.getTextPosPoint(textYesPos);
			tYes = Text(textYes, yP.x, yP.y, style = self.style);
			self.addShape(tYes)

		if textNoPos != "NONE":
			nP = self.getTextPosPoint(textNoPos);
			tNo = Text(textNo, nP.x, nP.y, style = self.style);
			self.addShape(tNo)
		

		self.addShape(dia, t)

		self.jointPoints = dia.jointPoints

	def getTextPosPoint(self, posString):
		shiftFactor = 0.05
		if posString != "NONE":
			if posString == "LEFT":
				Style.textVAlign("BOTTOM", self.style);
				Style.textHAlign("RIGHT", self.style);
				yesX = self.x - self.width/2 - self.width*shiftFactor
				yesY = self.y + self.height*shiftFactor
			elif posString == "RIGHT":
				Style.textVAlign("BOTTOM", self.style);
				Style.textHAlign("LEFT", self.style);
				yesX = self.x + self.width/2 + self.width*shiftFactor
				yesY = self.y + self.height*shiftFactor
			elif posString == "TOP":
				Style.textVAlign("BOTTOM", self.style);
				Style.textHAlign("LEFT", self.style);
				yesX = self.x + self.width*shiftFactor
				yesY = self.y + self.height/2 + self.height*shiftFactor
			elif posString == "BOTTOM":
				Style.textVAlign("TOP", self.style);
				Style.textHAlign("LEFT", self.style);
				yesX = self.x + self.width*shiftFactor
				yesY = self.y - self.height/2 - self.height*shiftFactor
			else:
				raise Exception(
						"Invalid posString: " + posString + 
						" Select from LEFT, RIGHT, TOP, BOTTOM and NONE"
					)
			return Point(yesX, yesY)
		else:
			return None

class FC_Terminator(ComplexShape):
	def __init__(
					self,
					x = 0,
					y = 0,
					width = 4,
					height = 3,
					text = ''
				):
		super(FC_Terminator, self).__init__(Point(x,y));

		self.x = x;
		self.y = y;
		self.width = width;
		self.height = height;

		Style.textHAlign("CENTER", instance = self.style);


		rr = RoundedRect(
				x, 
				y, 
				width, 
				height, 
				border_radius =  height/2.0,
				style=self.style
			)
		t = Text(text, x, y, width*0.8/self.style.textSize, style=self.style)

		self.addShape(rr, t)

		self.jointPoints = rr.jointPoints

if __name__ == '__main__' and __package__ is None:

	FC_Decision.preview();
