#from pyx import *
from codechart import * 

class FlowChart(ComplexShape):
	def __init__(self):
		super(FlowChart, self).__init__()
		leftCenter = 10
		rightCenter = 55
		itemWidth = 20
		itemHeight = 12
		lineHeight = 25
		diamondScale = 1.5

		self.style = self.style \
					 .strokeWidth(0.2) \
					 .textSize(9) \
					 .endArrow(1)

		e1 = FC_Terminator(
				self.style,
				leftCenter, -lineHeight-0.3, 
				itemWidth * 1.3, itemHeight,
				r"Enter a new rigeon"
			)
		d1 = FC_Decision( 
				self.style,
				leftCenter, -lineHeight*2, 
				itemWidth*diamondScale, itemHeight*diamondScale,
				r"Correlation Exist?"
			)

		d2 = FC_Decision(
				self.style,
				leftCenter, -lineHeight*3, 
				itemWidth*diamondScale, itemHeight*diamondScale,
				r"WS \(RSSI>TH\)",
				textYes = r"Yes",
				textYesPos= "RIGHT",
				textNoPos = "BOTTOM"
			)

		d3 = FC_Decision(
				self.style,
				leftCenter, -lineHeight*4, 
				itemWidth*diamondScale, itemHeight*diamondScale,
				r"2G \(RSSI>TH\)"
			)


		e2 = FC_Terminator(
				self.style,
				leftCenter, -lineHeight*6, 
				itemWidth*1.3, itemHeight,
				r"End Sending"
			)

		r1 = FC_Process(
				self.style, 
				rightCenter, -lineHeight*2, 
				itemWidth, itemHeight,
				r"Query Database"
			)

		r2 = FC_Process(
				self.style,
				rightCenter, -lineHeight*3, 
				itemWidth, itemHeight,
				r"Find Correlation"
			)

		d4 = FC_Decision(
				self.style,
				rightCenter, -lineHeight*4, 
				itemWidth*diamondScale, itemHeight*diamondScale,
				r"Correlation Exist?"
			)

		r3 = FC_Process(
				self.style,
				rightCenter, -lineHeight*5, 
				itemWidth, itemHeight,
				r"Broadcast Correlation"
			)

		self.addShape(e1, e2, d1, d2, d3, d4, r1, r2, r3);

		self.style = self.style \
					 .textVAlign("TOP") \
					 .textHAlign("LEFT")\
					 .textSize(6) 
		t1 = Text(
				self.style,
				leftCenter+itemWidth/2.0*diamondScale, 
				-lineHeight*3 - 0.1*self.style.getTextSize(),
				None,
				r"PU Present"
			)
		t2 = Text(
				self.style,
				leftCenter+itemWidth/2.0*diamondScale,
				-lineHeight*4 - 0.1*self.style.getTextSize(),
				None,
				r"PU Present"
			)

		t3 = Text(
				self.style,
				leftCenter + 0.5,
				-lineHeight*4 \
					- itemHeight/2.0*diamondScale \
					- (0.5+0.1)*self.style.getTextSize(),
				None,
				r"PU Absent"
			)

		self.addShape(t1, t2, t3);

		self.addShape(
			StraightLine(
				self.style,
				e1.jointPoints[0],
				d1.jointPoints[3]
			)
		)

		self.addShape(
			StraightLine(
				self.style,
				d1.jointPoints[1],
				d2.jointPoints[3]
			)
		)

		self.addShape(
			StraightLine(
				self.style,
				d2.jointPoints[1],
				d3.jointPoints[3]
			)
		)

		self.addShape(
			StraightLine(
				self.style,
				d3.jointPoints[1],
				e2.jointPoints[2],
			)
		)

		self.addShape(
			StraightLine(
				self.style,
				d1.jointPoints[2],
				r1.jointPoints[7]
			)
		)

		self.addShape(
			StraightLine(
				self.style,
				r1.jointPoints[4],
				r2.jointPoints[6]
			)
		)
		self.addShape(
			StraightLine(
				self.style,
				r2.jointPoints[4],
				d4.jointPoints[3]
			)
		)
		self.addShape(
			StraightLine(
				self.style,
				d4.jointPoints[1],
				r3.jointPoints[6]
			)
		)

		self.addShape(
			ElbowLine(
				self.style,
				(
					d2.jointPoints[2],
					Point.center(d2.jointPoints[2], r1.jointPoints[7]),
					r1.jointPoints[7]
				),
				'x'
			)
		)

		self.addShape(
			ElbowLine(
				self.style,
				(
					d3.jointPoints[2],
					Point.center(d3.jointPoints[2], r1.jointPoints[7]),
					r1.jointPoints[7]
				),
				'x'
			)
		)

		l1 = ElbowLine(
				self.style, 
				(
					r3.jointPoints[4],
					Point.center(r3.jointPoints[4], e2.jointPoints[2]),
					e2.jointPoints[2],
				),
				'y'
			)

		self.addShape(l1);

		self.addShape(
			ElbowLine(
				self.style.noEndArrow(),
				(
					d4.jointPoints[2],
					Point(
						d4.jointPoints[2].x + 10,
						(d4.jointPoints[2].y+l1.jointPoints[1].y)/2
					),
					l1.jointPoints[2],
				),
				'x'
			)
		)

if __name__ == '__main__':
	FlowChart.preview();


