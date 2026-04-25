import turtle
wn=turtle.Screen()
rak=turtle.Turtle()

rak.left(90)
rak.forward(230)
rak.right(90)
rak.forward(30)
for i in range(180):
    rak.forward(1)
    rak.right(1)
rak.forward(30)
rak.left(135)
rak.forward(150)
wn.exitonclick()
