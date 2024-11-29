import turtle

o = turtle.Turtle()
o.shape("turtle")

for i in range(4):
	if(i%2==0):
		o.forward(100)
		o.left(135)
	else:
		o.forward(100)
		o.left(90)
		
	turtle.done