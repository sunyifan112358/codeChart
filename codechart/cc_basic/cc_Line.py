__all__ = [
	'Line',
	'StraightLine',
	'Polyline',
	'ElbowLine',
	'TensionCurve'
]
from pyx import *
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve
from cc_Shape import *
from cc_Point import Point
from cc_Style import *

class Line(PrimitiveShape):
	''' Abstract class for all lines'''
	def __init__(
			self, 
			style = None,
			center = Point(0, 0), 
		):
		super(Line, self).__init__(style, center);
		self.path = None;

	def getStyleSetting(self):
		lineStyle = [];
		lineStyle.append(self.style.getPyXStrokeColor());
		lineStyle.append(self.style.getPyXStrokeWidth());
		lineStyle.append(self.style.getPyXLineStyle());
		if self.style.getUseBeginArrow():
			lineStyle.append(self.style.getPyXBeginArrow())
		if self.style.getUseEndArrow():
			lineStyle.append(self.style.getPyXEndArrow())
		return lineStyle

	def draw(self, canvas):
		if self.style.getDoStroke():
			canvas.stroke(
					self.path,
					self.getStyleSetting()
				)


class StraightLine(Line):
	''' A straight line from point to point'''
	def __init__(
			self, 
			style = None,
			p1 = Point(0, 0),
			p2 = Point(20, 20)
		):
		super(StraightLine, self).__init__(style, Point.center(p1, p2));

		pathitems = [];
		pathitems.append(path.moveto(p1.x, p1.y));
		pathitems.append(path.lineto(p2.x, p2.y));
		self.path = path.path(*pathitems);

class Polyline(Line):

	def __init__(self, style = None, pos = None):
		if pos == None:
			pos = self.getDefaultPoints();
		super(Polyline, self).__init__(style, Point.center(*pos));

		pathitems = [];
		pathitems.append(path.moveto(pos[0].x, pos[0].y));
		self.addJointPoint(Point(pos[0].x, pos[0].y));

		for i in range(len(pos)-1):
			pathitems.append( path.lineto(pos[i+1].x, pos[i+1].y) )
			self.addJointPoint( Point(pos[i+1].x, pos[i+1].y));

		self.path = path.path(*pathitems);
	
	def getDefaultPoints(self):
		points = (
				Point(0, 0),
				Point(20, 30),
				Point(50, -15),
				Point(-30, 70)
			)
		return points

	def draw(self, canvas):
		super(Polyline,self).draw(canvas);


class ElbowLine(ComplexShape):
	'''ElbowLine'''
	def __init__(
			self, 
			style = None, 
			pos = None,
			firstFold = 'x'
		):
		if pos == None:
			pos = self.getDefaultPoints();
		super(ElbowLine, self).__init__(style, Point.center(*pos));
		corners = []
		corners.append(pos[0]);
		self.addJointPoint(pos[0]);
		nextFold = firstFold
		for i in range(len(pos)-1):
			p = Point(0,0)
			self.addJointPoint(pos[i+1]);
			if nextFold == 'x':
				p = Point(
						pos[i+1].x,
						pos[i].y
					)
				nextFold = 'y'
			elif nextFold == 'y':
				p = Point(
						pos[i].x,
						pos[i+1].y
						)
				nextFold = 'x'
			else:
				raise ValueError("First fold can only be 'x' or 'y'") 
			corners.append(p)
			self.addJointPoint(p);
		corners.append(pos[-1]);

		self.addShape(
			Polyline(self.style,  corners)
		)
		
	def getDefaultPoints(self):
		points = (
				Point(0, 0),
				Point(30, -30),
				Point(60, -60), 
				Point(100, -0) 
			)
		return points

	def draw(self, canvas):
		super(ElbowLine, self).draw(canvas);

class TensionCurve(Line):
	'''Curve from serveral points'''
	def __init__(self, style=None, pos=None):
		if pos==None :
			pos = self.getDefaultPoints();
		super(TensionCurve, self).__init__(style, Point.center(*pos));

		pathitems = []
		i = 0
		for p in pos:
			if i == 0:
				pathitems.append(beginknot(*pos[0].toTuple()))
			elif i == len(pos) - 1:
				pathitems.append(tensioncurve())
				pathitems.append(endknot(*pos[i].toTuple()))
			else:
				pathitems.append(tensioncurve())
				pathitems.append(smoothknot(*pos[i].toTuple()))
			i += 1
		self.path = metapost.path.path(pathitems)

	def getDefaultPoints(self):
		'''generate defult points'''
		return (
				Point(0, 0), 
				Point(50, 40),
				Point(60, 70),
				Point(0, -20)
			)

if __name__ == "__main__":
	StraightLine.preview()
	Polyline.preview()
	ElbowLine.preview()
	TensionCurve.preview()
