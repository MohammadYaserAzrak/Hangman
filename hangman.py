import turtle


class Hangman:
    def __init__(self) -> None:
        turtle.hideturtle()
        turtle.bgcolor("#CECECE")
        turtle.setup(900, 900)
        turtle.pensize(10)

    def draw_gallows(self):
        turtle.speed(0)
        turtle.color("black")
        turtle.penup()
        turtle.goto(-325, -100)
        turtle.pendown()
        turtle.forward(150)
        turtle.penup()
        turtle.goto(-250, -100)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

    def draw_head(self):
        turtle.speed(2)
        turtle.color("#0000A5")
        turtle.speed(8)
        turtle.penup()
        turtle.goto(-80, 130)
        turtle.pendown()
        turtle.circle(30)

    def draw_body(self):
        turtle.penup()
        turtle.goto(-49, 100)
        turtle.pendown()
        turtle.goto(-49, -40)

    def draw_left_arm(self):
        turtle.penup()
        turtle.goto(-50, 50)
        turtle.pendown()
        turtle.goto(-80, 20)

    def draw_right_arm(self):
        turtle.penup()
        turtle.goto(-50, 50)
        turtle.pendown()
        turtle.goto(-20, 20)

    def draw_left_leg(self):
        turtle.penup()
        turtle.goto(-50, -40)
        turtle.pendown()
        turtle.goto(-80, -70)

    def draw_right_leg(self):
        turtle.penup()
        turtle.goto(-50, -40)
        turtle.pendown()
        turtle.goto(-20, -70)

    def game_won(self, CORRECT_WORD):
        turtle.penup()
        turtle.goto(-50, -200)
        turtle.pendown()
        turtle.write(
            "Congratulations!",
            align="center",
            font=("courier", 24, "bold"),
        )
        turtle.penup()
        turtle.goto(-50, -250)
        turtle.pendown()
        turtle.write(
            f"You guessed the word {CORRECT_WORD}.",
            align="center",
            font=("courier", 24, "bold"),
        )

    def game_lost(self, CORRECT_WORD):
        turtle.penup()
        turtle.goto(-50, -200)
        turtle.pendown()
        turtle.write(
            "You lost!",
            align="center",
            font=("courier", 24, "bold"),
        )
        turtle.penup()
        turtle.goto(-50, -250)
        turtle.pendown()
        turtle.write(
            f"The word was {CORRECT_WORD}.",
            align="center",
            font=("courier", 24, "bold"),
        )
