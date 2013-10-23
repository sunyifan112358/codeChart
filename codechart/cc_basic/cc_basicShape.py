__all__ = [
	'Ellipse',
	'Polygon',
	'Diamond',
	'Rectangle',
	'RoundedRect'
]

from pyx import *
import math
from cc_Point import Point
from cc_Shape import *
from cc_Style import *

class Ellipse(Shape):

	def __init__(self, x, y, r1, r2, degree):
		super(Ellipse, self).__init__(Point(x, y));
		self.x = x;
		self.y = y;
		self.r1 = r1;
		self.r2 = r2;
		self.degree = degree;

		self.addJointPoint(Point(x-r1, y));
		self.addJointPoint(Point(x, y-r2));
		self.addJointPoint(Point(x+r1, y));
		self.addJointPoint(Point(x, y+r2));



	def draw(self, canvas):
		super(Ellipse,self).draw(canvas);
		circle = path.circle(0,0,1);
		if self.style.doFill:
			canvas.fill(
				circle, 
				[
					trafo.scale(sx=self.r1, sy=self.r2), 
					trafo.rotate(self.degree),
					trafo.translate(self.x, self.y),
					self.style.fillColor.getPyxColor()
				]
			)
		if self.style.doStroke:
			canvas.stroke( 
				circle, 
				[
					trafo.scale(sx=self.r1, sy=self.r2), 
					trafo.rotate(self.degree),
					trafo.translate(self.x, self.y),
					self.style.strokeColor.getPyxColor(),
					style.linewidth(self.style.strokeWidth),
					Style.getPyXLineStyle(self.style.lineStyle)
				]
			)
		

class Polygon(Shape):

	def __init__(self, *pos):
		super(Polygon, self).__init__(Point.center(*pos));

		pathitems = [];
		pathitems.append(path.moveto(pos[0].x, pos[0].y));
		self.addJointPoint(Point(pos[0].x, pos[0].y));

		for i in range(len(pos)-1):
			pathitems.append( path.lineto(pos[i+1].x, pos[i+1].y) )
			self.addJointPoint(Point(pos[i+1].x, pos[i+1].y));

		pathitems.append(path.closepath())

		self.poly = path.path(*pathitems);	

	def draw(self, canvas):
		super(Polygon,self).draw(canvas);
		if self.style.doFill:
			canvas.fill(
				self.poly,
				[
					self.style.fillColor.getPyxColor()
				]
			)
		if self.style.doStroke:
			canvas.stroke(
				self.poly,
				[
					self.style.strokeColor.getPyxColor(),
					style.linewidth(self.style.strokeWidth),
					Style.getPyXLineStyle(self.style.lineStyle)
				]
			)

class Diamond(ComplexShape):
	def __init__(self, x, y, width, height, style=None):
		super(Diamond, self).__init__(Point(x, y), style);

		p1 = Point(x-width/2.0, y);
		p2 = Point(x, y-height/2.0);
		p3 = Point(x+width/2.0, y);
		p4 = Point(x, y+height/2.0);

		self.addJointPoint(p1);
		self.addJointPoint(p2);
		self.addJointPoint(p3);
		self.addJointPoint(p4);

		self.addJointPoint(Point.center(p1, p2));
		self.addJointPoint(Point.center(p2, p3));
		self.addJointPoint(Point.center(p3, p4));
		self.addJointPoint(Point.center(p1, p4));

		polygon = Polygon(p1, p2, p3, p4);
		self.addShape(polygon);

	def draw(self, canvas):
		super(Diamond, self).draw(canvas);


class Rectangle(ComplexShape):
	def __init__(self, x, y, width, height, style = None):
		super(Rectangle, self).__init__(Point(x, y), style = style);
		p1 = Point(x-width/2.0, y-height/2.0);
		p2 = Point(x+width/2.0, y-height/2.0);
		p3 = Point(x+width/2.0, y+height/2.0);
		p4 = Point(x-width/2.0, y+height/2.0);

		self.addJointPoint(p1);
		self.addJointPoint(p2);
		self.addJointPoint(p3);
		self.addJointPoint(p4);
		self.addJointPoint(Point.center(p1, p2));
		self.addJointPoint(Point.center(p2, p3));
		self.addJointPoint(Point.center(p3, p4));
		self.addJointPoint(Point.center(p1, p4));

		polygon = Polygon(p1, p2, p3, p4);
		self.addShape(polygon);

	def draw(self, canvas):
		super(Rectangle, self).draw(canvas);

