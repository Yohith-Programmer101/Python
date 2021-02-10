from turtle import *
t = Turtle()
t.speed(0)
def get_coords(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(get_coords)
onscreenclick(get_coords)
