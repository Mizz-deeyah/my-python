# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# tim.speed("fastest")
#
#
# def move_forward():
#     tim.forward(20)
#
#
# def move_backward():
#     tim.backward(20)
#
#
# def turn_left():
#     tim.left(10)
#
#
# def turn_right():
#     tim.right(10)
#
#
# def pen_up():
#     tim.penup()
#
#
# def pen_down():
#     tim.pendown()
#
#
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# # Listen for keyboard presses
# screen.listen()
#
# # Movement keys
# screen.onkeypress(move_forward, "Up")
# screen.onkeypress(move_backward, "Down")
# screen.onkeypress(turn_left, "Left")
# screen.onkeypress(turn_right, "Right")
#
# # Pen controls
# screen.onkeypress(pen_up, "u")
# screen.onkeypress(pen_down, "d")
#
# # Clear screen
# screen.onkeypress(clear_drawing, "c")
#
#
# screen.exitonclick()

# from turtle import Turtle, Screen
# import random
#
# # Create screen
# screen = Screen()
# screen.setup(width=500, height=400)
#
# # Turtle colors and positions
# colors = ["red", "blue", "green"]
# y_positions = [-70, 0, 70]
#
# all_turtles = []
#
# # Create turtles
# for i in range(3):
#     turtle_racer = Turtle(shape="turtle")
#     turtle_racer.color(colors[i])
#     turtle_racer.penup()
#     turtle_racer.goto(x=-230, y=y_positions[i])  # Start from left
#     all_turtles.append(turtle_racer)
#
# # Start race
# race_on = True
#
# while race_on:
#     for turtle in all_turtles:
#
#         random_distance = random.randint(0, 10)
#         turtle.forward(random_distance)
#
#         # Check winner
#         if turtle.xcor() > 220:
#             race_on = False
#             winning_color = turtle.pencolor()
#             print(f"The {winning_color} turtle wins!")
#
# # Keep window open
# screen.exitonclick()

questions = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["A. Lagos", "B. Abuja", "C. Kano", "D. Port Harcourt"],
        "answer": "B"
    },
    {
        "question": "Which language is used for Python programming?",
        "options": ["A. HTML", "B. Java", "C. Python", "D. CSS"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    }
]

score = 0

print("=== WELCOME TO THE QUIZ GAME ===\n")

# Loop through all questions
for i, q in enumerate(questions, start=1):
    print(f"Question {i}: {q['question']}")

    # Display options
    for option in q["options"]:
        print(option)

    # Get user answer
    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    # Check answer
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}\n")

# Final score
print("=== QUIZ COMPLETED ===")
print(f"Your final score is: {score}/{len(questions)}")