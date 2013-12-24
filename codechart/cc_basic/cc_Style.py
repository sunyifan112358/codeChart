__all__ = ['Style']
from pyx import *
from cc_Color import Color
import copy

class Style(object):
	'''Style setting for all shapes
	All shapes keeps an instance of Style and use it for rendering
	'''

	def __init__(self):
		'''Set the default style sheet'''

		#rotation
		self._rotate = 0

		#Stroke and fill
		self._doFill = False
		self._doStroke = True
		self._fillColor = Color(0, 0, 0)
		self._strokeColor = Color(0, 0, 0)
		self._strokeWidth = 1
		self._lineStyle = "SOLID"

		#Arrow related 
		self._useBeginArrow = False;
		self._beginArrowSize = 2;
		self._useEndArrow = True;
		self._endArrowSize = 2;

		#Text related
		self._textHAlign = "CENTER";
		self._textVAlign = "BASELINE";
		self._textHFlush = "LEFT";
		self._textSize  = 12;

	def rotate(self, rotate):
		s = Style.getSnapshot(self)
		s._rotate = rotate
		return s

	def getPyXRotate(self):
		return trafo.rotate(self.getRotate())

	def getRotate(self):
		return self._rotate;
			
	def noFill(self):
		s = Style.getSnapshot(self)
		s._doFill = False;
		return s

	def getDoFill(self):
		return self._doFill

	def noStroke(self):
		s = Style.getSnapshot(self)
		s._doStroke = False;
		return s
	
	def getDoStroke(self):
		return self._doStroke

	def fill(self, r, g, b):
		s = Style.getSnapshot(self)
		s._fillColor = Color(r, g, b);
		s._doFill = True;
		return s
	
	def getFillColor(self):
		return self._fillColor()

	def getPyXFillColor(self):
		return self._fillColor.getPyXColor()

	def stroke(self, r, g, b):
		s = Style.getSnapshot(self)
		s._strokeColor = Color(r, g, b)
		s._doStroke = True
		return s

	def getStrokeColor(self):
		return self._strokeColor
	
	def getPyXStrokeColor(self):
		return self._strokeColor.getPyXColor()

	def strokeWidth(self, strokeWidth):
		s = Style.getSnapshot(self)
		s._strokeWidth = strokeWidth;
		return s
	
	def getStrokeWidth(self):
		return self._strokeWidth
	
	def getPyXStrokeWidth(self):
		return style.linewidth(self._strokeWidth)

	def lineStyle(self, lineStyle):
		s = Style.getSnapshot(self)
		s._lineStyle = lineStyle;
		return s

	def getPyXLineStyle(self):
		lineStyle = self._lineStyle
		if(lineStyle=="SOLID"):
			return style.linestyle.solid
		elif(lineStyle == "DASHED"):
			return style.linestyle.dashed
		elif(lineStyle == "DOTTED"):
			return style.linestyle.dotted
		elif(lineStyle == "DASHDOTTED"):
			return style.linestyle.dashdotted
		else:
			raise ValueError(
				"Unsupport line style "+lineStyle+
				" Choose from SOLID, DASHED, DOTTED and DASHDOTTED"
			)

	def noBeginArrow(self):
		s = Style.getSnapshot(self)
		s._useBeginArrow = False
		return s
	
	def getUseBeginArrow(self):
		return self._useBeginArrow

	def beginArrow(self, size):
		s = Style.getSnapshot(self)
		s._beginArrowSize = size
		s._userBeginArrow = True
		return s

	def getBeginArrowSize(self):
		return self._beginArrowSize

	def getPyXBeginArrow(self):
		if self.getUseBeginArrow():
			return deco.barrow(
					[
						deco.stroked([self.getPyXStrokeColor()]),
						deco.filled([self.getPyXStrokeColor()])
					],
					size = self.getBeginArrowSize()
				)
		else:
			return None

	def noEndArrow(self):
		s = Style.getSnapshot(self)
		s._useEndArrow = False
		return s
	
	def getUseEndArrow(self):
		return self._useEndArrow

	def endArrow(self, size):
		s = Style.getSnapshot(self)
		s._endArrowSize = size
		s._useEndArrow = True
		return s

	def getEndArrowSize(self):
		return self._endArrowSize

	def getPyXEndArrow(self):
		if self.getUseEndArrow():
			return deco.earrow(
					[
						deco.stroked([self.getPyXStrokeColor()]),
						deco.filled([self.getPyXStrokeColor()])
					],
					size = self.getEndArrowSize()
				)
		else:
			return None

	def textHAlign(self, hAlignString):
		s = Style.getSnapshot(self)
		s._textHAlign = hAlignString;
		return s

	def getTextHAlign(self):
		return s_textHAlign

	def getPyXHAlign(self):
		hAlign = self._textHAlign
		if(hAlign == "LEFT"):
			return text.halign.boxleft;
		elif(hAlign == "CENTER"):
			return text.halign.boxcenter;
		elif(hAlign == "RIGHT"):
			return text.halign.boxright;
		else:
			raise ValueError(
					"In valid horizontal align: " + hAlign +
					" Choose among LEFT, CENTER and RIGHT"
				);

	def textVAlign(self, vAlignString):
		s = Style.getSnapshot(self)
		s._textVAlign = vAlignString;
		return s

	def getTextVAlign(self):
		return self._textVAlign

	def getPyXVAlign(self):
		vAlign = self._textVAlign
		if(vAlign == "TOP"):
			return text.valign.top;
		elif(vAlign == "MIDDLE"):
			return text.valign.middle;
		elif(vAlign == "BOTTOM"):
			return text.valign.bottom;
		elif(vAlign == "BASELINE"):
			return text.valign.baseline;
		else:
			raise ValueError("In valid vertical align: " + hAlignString +
				" Choose among TOP, MIDDLE, BOTTOM and BASELINE");

	def textHFlush(self, hFlushString):
		s = Style.getSnapshot(self)
		s._textHFlush = hFlushString;	
		return s

	def getTextHFlush(self):
		return self._textHFlush

	def getPyXHFlush(self):
		hFlush = self._textHFlush
		if(hFlush == "LEFT"):
			return text.halign.flushleft
		elif(hFlush == "CENTER"):
			return text.halign.flushcenter
		elif(hFlush == "RIGHT"):
			return text.halign.flushright
		else:
			raise ValueError(
					"In valid horizontal flush: " + hFLush +
					" Choose among LEFT, CENTER and RIGHT"
				);

	def textSize(self, size):
		s = Style.getSnapshot(self)
		s._textSize = size;
		return s

	def getTextSize(self):
		return self._textSize

	def getPyXTextSize(self):
		'''Text size is achieved by scale'''
		return trafo.scale(sx=self.getTextSize())	


	@staticmethod
	def getSnapshot(instance = None):
		if not instance:
			if isinstance(instance, Style):
				raise TypeError( "Only take snapshot for Style tyle")
			p = Style()
			return p
		else:
			return copy.deepcopy(instance)

if __name__ == "__main__":
	s = Style()
	s2 = s.noFill()
	print s.doFill
	print s2.doFill
