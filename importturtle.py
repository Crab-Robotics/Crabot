import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)
n=10
while n <= 40:
    t.circle(n)
    n = n+10
while True:
    s.update()