__all__ = [
	'Shape', 
	'ComplexShape',
	'PrimitiveShape'
]
from pyx import *
from cc_Point import Point
from cc_Plot import Plot
from cc_Style import Style

class Shape(object):
	'''All objects on a plot'''

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
	
	def intersection(self, shape):
		'''Find the intersection points of 2 shapes
		Only check if the input is a Shape'''
		if not isinstance(shape, Shape): 
			raise TypeError("Intersection only accept Shape")
		

	@classmethod
	def preview(cls):
		p = Plot()
		p.addShape(cls())
		p.draw()
		p.savePDF('preview/' + cls.__name__)
		return p

	@classmethod
	def save(cls):
		p = cls.preview()
		p.savePNG('preview/' + cls.__name__)

class PrimitiveShape(Shape):
	'''Primitive shape like line, polygon, ellipse'''
	def __init__(self, center = Point(0, 0), style=None):
		super(PrimitiveShape, self).__init__(center, style = style)
		self.path = None

	def intersection(self, shape):
		'''Find the intersection points of 2 shapes
		if shape is a PrimitiveShape, find intersection, 
		if shape is a ComplexShape, use ComplexShape's correspoding function
		'''
		super(PrimitiveShape, self).intersection(shape)
		if isinstance(shape, PrimitiveShape):
			# Find intersection between primitive and primitive shapes
			return self.PPIntersection(shape)
		elif isinstance(shape, ComplexShape):
			return shape.intersection(self)
	
	def PPIntersection(self, shape):
		if not isinstance(shape, PrimitiveShape):
			raise TypeError("Shape is expected to be a PrimitiveShape");
		ps = self.path.intersect(shape.path)
		points = []
		for p in ps[0]:
			point = self.path.at(p)
			points.append(Point(point[0].t*100, point[1].t*100))
		return points

	def draw(self, canvas):
		super(PrimitiveShape, self).draw(canvas)
		if self.style.doFill:
			canvas.fill(
				self.path,
				[
					self.style.fillColor.getPyxColor()
				]
			)
		if self.style.doStroke:
			canvas.stroke(
				self.path,
				[
					self.style.strokeColor.getPyxColor(),
					style.linewidth(self.style.strokeWidth),
					Style.getPyXLineStyle(self.style.lineStyle)
				]
			)


class ComplexShape(Shape):
	''' Complex shape is a group of primitive or complex shapes '''
	def __init__(self, center=Point(0, 0), style=None):
		super(ComplexShape, self).__init__(center, style = style);
		self.shapes = [];

	def intersection(self, shape):
		'''Find intersections points of 2 shapes'''
		super(ComplexShape, self).intersection(shape)
		points = []
		for s in self.shapes:
			ps = s.intersection(shape)
			if ps != None:
				points += ps
		return points

	def addShape(self, *shapes):
		for shape in shapes:
			self.shapes.append(shape);

	def draw(self, canvas):
		for shape in self.shapes:
			shape.draw(canvas)

class testIntersection(ComplexShape):
	def __init__(self):
		super(testIntersection, self).__init__();
		Style.strokeWidth(0.2);
		e1 = Rectangle(0, 0, 100, 100)
		e2 = Rectangle(0, 75, 200, 200)
		self.addShape(e1, e2)
		ps = e1.intersection(e2)
		for p in ps:
			c = Ellipse(p.x, p.y, 1, 1)
			self.addShape(c)



if __name__ == "__main__":
	from cc_basicShape import *
	testIntersection.preview()
	
