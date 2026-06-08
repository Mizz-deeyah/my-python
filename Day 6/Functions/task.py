# def my_function():
#     print("Hello")
#     name = input("your name")
#     print(f"Hello {name}")
#
 # my_function()
#
# def my_item():
#     print("welcome")
#     item = input("your class")
#     print(item)



# temperature = int(input("what is your temperature?"))
# if temperature >= 80:
#     print("critical, shutdown system")
# elif temperature >= 50:
#     print("warning, monitor closely")
# else:
#     print("Safe")
# equipment_name = input("what is your equipment name?")
# status = input("what is the status of the equipment? working or faulty?")
# maintenance = input("what was the last maintenance day?")
# if status == "faulty":
#     print("send maintenance immediately for " + equipment_name)
# elif maintenance > 30:
#     print("Schedule maintenance for" + equipment_name)
# else:
#     print(equipment_name + "is operating normally")


# print("Hello")
# num_char = len("Hello")
# print(num_char)

# def my_function():
#     print("Hello")
#     print("Bye")

# def my_space():
#     print("welcome to my space what would you like to do?")
#     print("bye")
#
#
# my_space()
#

# count = int(input("How many equipment do you want to check?"))
# for i in range (1, count +1):
#        print("equipment", i)
#        name = input("name: ")
#        status= input("status: ")
#        print("Result: ", name, "_", status)

# faulty= 0
# for i in range (5):
#     status = input("Enter equipment status: ")
#     if status == "faulty" :
#         faulty = faulty + 1
# print(faulty, "out of 5 equipment that are faulty")

# equipment = ["pump", "Valve", "Generator", "Compressor"]
# faulty = 0
# for item in equipment:
#     status = input("enter status for " + item +" : ")
#     if status == "faulty":
#         print("ALERT!", item, "is faulty")
#         faulty = faulty + 1

# def my_equipment():
#     faulty = 0
#     for i in range (5):
#         name = (input("enter equipment name: "))
#         status =(input("enter equipment status: "))
#
#         if status == "faulty" :
#             faulty  += 1
#         if faulty > 3 :
#             print("Contact the technician immediately")
#     print(faulty, " out of the 5 equipment that are faulty")

name = {
    "Abdulfatai": "Tall",
    "Abdulazeez":"Chubby",
    "Yakubu": "Slim",
    "Halima":"petite"

}
for key in name:
    print(name[key])

my_equipment()




