from turtle import *
t = Turtle()
t.speed(0)
def get_coords(x,y):
    t.sethesding(t.towards(x,y))
    t.goto(x,y)
onscreenclick(get_coords)