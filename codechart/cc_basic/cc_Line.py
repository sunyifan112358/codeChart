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
			center = Point(0, 0), 
			style=None
		):
		super(Line, self).__init__(center, style);
		self.path = None;

	def getStyleSetting(self):
		lineStyle = [];
		lineStyle.append(self.style.strokeColor.getPyxColor());
		lineStyle.append(style.linewidth(self.style.strokeWidth));
		lineStyle.append(Style.getPyXLineStyle(self.style.lineStyle));
		if(self.style.useBeginArrow):
			lineStyle.append(
				deco.barrow(
					[
						deco.stroked([color.rgb(0,0,0)]),
						deco.filled([color.rgb(0,0,0)])
					],
					size = self.style.beginArrowSize
				)
			)
		if(self.style.useEndArrow):
			lineStyle.append(
				deco.earrow(
					[
						deco.stroked([color.rgb(0,0,0)]),
						deco.filled([color.rgb(0,0,0)])
					],
					size = self.style.endArrowSize
				)
			)
		return lineStyle

	def draw(self, canvas):
		if self.style.doStroke:
			canvas.stroke(
					self.path,
					self.getStyleSetting()
				)


class StraightLine(Line):
	''' A straight line from point to point'''
	def __init__(
			self, 
			p1 = Point(0, 0),
			p2 = Point(20, 20), 
			style = None
		):
		super(StraightLine, self).__init__(Point.center(p1, p2), style);

		pathitems = [];
		pathitems.append(path.moveto(p1.x, p1.y));
		pathitems.append(path.lineto(p2.x, p2.y));
		self.path = path.path(*pathitems);

class Polyline(Line):

	def __init__(self, *pos):
		super(Polyline, self).__init__(Point.center(*pos));

		pathitems = [];
		pathitems.append(path.moveto(pos[0].x, pos[0].y));
		self.addJointPoint(Point(pos[0].x, pos[0].y));

		for i in range(len(pos)-1):
			pathitems.append( path.lineto(pos[i+1].x, pos[i+1].y) )
			self.addJointPoint( Point(pos[i+1].x, pos[i+1].y));

		self.path = path.path(*pathitems);

	def draw(self, canvas):
		super(Polyline,self).draw(canvas);


class ElbowLine(ComplexShape):
	def __init__(self, firstFoldX, *pos):
		super(ElbowLine, self).__init__(Point.center(*pos));
		corners = []
		corners.append(pos[0]);
		self.addJointPoint(pos[0]);
		foldX = firstFoldX
		for i in range(len(pos)-1):
			p = Point(0,0)
			self.addJointPoint(pos[i+1]);
			if(foldX):
				p = Point(
						pos[i+1].x,
						pos[i].y
						)
			else:
				p = Point(
						pos[i].x,
						pos[i+1].y
						)

				foldX = not foldX;
			corners.append(p)
			self.addJointPoint(p);
		corners.append(pos[-1]);

		self.addShape(
			Polyline( *corners )
		)

		def draw(self, canvas):
			super(ElbowLine, self).draw(canvas);

class TensionCurve(Line):
	'''Curve from serveral points'''
	def __init__(self, style=None, pos=None):
		if pos==None :
			pos = self.getDefaultPoints();
		super(TensionCurve, self).__init__(Point.center(*pos), style);

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
	TensionCurve.preview()
