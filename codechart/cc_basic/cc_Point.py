__all__ = ['Point']

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "Point: x="+str(self.x)+" y="+str(self.y);

	def __repr__(self):
		return self.__str__();
	
	def toTuple(self):
		'''Get the tuple form of Point'''
		return (self.x, self.y)

	def move(self, point):
		'''Move the point by a vector'''
		p = Point( self.x + point.x, self.y + point.y )
		return p	

	@staticmethod
	def center(*points):
		tempX = 0.0
		tempY = 0.0
		for point in points:
			tempX = tempX + point.x
			tempY = tempY + point.y
		tempX = tempX*1.0/len(points)
		tempY = tempY*1.0/len(points)
		return Point(tempX, tempY);
 
