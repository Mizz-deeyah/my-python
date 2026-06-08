def greet():

     print("good morning Halima")
     print("how are you doing Halima?")
     print("what are your plans for today?")

greet()









#functions that allows for input

# def list_of_items(items):
#              print(f"{items}")
# list_of_items("items")

# def life_in_weeks(age):
#      years_left = 90 - int(age)
#      weeks_left = years_left * 52
#      print(f"you have {weeks_left} weeks left")
#
# life_in_weeks(35)

scores = [30, 40, 45, 50, 55, 60, 70, 75]
def analyze_scores(scores):
     highest = scores[0]
     lowest = scores[0]
     total = 0
     passed_count = 0

     # Loop
     for score in scores:
         if score > highest:
             highest = score
         if score < lowest:
             lowest = score
         total += score
         if score >= 50:
             passed_count += 1

     average = round(total / 8)
     print("Highest score:", highest)
     print("Lowest score:", lowest)
     print("Average score:", average)
     print("Number of students passed:", passed_count)

analyze_scores(scores)







# import random
# def guess_number():
#      # generate a random number between 1 and 20
#     target = random.randint(1, 20)
#
#     while True:
#           try:
#             guess = int(input("Guess a number between 1 and 20:"))
#           except ValueError:
#               print("please enter a valid number.")
#
#           if guess > target:
#               print("too high")
#           elif guess < target:
#               print("too low")
#           else:
#               print("correct")
#               break
#
#
# guess_number()