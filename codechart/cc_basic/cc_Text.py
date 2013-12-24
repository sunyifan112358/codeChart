__all__ = ['Text']
from pyx import *
from cc_Plot import *
from cc_Shape import Shape
from cc_Style import *
from cc_Point import *

class Text(Shape):

	def __init__(
			self, 
			style = None,
			x = 0, y = 0, 
			width = 20,
			string = r"$\int_{-\infty}^{\infty}tdt$"
		):
		super(Text, self).__init__(style, Point(x, y));
		if width:
			self.parbox = text.parbox(width/self.style.getTextSize());
		else:
			self.parbox = None
		self.string = string;
		self.x = x;
		self.y = y;

	def draw(self, canvas):
		canvas.text(
			self.x, 
			self.y, 
			self.string, 
			self.getStyleSetting()
		)

	def getStyleSetting(self):
		styleSetting = []
		if self.parbox:
			styleSetting.append(self.parbox)
		styleSetting.append(self.style.getPyXHAlign())
		styleSetting.append(self.style.getPyXVAlign())
		styleSetting.append(self.style.getPyXHFlush())
		styleSetting.append(self.style.getPyXTextSize())
		styleSetting.append(self.style.getPyXRotate())
		return styleSetting

if __name__ == "__main__":
	Text.preview();
