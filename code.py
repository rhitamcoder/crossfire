import turtle
import random
import time

screen = turtle.Screen()
screen.title("Crossfire")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

star_drawer = turtle.Turtle()
star_drawer.hideturtle()
star_drawer.penup()
star_drawer.color("white")

for _ in range(100):
    x = random.randint(-390, 390)
    y = random.randint(-290, 290)
    star_drawer.goto(x, y)
    star_drawer.dot(2)

ship = turtle.Turtle()
ship.shape("triangle")
ship.color("green")
ship.shapesize(stretch_wid=1.5, stretch_len=1.5)
ship.penup()
ship.setheading(90)
ship.goto(0, -270)

screen.update()

missile = turtle.Turtle()
missile.shape("triangle")
missile.color("green")
missile.shapesize(stretch_wid=0.5, stretch_len=1)
missile.setheading(90)
missile.penup()
missile.hideturtle()

missile_state = "ready"

def ship_right():
    x = ship.xcor()
    if x < 360:
        ship.setx(x + 20)

def ship_left():
    x = ship.xcor()
    if x > -360:
        ship.setx(x - 20)

def fire_missile():
    global missile_state
    if missile_state == "ready":
        missile.goto(ship.xcor(), ship.ycor() + 10)
        missile.showturtle()
        missile_state = "firing"

def create_alien(x, y):
    alien = turtle.Turtle()
    alien.shape("circle")
    alien.color("green")
    alien.penup()
    alien.goto(x, y)
    return alien

def create_alien_missile(x, y):
    alien_missile = turtle.Turtle()
    alien_missile.shape("circle")
    alien_missile.color("green")
    alien_missile.shapesize(stretch_wid=0.5, stretch_len=1)
    alien_missile.setheading(270)
    alien_missile.penup()
    alien_missile.goto(x, y)
    return alien_missile

alien_missiles = []

def alien_fire():
    if random.randint(1, 200) == 1:
        shooter = random.choice(aliens)
        new_missile = create_alien_missile(shooter.xcor(), shooter.ycor())
        alien_missiles.append(new_missile) 

def flash_ship():
    ship.color("red")
    screen.ontimer(restore_ship, 150)

def restore_ship():
    ship.color("green")

screen.listen()
screen.onkey(ship_right, "Right")
screen.onkey(ship_left, "Left")

screen.onkey(fire_missile, "space")

aliens = []

num_cols = 10
spacing = 70
starting_x = -(spacing * (num_cols - 1)) / 2

for row in range(5):
    for col in range(num_cols):
        x = starting_x + col * spacing
        y = 250 - row * 50
        alien = create_alien(x, y)
        aliens.append(alien)

alien_direction = 1
alien_speed = 2

score = 0

score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-340, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

lives = 3

lives_display = turtle.Turtle()
lives_display.color("white")
lives_display.penup()
lives_display.hideturtle()
lives_display.goto(300, 260)
lives_display.write(f"Lives: {lives}", font=("Arial", 16, "normal"))

game_over = False

try:
    while True:
        time.sleep(0.02)
        screen.update()

        if game_over:
            continue

        if missile_state == "firing":
            missile.sety(missile.ycor() + 10)

            if missile.ycor() > 290:
                missile.hideturtle()
                missile_state = "ready"

        if missile_state == "firing":
            for alien in aliens[:]:
                if abs(missile.xcor() - alien.xcor()) < 20 and abs(missile.ycor() - alien.ycor()) < 20:
                    alien.hideturtle()
                    aliens.remove(alien)
                    missile.hideturtle()
                    missile_state = "ready"
                    score += 10
                    score_display.clear()
                    score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))
                    break

        if len(aliens) == 0:
            game_over == True
            score_display.goto(0, 0)
            score_display.write(f"YOU WIN! Final Score: {score}", align="center", font=("Arial", 24, "normal"))

        for alien in aliens:
            alien.setx(alien.xcor() + alien_speed * alien_direction)

        for alien in aliens:
            if alien.xcor() > 380 or alien.xcor() < -380:
                alien_direction *= -1
                break

        alien_fire()

        for alien_missile in alien_missiles[:]:
            alien_missile.sety(alien_missile.ycor() - 10)

            if abs(alien_missile.xcor() - ship.xcor()) < 25 and abs(alien_missile.ycor() - ship.ycor()) < 20:
                alien_missile.hideturtle()
                alien_missiles.remove(alien_missile)
                lives -= 1
                lives_display.clear()
                lives_display.write(f"Lives: {lives}", font=("Arial", 16, "normal"))
                flash_ship()

                if lives == 0:
                    game_over = True
                    score_display.goto(0, 0)
                    score_display.write(f"GAME OVER - Final Score: {score}", align="center", font=("Arial", 24, "normal"))

                continue

            if alien_missile.ycor() < -300:
                alien_missile.hideturtle()
                alien_missiles.remove(alien_missile)

except turtle.Terminator:
    print("Game window closed.")
except Exception:
    print("Game window closed.")
