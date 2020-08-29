import turtle

x = 0
y = 0
# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)

wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_len=1, stretch_wid=5)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_len=1, stretch_wid=5)

# ball
ball = turtle.Turtle()
ball.speed(5)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = -.2


def show_score():
    pen.clear()
    pen.write("player A:%s" % x + "      player B:%s" % y)


# function
def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 20)


def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 20)


def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 20)


def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 20)


def power_e():
    if ball.dy > 0:
        ball.dy = -1
        ball.dx = .5
        ball.speed(8)
    else:
        ball.dy = 1
        ball.speed(8)


def power_m():
    if ball.dy > 0:
        ball.dy = -1
        ball.dx = -.5
        ball.speed(8)
    else:
        ball.dy = 1
        ball.speed(8)


def backToNormalA():
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = .2
        ball.dy = .2
        ball.speed(5)


def backToNormalB():
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = -.2
        ball.dy = .2
        ball.speed(5)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(power_e, "e")
wn.onkeypress(power_m, "m")

show_score()
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # ball bouncing from paddle
    if ball.xcor() > 340 and ((ball.ycor() < paddle_b.ycor() + 50) and (ball.ycor() > paddle_b.ycor() - 50)):
        ball.setx(340)
        ball.dx *= -1
        ball.dy *= 1

    if ball.xcor() < -340 and ((ball.ycor() < paddle_a.ycor() + 50) and (ball.ycor() > paddle_a.ycor() - 50)):
        ball.setx(-340)
        ball.dx *= -1
        ball.dy *= 1
        # paddle checking
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    # ball checking
    if ball.xcor() > 390:
        backToNormalA()

        x += 1

        show_score()

    if ball.xcor() < -390:
        backToNormalB()
        y += 1
        show_score()

# egVar = False
# if egVar:
# power_e()
# egVar = False
# else:
# time.sleep(5)
# pass
