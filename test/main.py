from pyx import *

from codechart import * 

leftCenter = 10
rightCenter = 55
itemWidth = 20
itemHeight = 12
lineHeight = 25
diamondScale = 1.5


p = Plot();

Style.noFill();
Style.stroke(0,0,0);
Style.strokeWidth(0.2);
Style.lineStyle("SOLID")
Style.textHAlign("CENTER");
Style.textVAlign("MIDDLE");
Style.textHFlush("CENTER");
Style.textSize(9);

#e1 = Ellipse(leftCenter, -lineHeight-0.5, itemWidth/2*1.3, itemHeight/2, 0)
e1 = FC_Terminator(
		leftCenter,
		-lineHeight-0.3, 
		itemWidth*1.3, 
		itemHeight,
		r"Enter a New Region"
	)
d1 = FC_Decision( 
		leftCenter, 
		-lineHeight*2, 
		itemWidth*diamondScale, 
		itemHeight*diamondScale,
		r"Correlation Exist?"
	)

d2 = FC_Decision(
		leftCenter, 
		-lineHeight*3, 
		itemWidth*diamondScale, 
		itemHeight*diamondScale,
		r"WS \(RSSI>TH\)",
		textYes = r"Yes",
		textYesPos= "RIGHT",
		textNoPos = "BOTTOM"
	)

d3 = FC_Decision(
		leftCenter, 
		-lineHeight*4, 
		itemWidth*diamondScale, 
		itemHeight*diamondScale,
		r"2G \(RSSI>TH\)"
	)


e2 = FC_Terminator(
		leftCenter, 
		-lineHeight*6, 
		itemWidth*1.3, 
		itemHeight,
		r"End Sending"
	)

r1 = FC_Process(
		x=rightCenter, 
		y = -lineHeight*2, 
		width=itemWidth, 
		height=itemHeight,
		text=r"Find Correlation"
	);

r2 = FC_Process(
		rightCenter, 
		-lineHeight*3, 
		itemWidth, 
		itemHeight,
		r"Query Database"
	)

d4 = FC_Decision(
		rightCenter, 
		-lineHeight*4, 
		itemWidth*diamondScale, 
		itemHeight*diamondScale,
		r"Correlation Exist?"
	)

r3 = FC_Process(
		rightCenter, 
		-lineHeight*5, 
		itemWidth, 
		itemHeight,
		r"Broadcast Correlation"
	)


p.addShape(e1, e2, d1, d2, d3, d4, r1, r2, r3);

Style.textVAlign("TOP")
Style.textHAlign("LEFT")
Style.textSize(6)
t1 = Text(
		r"PU Present",
		leftCenter+itemWidth/2.0*diamondScale-1,
		-lineHeight*3 - 1 - 0.5
	)
t2 = Text(
		r"PU Present",
		leftCenter+itemWidth/2.0*diamondScale,
		-lineHeight*4 - 1
	)

t3 = Text(
		r"PU Absent",
		leftCenter + 1,
		-lineHeight*4 - itemHeight/2.0*diamondScale -3 - 1
	)

p.addShape(t1, t2, t3);

Style.endArrow(1)

p.addShape(
	StraightLine(
		e1.jointPoints[0],
		d1.jointPoints[3]
	)
)

p.addShape(
	StraightLine(
		d1.jointPoints[1],
		d2.jointPoints[3]
	)
)

p.addShape(
	StraightLine(
		d2.jointPoints[1],
		d3.jointPoints[3]
	)
)

p.addShape(
	StraightLine(
		d3.jointPoints[1],
		e2.jointPoints[2]
	)
)

p.addShape(
	StraightLine(
		d1.jointPoints[2],
		r1.jointPoints[7]
	)
)

p.addShape(
	StraightLine(
		r1.jointPoints[4],
		r2.jointPoints[6]
	)
)
p.addShape(
	StraightLine(
		r2.jointPoints[4],
		d4.jointPoints[3]
	)
)
p.addShape(
	StraightLine(
		d4.jointPoints[1],
		r3.jointPoints[6]
	)
)

p.addShape(
	ElbowLine(
		True,
		d2.jointPoints[2],
		Point.center(d2.jointPoints[2], r1.jointPoints[7]),
		r1.jointPoints[7]
	)
)

p.addShape(
	ElbowLine(
		True,
		d3.jointPoints[2],
		Point.center(d3.jointPoints[2], r1.jointPoints[7]),
		r1.jointPoints[7]
	)
)




l1 = ElbowLine(
		False,
		r3.jointPoints[4],
		Point.center(r3.jointPoints[4], e2.jointPoints[2]),
		e2.jointPoints[2]
	)

p.addShape(l1);

Style.noEndArrow();
p.addShape(
	ElbowLine(
		True,
		d4.jointPoints[2],
		Point(
			d4.jointPoints[2].x+1, 
			(d4.jointPoints[2].y+l1.jointPoints[1].y)/2
		),
		l1.jointPoints[2],
		
	)
)




p.draw();



p.save("test1")


