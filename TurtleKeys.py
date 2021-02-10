from turtle import *
import turtle
turtle.speed(0)
turtle.title("JOY STICK")
t = Turtle()
def f():
    fd(20)
def b():
     bk(20)
def l():
    left(90)
def r():
    right(90)
onkey(f,"Up")
onkey(b,"Down")
onkey(l,"Left")
onkey(r,"Right")
listen()
turtle.exitonclick()


