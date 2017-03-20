#Create a polygon function that accepts a turtle, sides, and distance.
#function file



def polygon(t, sides, distance):
    angle = 360/sides#angle variable is inside the function
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.right(angle)
    t.end_fill()

def cool(t,d):
    t.color('black')
    polygon(t,4,d)
    t.color('orange')
    polygon(t,3,d)

def coolQ(t, d):
    t.color('pink')
    polygon(t, 4, d)
    t.color('white')
    polygon(t, 3, d)
    
def coolSquared(t,d):
    for times in range(4):
        cool(t,d)
        t.right(90)


def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def star(t,d):

    t.begin_fill()
    for times in range(8):
        t.forward(d)
        t.left(135)

    t.end_fill()

def funky1(t, d1, d2, c1, c2):
    t.color(c1)
    polygon(t, 3, d1)
    t.color(c2)
    polygon(t, 3, d2)


def milkyway(t, d):
    for n in range(75):
        t.color(180+n, 238-n, 178+n)
        star(t, d)
        t.forward(d+3)
        t.right(n-5)

def petal(t, r, angle):
      for n in range(2):
            t.circle(r, angle)
            t.left(180-angle)
            

        
