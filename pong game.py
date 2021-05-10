# russell mckenna
# pong game


#imports
import turtle
import time


#window setup
dimentional_list = [1000,750]
window = turtle.Screen()
turtle.speed(0)
window.title('Pong')
window.bgcolor('black')
window.setup(dimentional_list[0], dimentional_list[1])
window.tracer(0)


#paddles
width = dimentional_list[0]
height = dimentional_list[1]
paddlewidth = 10
paddlelength = 160
positon_from_origin = 450
ballr = 12.5
ybar = (height - ballr)/2
xbar = (width - ballr)/2


#paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape('square')
paddle1.shapesize(stretch_wid=8, stretch_len=1)
paddle1.color('white')
paddle1.penup()
paddle1.goto(-positon_from_origin,0)


#paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape('square')
paddle2.shapesize(stretch_wid=8, stretch_len=1)
paddle2.color('white')
paddle2.penup()
paddle2.goto(positon_from_origin,0)


#Ball

ballspeed = 5
ballx = ballspeed
bally = ballspeed

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.shapesize(stretch_wid=1.25, stretch_len=1.25)
ball.color('white')
ball.penup()
ball.goto(0,0)

#function that resets the ball and the ball speed
def ballreset():
    ball.setx(0)
    ball.sety(0)
    score.clear()
    score.write("Player 1: {}         Player 2 : {}".format(p1score,p2score),align= 'center', font = ('Agency FB',26,'normal'))


#scorecard

p1score = 0
p2score = 0

score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0,(height/2-50))
score.write("Player 1: {}         Player 2 : {}".format(p1score,p2score),align= 'center', font = ('Agency FB',26,'normal'))



#function for paddles to move up
movespeed = 20
def paddleup(paddle):
    ycord = paddle.ycor()
    if ycord <= (height - paddlelength)/2:
        ycord += movespeed
        paddle.sety(ycord)

#function for paddles to move down
def paddledown(paddle):
    ycord = paddle.ycor()
    if ycord >= -(height - paddlelength)/2:
        ycord -= movespeed
        paddle.sety(ycord)

#functions for paddle movement because each key press needs and empty function

# movement functions for paddle 1
def paddle1up():
    paddleup(paddle1)
def paddle1down():
    paddledown(paddle1)
#movement functions for paddle 2
def paddle2up():
    paddleup(paddle2)
def paddle2down():
    paddledown(paddle2)

#programing of the movement keys with coresponging functions
window.listen()
window.onkeypress(paddle1up,'w')
window.onkeypress(paddle2up,'Up')
window.onkeypress(paddle1down,'s')
window.onkeypress(paddle2down,'Down')

#main game loop

while True:
    window.update()

#ball movement
    ball.setx(ball.xcor()+ballx)
    ball.sety(ball.ycor()+bally)


#ball wall collisions
    #top wall
    if ball.ycor() >= ybar:
        ball.sety(ybar)
        bally *= -1

    #bottom wall
    if ball.ycor() <= (-ybar):
        ball.sety(-ybar)
        bally *= -1

    #right wall
    if ball.xcor() >= (xbar):
        p1score += 1
        ballx = ballspeed
        bally = ballspeed
        ballreset()
        print(ballx)

    #left wall
    if ball.xcor() <= (-xbar):
        p2score += 1
        ballx = ballspeed
        bally = ballspeed
        ballreset()


#ball paddle contact
    #contact with paddle2
    if (ball.xcor()+ballr) >= (paddle2.xcor()-paddlewidth/2) and ((paddle2.ycor()-paddlelength/2) <= ball.ycor() < (paddle2.ycor()+paddlelength/2)):
        ball.setx(paddle2.xcor()-paddlewidth/2-ballr)
        ballx *= -1
        ballx -= 1

    #contact with paddle1
    if (ball.xcor()-ballr) <= (paddle1.xcor()+paddlewidth/2) and ((paddle1.ycor()-paddlelength/2) <= ball.ycor() < (paddle1.ycor()+paddlelength/2)):
        ball.setx(-(paddle2.xcor()-paddlewidth/2-ballr))
        ballx *= -1
        ballx += 1

    time.sleep(1./60)

#displays winner message
    if p1score >= 11 or p2score >= 11:
        window.clear()
        window.title('Pong')
        window.bgcolor('black')
        window.setup(width, height)
        window.tracer(0)

        winner = turtle.Turtle()
        winner.speed(0)
        winner.color('white')
        winner.penup()
        winner.hideturtle()
        winner.goto(0,0)

        if p1score >= 11:
            winner.write("Player 1 Wins" ,align= 'center', font = ('Agency FB',26,'normal'))
            time.sleep(2.5)
            break
        if p2score >= 11:
            winner.write("Player 2 Wins" ,align= 'center', font = ('Agency FB',26,'normal'))
            time.sleep(2.5)
            break
