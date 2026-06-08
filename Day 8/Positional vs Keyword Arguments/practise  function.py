def calculate_love_score(name1, name2):
    combined_names =(name1 + name2)
    1 = combined_names.count(1)

    first_digit =

    h = combined_names.count("h")
    a = combined_names.count("a")
    t = combined_names.count("t")
    e = combined_names.count("e")
    second_digit = h+a+t+e

    score = str(first_digit) + str(second_digit)
    return score
print(calculate_love_score(" Halima", "Ali"))