class RoundedRect(Shape):
	def __init__(self, x, y, width, height, border_radius = 0.5, style = None):
		super(RoundedRect, self).__init__(Point(x,y), style = style)
		p1 = Point(x-width/2.0, y-height/2.0);
		p2 = Point(x+width/2.0, y-height/2.0);
		p3 = Point(x+width/2.0, y+height/2.0);
		p4 = Point(x-width/2.0, y+height/2.0);

		self.addJointPoint(Point.center(p1, p2));
		self.addJointPoint(Point.center(p2, p3));
		self.addJointPoint(Point.center(p3, p4));
		self.addJointPoint(Point.center(p1, p4));

		p1_r1 = Point(
					p1.x,
					p1.y+border_radius
				)
		p1_r2 = Point(
					p1.x,
					p1.y + 1/2.0*border_radius
				)
		p1_r3 = Point(
					p1.x + 1/2.0*border_radius,
					p1.y
				)
		p1_r4 = Point(
					p1.x+border_radius,
					p1.y
				)
		

		p2_r1 = Point(
					p2.x - border_radius,
					p2.y
				)
		p2_r2 = Point(
					p2.x - 1/2.0*border_radius,
					p2.y
				)
		p2_r3 = Point(
					p2.x ,
					p2.y + 1/2.0*border_radius
				)
		p2_r4 = Point(
					p2.x,
					p2.y + border_radius
				)

		p3_r1 = Point(
					p3.x ,
					p3.y - border_radius
				)
		p3_r2 = Point(
					p3.x ,
					p3.y - 1/2.0*border_radius
				)
		p3_r3 = Point(
					p3.x - 1/2.0*border_radius,
					p3.y 
				)
		p3_r4 = Point(
					p3.x - border_radius,
					p3.y 
				)

		p4_r1 = Point(
					p4.x + border_radius,
					p4.y
				)
		p4_r2 = Point(
					p4.x + 1/2.0*border_radius,
					p4.y 
				)
		p4_r3 = Point(
					p4.x ,
					p4.y - 1/2.0*border_radius
				)
		p4_r4 = Point(
					p4.x ,
					p4.y - border_radius
				)

		pathitems = [];
		pathitems.append( path.moveto(p1_r1.x, p1_r1.y) )
		pathitems.append( 
			path.curveto(p1_r2.x, p1_r2.y, p1_r3.x, p1_r3.y, p1_r4.x, p1_r4.y) 
		);

		pathitems.append( path.lineto(p2_r1.x, p2_r1.y) );
		pathitems.append( 
			path.curveto(p2_r2.x, p2_r2.y, p2_r3.x, p2_r3.y, p2_r4.x, p2_r4.y) 
		);

		pathitems.append( path.lineto(p3_r1.x, p3_r1.y) );
		pathitems.append( 
			path.curveto( p3_r2.x, p3_r2.y, p3_r3.x, p3_r3.y, p3_r4.x, p3_r4.y) 
		);

		pathitems.append( path.lineto(p4_r1.x, p4_r1.y) );
		pathitems.append( 
			path.curveto( p4_r2.x, p4_r2.y, p4_r3.x, p4_r3.y, p4_r4.x, p4_r4.y) 
		);


		pathitems.append( path.closepath() );
		self.line = path.path( *pathitems );

	def draw(self,canvas):
		super(RoundedRect,self).draw(canvas);
		if self.style.doFill:
			canvas.fill(
				self.line,
				[
					self.style.fillColor.getPyxColor()
				]
			)
		if self.style.doStroke:
			canvas.stroke(
				self.line,
				[
					self.style.strokeColor.getPyxColor(),
					style.linewidth(self.style.strokeWidth),
					Style.getPyXLineStyle(self.style.lineStyle)
				]
			)


