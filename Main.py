from turtle import *
import random

WIDTH = 700
HEIGHT = 700

CORMAX = 320

PENSIZE_MIN = 2
PENSIZE_MAX = 6

ANGLE = 15

COLOR = 25
COLORVAL_MIN = 50
COLORVAL_MAX = 255

DISTANCE_MIN = 1
DISTANCE_MAX = 5

NUM_TURTLES = random.randint(5,8)

print( "Screen: " + str(WIDTH) + "x" + str(HEIGHT) )
print( "Number of turtles: " + str(NUM_TURTLES) )
print( "Turtle:" )
print( "-- coordinate maximum: " + str(CORMAX) )
print( "-- pen size: " + str(PENSIZE_MIN) + "-" + str(PENSIZE_MAX) )
print( "-- color: " + str(COLORVAL_MIN) + "-" + str(COLORVAL_MAX) + ", +-" + str(COLOR) )
print( "-- distance: " + str(DISTANCE_MIN) + "-" + str(DISTANCE_MAX) )

class ranTurtle(Turtle):
    def __init__(self):
        Turtle.__init__(self)        
        self.speed(10000)
        self.hideturtle()

        ## color
        r = lambda: random.randint(50,255)
        self.colorR = r()
        self.colorG = r()
        self.colorB = r()
        self.color = '#%02X%02X%02X' % (self.colorR, self.colorG, self.colorB)

        ## heading
        self.setheading( random.randint(0,359) )

        ## position
        self.penup()
        axis = random.randint(1,2)
        cord1 = random.choice([+CORMAX,-CORMAX])
        cord2 = random.randint(-CORMAX, +CORMAX)                
        if axis == 1:
            self.setx( cord1 )
            self.sety( cord2 )
        else:
            self.setx( cord2 )
            self.sety( cord1 )        
        self.pendown()

    def ranforward(self):
        Turtle.forward(self, random.randint( DISTANCE_MIN, DISTANCE_MAX ))

    def rancolor(self):
        colormod = lambda: random.randint(-COLOR, +COLOR)
        self.colorR += colormod()
        self.colorG += colormod()
        self.colorB += colormod()
        
        if self.colorR < COLORVAL_MIN:
            self.colorR = COLORVAL_MIN
        elif self.colorR > COLORVAL_MAX:
            self.colorR = COLORVAL_MAX
        if self.colorG < COLORVAL_MIN:
            self.colorG = COLORVAL_MIN
        elif self.colorG > COLORVAL_MAX:
            self.colorG = COLORVAL_MAX
        if self.colorB < COLORVAL_MIN:
            self.colorB = COLORVAL_MIN
        elif self.colorB > COLORVAL_MAX:
            self.colorB = COLORVAL_MAX

        Turtle.color(self, '#%02X%02X%02X' % (self.colorR, self.colorG, self.colorB))
    
def ranPensize(current):
    mod = random.randint(-3,+3
                         )
    new = current + mod
    if (new > PENSIZE_MAX):
        return PENSIZE_MAX
    elif (new < PENSIZE_MIN):
        return PENSIZE_MIN
    else:
        return new

def between(num, low, high):
    return ( ( low <= num <= high ) )
    
s = Screen()
s.setup(width=WIDTH, height=HEIGHT, startx=0, starty=0)
s.bgcolor("black")

turtles = []
turtleNum = 0

for i in range( 1, NUM_TURTLES ):
    t = ranTurtle()
    turtles.append( ranTurtle() )

while(1):
    for t in turtles:    
        
        t.pensize( ranPensize( t.pensize() ) )
        t.left( random.randint(-ANGLE,+ANGLE) )
        t.rancolor( )
        t.ranforward( )

        if t.xcor() > +CORMAX: # right
            
            if 0 <= t.heading() <= 90: #right-left
                t.left( 5 )
                
            elif 270 <= t.heading() <= 359: #right-right
                t.right( 5 )
                
        elif t.xcor() < -CORMAX: # left
               
            if  180 <= t.heading() <= 270: #left-left
                t.left( 5 )

            elif 90 <= t.heading() <= 180: #right-right
                t.right( 5 )

        elif t.ycor() > +CORMAX: # top

            if 90 <= t.heading() <= 180: # top-left
                t.left( 5 )

            elif 0 <= t.heading() <= 90:
                t.right( 5 )

        elif t.ycor() < -CORMAX: # bottom

            if 270 <= t.heading() <= 359: # top-left
                t.left( 5 )

            elif 180 <= t.heading() <= 270:
                t.right( 5 )
            
