__all__ = ['Plot']
from pyx import *
from cc_Color import Color

import Image

class Plot:

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



	def saveEPS(self, filename):
		self.canvas.writeEPSfile(filename)
	
	def savePDF(self, filename):
		self.canvas.writePDFfile(filename)
	
	def savePNG(self, filename):
		self.saveEPS(filename)
		img = Image.open(filename+".eps")
		while img.size[0]*img.size[1] >= 1e7:
			img = img.resize((img.size[0]/2, img.size[1]/2))
		img.save(filename + ".png");
		
