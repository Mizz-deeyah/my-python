# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "you did not provide valid inputs"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result:{formated_f_name} {formated_l_name}"
#
#
# print(format_name(input("what is your first name?"), input("What is yor last name"))

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(2000))