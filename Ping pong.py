import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(width=1000, height=1000)
wn.title("Pong by Ajit")

  

#paddle_a
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.penup()
paddle_a.speed(6)
paddle_a.goto(-200, 0)
paddle_a.shapesize(stretch_len=1,stretch_wid=10)


#paddle_B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.penup()
paddle_b.speed(2)
paddle_b.goto(200, 0)
paddle_b.shapesize(stretch_len=1,stretch_wid=10)

# points
point_a=0
point_b=0

#ball
ball=turtle.Turtle()
ball.shape("circle")
ball.color("black")
ball.goto(0,0)
ball.penup()
ball.speed(0)
ball.dx=8
ball.dy=8

# score
score=turtle.Turtle()
score.color("blue")
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0,222)
score.write("player:{}       Ajit:{} ".format(point_a,point_b),align="center",font=("courier",22,"normal"))

#function
def paddel_aup():
    y=paddle_a.ycor()
    y+=50
    paddle_a.sety(y)

def paddel_adown():
    y=paddle_a.ycor()
    y-=50
    paddle_a.sety(y)

def paddel_bup():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddel_bdown():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#keyboard bindiing
wn.listen()
wn.onkeypress(paddel_aup,"w")
wn.onkeypress(paddel_adown,"s")
wn.onkeypress(paddel_bup,"Up")
wn.onkeypress(paddel_bdown,"Down")

#main game loop
while True:
    wn.update()

    #moving the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #boder checking
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.dy*=-1

    if ball.xcor()>220:
       ball.goto(0,0)
       ball.dx*=-1
       point_a+=1
       score.clear()
       score.write("player:{}     Ajit:{} ".format(point_a,point_b),align="center",font=("courier",22,"normal"))

    if ball.xcor()<-220:
        ball.goto(0,0)
        ball.dx*=-1
        point_b+=1
        score.clear()
        score.write("player:{}      Ajit:{} ".format(point_a,point_b),align="center",font=("courier",22,"normal"))

    #ball and paddl collision
    #collison with paddel b
    if (ball.xcor()>170 and ball.xcor()<180) and ball.ycor()>=paddle_b.ycor()-100 and ball.ycor()<=paddle_b.ycor()+100:
        ball.dx*=-1
    #collison with paddel a
    if (ball.xcor()<-170 and ball.xcor()<180)and ball.ycor()>=paddle_a.ycor()-100 and ball.ycor()<=paddle_a.ycor()+100:
        ball.dx*=-1

turtle.done()

