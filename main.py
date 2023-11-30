#--Principal--
import turtle
import time

delay = 0.1

wn = turtle.Screen()

#Titulo y demas
wn.title("Juego snake")
wn.setup(width=600, height=600)
wn.bgcolor("#5f820d")

#--Cabeza de la serpiente--
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.goto(0, 0)
head.direction = "up"
head.penup()


def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)
        
    if head.direction == "down":
        y = head.ycor()      
        head.sety(y - 10)
        
    if head.direction == "right":
        x = head.xcor()      
        head.setx(x + 10)
    
    if head.direction == "left":
        x = head.xcor()      
        head.setx(x - 10)



while True:
    wn.update()
    mov()
    time.sleep(delay)



turtle.done()
