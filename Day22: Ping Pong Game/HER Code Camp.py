import turtle
import time
import random

#----------INTRO STUFF:--------#
#GAME WINDOW
width = 960
height = 540
window = turtle.Screen()
window.setup(width,height)
window.bgcolor('white')
window.title("WeL<3veNetflix's Ping Pong Game")
window.tracer(0)

#BALL
ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")
ball.speed(8)
ball.penup()

#STAR
window.addshape("ninja_star", ((0, 4), (16, 16), (4, 0), (16, -16), (0, -4), (-16, -16), (-4, 0), (-16, 16)))
star = turtle.Turtle()
star.penup()
star.shape("ninja_star")
star.color("black")
star.hideturtle()
star.speed(0)

#OTHER VARIABLES
left_score = 0
right_score = 0
speedx = 10
speedy = 10
#------------------------------#



#-----------WRITERS:-----------#
#TITLE
title_writer = turtle.Turtle()
title_writer.speed(0)
title_writer.hideturtle()
title_writer.penup()
title_writer.setposition(0, 210)
title_writer.color('black')
title_writer.write("Ping Pong Game", align='center', font=('Courier', 40, 'bold'))

#SCORE
score_writer = turtle.Turtle()
score_writer.speed(0)
score_writer.hideturtle()
score_writer.penup()

#RANDOM INFO
give_info = turtle.Turtle()
give_info.speed(0)
give_info.hideturtle()
give_info.penup()
give_info.setposition(0, -10)
give_info.color('red')
#------------------------------#


#-----------PADDLES:-----------#
#COORDINATES
lp1 = (-30,-400)
lp2 = (-30,-380)
lp3 = (30,-380)
lp4 = (30,-400)
rp1 = (-30,400)
rp2 = (-30,380)
rp3 = (30,380)
rp4 = (30,400)

window.addshape("left_paddle", (lp1, lp2, lp3, lp4))
paddle_one = turtle.Turtle()
paddle_one.penup()
paddle_one.shape("left_paddle")
paddle_one.color("grey")
window.addshape("right_paddle", (rp1, rp2, rp3, rp4))
paddle_two = turtle.Turtle()
paddle_two.penup()
paddle_two.shape("right_paddle")
paddle_two.color("grey")

#MOVEMENT FUNCTIONS
def paddle_one_up():
    paddle_one.sety(paddle_one.ycor()+20)
    if paddle_one.ycor() > 240:
        paddle_one.sety(240)
def paddle_one_down():
    paddle_one.sety(paddle_one.ycor()-20)
    if paddle_one.ycor() < -240:
        paddle_one.sety(-240)
def paddle_two_up():
    paddle_two.sety(paddle_two.ycor()+20)
    if paddle_two.ycor() > 240:
        paddle_two.sety(240)
def paddle_two_down():
    paddle_two.sety(paddle_two.ycor()-20)
    if paddle_two.ycor() < -240:
        paddle_two.sety(-240)
#------------------------------#



#----------FUNCTIONS:----------#
#WRITE SCORE
def write_score():
    score_writer.setposition(300, 190)
    score_writer.color('blue')
    score_writer.write("Score: " + str(right_score), align='left', font=('Courier', 20, 'normal'))
    score_writer.setposition(-450, 190)
    score_writer.color('green')
    score_writer.write("Score: " + str(left_score), align='left', font=('Courier', 20, 'normal'))
write_score()

#WRITE MISS
def write_miss():
    give_info.setposition(0, -10)
    give_info.write("MISS!", align='center', font=('Arial', 30, 'bold'))
    give_info.setposition(0, -50)
    give_info.write("- 10", align='center', font=('Arial', 30, 'bold'))
    time.sleep(1.5)
    give_info.clear()

#WRITE +10
def write_plus_10():
    give_info.setposition(0, -10)
    give_info.write("+ 10", align='center', font=('Arial', 30, 'bold'))
    time.sleep(0.5)
    give_info.clear()

#BALL HIT RIGHT?
def check_for_right_hit():
    global speedx
    global right_score
    if (ball.xcor() == 390) and paddle_two.ycor() < ball.ycor()+40 and paddle_two.ycor() > ball.ycor() - 40:
        speedx = speedx * -1
        right_score = right_score + 10
        score_writer.clear()
        write_score()
        write_plus_10()

#BALL HIT LEFT?
def check_for_left_hit():
    global speedx
    global left_score
    if (ball.xcor() == -390) and paddle_one.ycor() < ball.ycor()+40 and paddle_one.ycor() > ball.ycor() - 40:
        speedx = speedx * -1
        left_score = left_score + 10
        score_writer.clear()
        write_score()
        write_plus_10()
    #------------------------------#


