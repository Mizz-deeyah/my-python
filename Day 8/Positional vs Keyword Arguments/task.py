# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# functions with input

# def greet_with_name(name, location):
#      print(f"hello,{name}")
#      print(f"what is it like in  {location}")
#
# greet_with(name = "Halima", location =
def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    first_digit = t + r + u + e

    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")
    second_digit = l + o + v + e

    score = str(first_digit) + str(second_digit)
    return score

print(calculate_love_score("halima danjuma", "ali zaki"))

