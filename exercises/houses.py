from turtle import *

color('red', 'yellow')
def house(x, y, z):
   setheading(0)
   up()
   goto(x, y)
   down()
   right(90)
   forward(z)
   left(90)
   forward(z)
   left(90)
   forward(z)
   left(30)
   forward(z)
   left(120)
   forward(z)
   left(120)
   forward(z)
   right(90)
   forward(z)

house(30, 30, 20)
house(200, 200, 40)
house(-100, -100, 50)
house(-100, 100, 80)

done()
