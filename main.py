# --Angel Gabriel Hirales Guzman
# --8SE
# --Cuadrado 2D en python
import turtle

turtle.setup(450,450)

tortuga = turtle.Turtle()
tortuga.speed(1.5)

# primer cuadrado
for _ in range(4):
    tortuga.forward(100)
    tortuga.left(90)

tortuga.goto(-50, -50)

#segundo cuadrado
for _ in range(4):
    tortuga.forward(100)
    tortuga.left(90)

# unir las esquinas inferiores
tortuga.penup()
tortuga.goto(100, 0)
tortuga.pendown()
tortuga.goto(50, -50) 

# unir las esquinas superiores
tortuga.penup()
tortuga.goto(0, 100)
tortuga.pendown()
tortuga.goto(-50, 50)

tortuga.penup()
tortuga.goto(100, 100)
tortuga.pendown()
tortuga.goto(50, 50)

turtle.done()