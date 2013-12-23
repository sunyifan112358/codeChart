__all__ = [
	'Ellipse',
	'Polygon',
	'Diamond',
	'Rectangle',
	'RoundedRect'
]

from pyx import *
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve

import math
from cc_Point import Point
from cc_Shape import *
from cc_Style import *

class Ellipse(PrimitiveShape):
	'''Ellipse and circle'''
	def __init__(
			self, 
			x=0, y=0, 
			r1=80, r2=None,
			degree=0,
			style = None
		):
		if(r2==None):
			r2=r1
		super(Ellipse, self).__init__(Point(x, y), style);

		pathitems = []
		p1 = Point(x-r1, y)
		p2 = Point(x, y-r2)
		p3 = Point(x+r1, y)
		p4 = Point(x, y+r2)
		self.path = metapost.path.path([
			smoothknot(*p1.toTuple()), tensioncurve(),
			smoothknot(*p2.toTuple()), tensioncurve(),
			smoothknot(*p3.toTuple()), tensioncurve(),
			smoothknot(*p4.toTuple()), tensioncurve(),
		])


		self.addJointPoint(Point(x-r1, y));
		self.addJointPoint(Point(x, y-r2));
		self.addJointPoint(Point(x+r1, y));
		self.addJointPoint(Point(x, y+r2));

class Polygon(PrimitiveShape):
	'''Polygon'''
	def __init__(
			self, 
			pos = None,
			style = None
		):
		if pos==None:
			pos = (
				Point(0, 0),
				Point(100, 50),
				Point(200, 30),
				Point(150, 100),
				Point(50, 70)
			) 
		
		super(Polygon, self).__init__(Point.center(*pos), style);

		pathitems = [];
		pathitems.append(path.moveto(pos[0].x, pos[0].y));
		self.addJointPoint(Point(pos[0].x, pos[0].y));

		for i in range(len(pos)-1):
			pathitems.append( path.lineto(pos[i+1].x, pos[i+1].y) )
			self.addJointPoint(Point(pos[i+1].x, pos[i+1].y));

		pathitems.append(path.closepath())

		self.path = path.path(*pathitems);	

class Diamond(ComplexShape):
	def __init__(
			self, 
			x = 0, y = 0, 
			width = 80, height = 50, 
			style=None
		):
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

		polygon = Polygon((p1, p2, p3, p4));
		self.addShape(polygon);

class Rectangle(ComplexShape):
	'''Rectangle'''
	def __init__(
			self, 
			x=0, y=0, 
			width=100, height=80, 
			style = None
		):
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

		polygon = Polygon((p1, p2, p3, p4));
		self.addShape(polygon);

class RoundedRect(PrimitiveShape):
	'''Rounded Rectangle'''
	def __init__(
			self, 
			x = 0, y = 0, 
			width = 80, height = 60, 
			border_radius = 5, 
			style = None
		):
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
		self.path = path.path( *pathitems );

if __name__ == "__main__":
	Diamond.preview();
	Ellipse.preview();
	Polygon.preview();
	Rectangle.preview();
	RoundedRect.preview();
