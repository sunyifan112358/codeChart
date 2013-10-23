__all__ = [
			'Line',
			'StraightLine',
			'Polyline',
			'ElbowLine'
		]
from pyx import *
from cc_Shape import *
from cc_Point import Point
from cc_Style import *

class Line(Shape):
	def __init__(self, center):
		super(Line, self).__init__(center);

		self.line = None;

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
				self.line,
				self.getStyleSetting()
			)
		

class StraightLine(Line):

	def __init__(self, p1, p2):
		super(StraightLine, self).__init__(Point.center(p1, p2));

		pathitems = [];
		pathitems.append(path.moveto(p1.x, p1.y));
		pathitems.append(path.lineto(p2.x, p2.y));
		self.line = path.path(*pathitems);

	def draw(self, canvas):
		super(StraightLine, self).draw(canvas)
		

class Polyline(Line):

	def __init__(self, *pos):
		super(Polyline, self).__init__(Point.center(*pos));

		pathitems = [];
		pathitems.append(path.moveto(pos[0].x, pos[0].y));
		self.addJointPoint(Point(pos[0].x, pos[0].y));

		for i in range(len(pos)-1):
			pathitems.append( path.lineto(pos[i+1].x, pos[i+1].y) )
			self.addJointPoint( Point(pos[i+1].x, pos[i+1].y));

		self.line = path.path(*pathitems);

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
