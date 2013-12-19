__all__ = ['Plot']
from pyx import *
from cc_Color import Color

from PIL import Image

class Plot:
	'''A container of all shapes and a canvas'''	

	def __init__(self):
		self.canvas = canvas.canvas()
		self.shapeList = [];
		text.set(mode="latex")

		'''Parameters'''
		'''stroke and fill'''
		self.doStroke 		= True
		self.doFill   		= False
		self.stokeColor 	= Color(0, 0, 0)
		self.fillColor  	= Color(0, 0, 0)
		self.strokeWeight 	= 1

	def addShape(self, *shapes):
		for shape in shapes:
			self.shapeList.append(shape);

	def draw(self):
		for shape in self.shapeList:
			shape.draw(self.canvas)



	def save(self, filename):
		self.canvas.writeEPSfile(filename)
		self.canvas.writePDFfile(filename)
		img = Image.open(filename+".eps")
		#img.resize((img.size[0]*2, img.size[1]*2))
		img.save(filename+".png")
