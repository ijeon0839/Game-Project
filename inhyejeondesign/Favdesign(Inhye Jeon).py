#Inhye Jeon

import turtle
bob=turtle.Turtle()
from myFunctionfile import*
turtle.colormode(255)

c1 = (252, 237, 208)#yellow
c2 = (156, 111, 111)#brown
c3 = (255, 209, 209)#pink red
turtle.bgcolor(c1)
bob.speed(0)
'''def funky1(t, d1, d2, c1, c2):
    t.color(c1)
    polygon(t, 3, d1)
    t.color(c2)
    polygon(t, 3, d2)
def coolQ(t, d):
    t.color('pink')
    polygon(t, 4, d)
    t.color('white')
    polygon(t, 3, d)'''


d = 30

bob.pensize(3)
jump(bob, -300, 300)
bob.color(255, 73, 73)
polygon(bob, 4, 600)
bob.pensize(1)

jump(bob, -300, -200)
for n in range(72):
      funky1(bob, 55, 27.5, c2, c3)
      bob.forward(d+3)
      bob.left(n-5)
      
bob.pensize(3)      
for n in range(27):
      funky1(bob, 50, 25, c2, c3)
      bob.forward(d)
      bob.left(n)
      bob.forward(d+(d/2))
      bob.left(90)

jump(bob, -70, 220)
for times in range(8):
    coolQ(bob,100)
    bob.right(45)
    bob.forward(100)


