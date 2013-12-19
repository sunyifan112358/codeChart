__all__ = ['StyleSet', 'Style']
from pyx import *
from cc_Color import Color
import copy

class StyleSet(object):
	def __init__(self):
		''' Stroke and fill '''
		self.doFill = False
		self.doStroke = False
		self.fillColor = Color(0, 0, 0)
		self.strokeColor = Color(0, 0, 0)
		self.strokeWidth = 1
		self.lineStyle = "SOLID"

		'''Arrow related'''
		self.useBeginArrow = False;
		self.beginArrowSize = 0.2;
		self.useEndArrow = True;
		self.endArrowSize = 0.2;

		''' Text related '''
		self.textHAlign = "LEFT";
		self.textVAlign = "BASELINE";
		self.textHFlush = "LEFT";
		self.textSize  = 0;
		

class Style(object):

	prototype = StyleSet();
	

	@staticmethod
	def noFill(instance = None):
		if not instance:
			instance = Style.prototype;
		instance.doFill = False;

	@staticmethod
	def noStroke(instance = None):
		if not instance:
			instance = Style.prototype;
		instance.doStroke = False;

	@staticmethod
	def fill(r, g, b, instance = None):
		if not instance:
			instance = Style.prototype;
		instance.fillColor = Color(r, g, b);
		instance.doFill = True;

	@staticmethod
	def stroke(r, g, b, instance = None):
		if not instance:
			instance = Style.prototype;
		instance.strokeColor = Color(r, g, b)
		instance.doStroke = True

	@staticmethod
	def strokeWidth(strokeWidth, instance = None):
		if not instance:
			instance = Style.prototype
		instance.strokeWidth = strokeWidth;

	@staticmethod
	def lineStyle(lineStyle, instance = None):
		if not instance:
			instance = Style.prototype
		instance.lineStyle = lineStyle;

	@staticmethod
	def getPyXLineStyle(lineStyle):
		if(lineStyle=="SOLID"):
			return style.linestyle.solid
		elif(lineStyle == "DASHED"):
			return style.linestyle.dashed
		elif(lineStyle == "DOTTED"):
			return style.linestyle.dotted
		elif(lineStyle == "DASHDOTTED"):
			return style.linestyle.dashdotted
		else:
			raise Exception("Unsupport line style "+lineStyle+
						" Choose from SOLID, DASHED, DOTTED and DASHDOTTED"
					)

	@staticmethod
	def noBeginArrow(instance = None):
		if not instance:
			instance = Style.prototype
		instance.useBeginArrow = False

	@staticmethod
	def beginArrow(size, instance = None):
		if not instance:
			instance = Style.prototype
		instance.beginArrowSize = size
		instance.userBeginArrow = True

	@staticmethod
	def noEndArrow(instance = None):
		if not instance:
			instance = Style.prototype
		instance.useEndArrow = False

	@staticmethod
	def endArrow(size, instance = None):
		if not instance:
			instance = Style.prototype
		instance.endArrowSize = size
		instance.useEndArrow = True

	@staticmethod
	def textHAlign(hAlignString, instance = None ):
		if not instance:
			instance = Style.prototype
		instance.textHAlign = hAlignString;

	@staticmethod
	def getPyXHAlign(hAlign):
		if(hAlign == "LEFT"):
			return text.halign.boxleft;
		elif(hAlign == "CENTER"):
			return text.halign.boxcenter;
		elif(hAlign == "RIGHT"):
			return text.halign.boxright;
		else:
			raise Exception("In valid horizontal align: " + hAlign +
				" Choose among LEFT, CENTER and RIGHT");

	@staticmethod
	def textVAlign(vAlignString, instance = None):
		if not instance:
			instance = Style.prototype
		instance.textVAlign = vAlignString;

	@staticmethod
	def getPyXVAlign(vAlign):
		if(vAlign == "TOP"):
			return text.valign.top;
		elif(vAlign == "MIDDLE"):
			return text.valign.middle;
		elif(vAlign == "BOTTOM"):
			return text.valign.bottom;
		elif(vAlign == "BASELINE"):
			return text.valign.baseline;
		else:
			raise Exception("In valid vertical align: " + hAlignString +
				" Choose among TOP, MIDDLE, BOTTOM and BASELINE");

	@staticmethod
	def textHFlush(hFlushString, instance = None):
		if not instance:
			instance = Style.prototype
		instance.textHFlush = hFlushString;	

	@staticmethod
	def getPyXHFlush(hFlush, instance = None):
		if(hFlush == "LEFT"):
			return text.halign.flushleft
		elif(hFlush == "CENTER"):
			return text.halign.flushcenter
		elif(hFlush == "RIGHT"):
			return text.halign.flushright
		else:
			raise Exception("In valid horizontal flush: " + hFLushString +
				" Choose among LEFT, CENTER and RIGHT");


	@staticmethod
	def textSize(size, instance = None):
		if not instance:
			instance = Style.prototype
		instance.textSize = size;

	@staticmethod
	def getPyXTextSize(tSize):
		return text.size(tSize);

	@staticmethod
	def getSnapshot(instance = None):
		if not instance:
			p = Style.prototype;
		else:
			p = instance

		s = copy.deepcopy(p);
		return s


	def __init__(self):
		pass

