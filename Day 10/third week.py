import random

def check_guess(guess, secret):
     if guess > secret:
         print("too high, oil production guess is above actual.")
         return False

     elif guess < secret:
         print("too low, oil production guess is below actual.")
         return False
     else:
         print("correct")
         return True
def oil_field_game():
    print("welcome to the oil field guessing game")
    print("guess the hidden oil production number (between 1 and 100)")

    secret = random.randint(1, 100)
    lives = 5
    while lives > 0:
        print(f"\n lives remaining: {lives}")
        try:
            guess = int(input("enter your guess: "))
        except ValueError:
            print("please enter a  valid number")
            continue
        if check_guess(guess, secret):
            break
        else:
            lives -= 1
    if lives == 0:
        print(f" game over,  the correct oil production number {secret}")

oil_field_game()