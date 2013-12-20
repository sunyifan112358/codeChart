__all__ = ['Shape', 'ComplexShape'];
from pyx import *
from cc_Point import Point
from cc_Plot import Plot
from cc_Style import Style

class Shape(object):

	def __init__(self, center=Point(0,0), style = None):
		self.center = center;
		self.jointPoints = [];
		if not style:
			self.style = Style.getSnapshot()
		else:
			self.style = Style.getSnapshot(style)
	
	def addJointPoint(self, point):
		self.jointPoints.append(point);

	def draw(self, canvas, showJointPoints=False):
		if(showJointPoints):
			for jointPoint in self.jointPoints:
				canvas.stroke(
					path.circle(
						jointPoint.x,
						jointPoint.y,
						0.1
					),
				)

	@classmethod
	def preview(cls):
		p = Plot();
		p.addShape(cls());
		p.draw();
		p.save('preview/' + cls.__name__);

class ComplexShape(Shape):
	''' Complex shape is a group of primitive or complex shapes '''
	def __init__(self, center, style=None):
		super(ComplexShape, self).__init__(center, style = style);
		self.shapes = [];
		if not style:
			self.style = Style.getSnapshot()
		else:
			self.style = Style.getSnapshot(style)

	def addShape(self, *shapes):
		for shape in shapes:
			self.shapes.append(shape);

	def draw(self, canvas):
		for shape in self.shapes:
			shape.draw(canvas)
		showJointPoints = False
		if(showJointPoints):
			for jointPoint in self.jointPoints:
				canvas.text(
					jointPoint.x, 
					jointPoint.y, 
					str(self.jointPoints.index(jointPoint)),
					[
						text.halign.boxcenter,
						text.valign.middle,
						text.size(-3)
					]
				)
				

if __name__ == "__main":
	pass
