import turtle

width = 1600
height = 800
screen = turtle.Screen()
screen.setup(width, height, 0, 0)


def CurveSegment(turtle, len):
    if len > 6:
        len3 = len // 3
        CurveSegment(t, len3)
        t.left(60)
        CurveSegment(t, len3)
        t.right(120)
        CurveSegment(t, len3)
        t.left(60)
        CurveSegment(t, len3)
    else:
        t.fd(len)
        t.left(60)
        t.fd(len)
        t.right(120)
        t.fd(len)
        t.left(60)
        t.fd(len)


t = turtle.Turtle()
t.speed(100000)
t.ht()
for i in range(3):
    CurveSegment(t, 150)
    t.right(120)



turtle.done()