# FOR NORMAL ROUND (UP TO 30 PTS)
while True:
    window.update()
    time.sleep(0.1)

    ball.setx(ball.xcor() + speedx)
    ball.sety(ball.ycor() + speedy)

    window.onkey(paddle_one_up, "w")
    window.onkey(paddle_one_down, "s")
    window.onkey(paddle_two_up, "Up")
    window.onkey(paddle_two_down, "Down")
    window.listen()

    #KEEPS IN BOUNDS
    if ball.ycor() >= 270:
        speedy = speedy * -1
    elif ball.ycor() <= -270:
        speedy = speedy * -1

    check_for_right_hit()
    #BLITZ? ----- CHANGE TO 30
    if right_score == 30:
        break
    check_for_left_hit()
    #BLITZ?
    if left_score == 30:
        break

    #IF PADDLES MISS
    if ball.xcor() == 400:
        write_miss()
        right_score = right_score - 10
        score_writer.clear()
        write_score()
        ball.setposition(0, 0)
    if ball.xcor() == -400:
        write_miss()
        left_score = left_score - 10
        score_writer.clear()
        write_score()
        ball.setposition(0, 0)

#-------SETTING UP FOR BLITZ-------#
give_info.setposition(0, -10)
give_info.write("BLITZ ROUND!", align='center', font=('Arial', 30, 'bold'))
time.sleep(1)
give_info.clear()

#SPEED CHANGE
speedx = 15
speedy = 15
ball.setposition(0, 0)

#BLITZ COLORS
window.bgcolor('pale green')
paddle_one.color("dark violet")
paddle_two.color("dark violet")

#VARIABLES NEEDED FOR BLITZ
i = 0
side = 1
counter = 10
star_rand_y = random.randint(-250, 250)
star.showturtle()
colors = ["red", "blue", "gold", "light sea green", "dark orange", "indigo"]
#--------------------------------#

#BLITZ LOOP
while left_score < 50 and right_score < 50:
    window.update()
    time.sleep(0.1)

    ball.color(colors[i])
    i += 1
    if i == 5:
        i = 0
    ball.setx(ball.xcor() + speedx)
    ball.sety(ball.ycor() + speedy)

    #CHANGES STAR POSITION
    if counter % 10 == 0:
        if side == 1:
            star.setposition(-380, star_rand_y)
            star_rand_y = random.randint(-250, 250)
            side = 2
        else:
            star.setposition(380, star_rand_y)
            star_rand_y = random.randint(-250, 250)
            side = 1
    counter = counter + 1

    #IF PADDLE TOUCHES STAR
    if (star.xcor() == 380) and paddle_two.ycor() < star.ycor()+40 and paddle_two.ycor() > star.ycor() - 40:
        right_score = right_score - 2
        score_writer.clear()
        write_score()
        give_info.setposition(0, -10)
        give_info.write("Right touched", align='center', font=('Arial', 30, 'bold'))
        give_info.setposition(0, -50)
        give_info.write("NINJA STAR!", align='center', font=('Arial', 30, 'bold'))
        time.sleep(2)
        give_info.clear()
        counter = 10

    if (star.xcor() == -380) and paddle_one.ycor() < star.ycor()+40 and paddle_one.ycor() > star.ycor() - 40:
        left_score = left_score - 2
        score_writer.clear()
        write_score()
        give_info.setposition(0, -10)
        give_info.write("Left touched", align='center', font=('Arial', 30, 'bold'))
        give_info.setposition(0, -50)
        give_info.write("NINJA STAR!", align='center', font=('Arial', 30, 'bold'))
        time.sleep(2)
        give_info.clear()
        counter = 10

    window.onkey(paddle_one_up, "W")
    window.onkey(paddle_one_down, "S")
    window.onkey(paddle_two_up, "Up")
    window.onkey(paddle_two_down, "Down")
    window.listen()

    #KEEPS IN BOUNDARIES
    if ball.ycor() >= 270:
        speedy = speedy * -1
    if star.ycor() >= 270:
        starspeedy = starspeedy * -1
    if ball.ycor() <= -270:
        speedy = speedy * -1
    if star.ycor() <= -270:
        starspeedy = starspeedy * -1

    check_for_right_hit()
    check_for_left_hit()

    #IF PADDLES MISS
    if ball.xcor() >= 400:
        write_miss()
        right_score = right_score - 10
        score_writer.clear()
        write_score()
        ball.setposition(0, 0)
    if ball.xcor() <= -400:
        write_miss()
        left_score = left_score - 10
        score_writer.clear()
        write_score()
        ball.setposition(0, 0)

#FINAL RESULTS
if left_score > right_score:
    give_info.setposition(0, -10)
    give_info.color("green")
    give_info.write("LEFT WINS!", align='center', font=('Arial', 50, 'bold'))
elif right_score > left_score:
    give_info.setposition(0, -10)
    give_info.color("blue")
    give_info.write("RIGHT WINS!", align='center', font=('Arial', 50, 'bold'))
else:
    give_info.setposition(0, -10)
    give_info.color("red")
    give_info.write("TIE GAME!", align='center', font=('Arial', 50, 'bold'))
