__all__ = ['Text']
from pyx import *
from cc_Plot import *
from cc_Shape import Shape
from cc_Style import *
from cc_Point import *

class Text(Shape):

	def __init__(self, latexString, x, y, parWidth = None, style = None):
		super(Text, self).__init__(Point(x, y), style);
		if parWidth:
			self.parbox = text.parbox(parWidth);
		else:
			self.parbox = None
		self.latexString = latexString;
		self.x = x;
		self.y = y;

	def draw(self, canvas):
		canvas.text(
			self.x, 
			self.y, 
			self.latexString, 
			self.getStyleSetting()
		)

	def getStyleSetting(self):
		styleSetting = []
		if self.parbox:
			styleSetting.append(self.parbox)
		styleSetting.append(Style.getPyXHAlign(self.style.textHAlign))
		styleSetting.append(Style.getPyXVAlign(self.style.textVAlign))
		styleSetting.append(Style.getPyXHFlush(self.style.textHFlush))
		#styleSetting.append(Style.getPyXTextSize(self.style.textSize))
		styleSetting.append(trafo.scale(sx=self.style.textSize))
		return styleSetting



	




