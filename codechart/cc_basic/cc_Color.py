__all__ = ['Color']
from pyx import *
class Color:
	def __init__(self, r=0, g=0, b=0):
		self.r = r;
		self.g = g;
		self.b = b;

	def getPyxColor(self):
		return color.rgb(
					self.r*1.0/255, 
					self.g*1.0/255, 
					self.b*1.0/255
				);

	@staticmethod
	def copy(c):
		return Color(c.r, c.g, c.b);
