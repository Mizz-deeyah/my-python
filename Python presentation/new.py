equip_name = input("Please enter the name of the equipment: ")
status = input("Please enter the status of the equipment (working or faulty): ").lower()
maintenance_input = input("Enter last maintenance (e.g. '2weeks' or '14days'): ").lower()

if "week" in maintenance_input:
    number = int(''.join(filter(str.isdigit, maintenance_input)))
    maintenance = number * 7   # convert weeks to days
elif "day" in maintenance_input:
    number = int(''.join(filter(str.isdigit, maintenance_input)))
    maintenance = number
else:
    maintenance = int(maintenance_input)  # fallback if just a number


if status == "faulty":
    print("Send maintenance officer immediately for " + equip_name)
elif maintenance > 30:
    print("Schedule maintenance officer for " + equip_name)
else:
    print(equip_name + " is operating normally")

def my_equip():
    faulty = 0
    for i in range(5):
        status = input("Enter status (working/faulty): ").lower()
        if status == "faulty":
            faulty += 1
    print("Number of faulty equipment entered:", faulty)

equip5 = {
    "valves": "working",
    "Pumps": "faulty",
    "Tires": "faulty",
    "Motors": "working",
    "Tubes": "working",
}

nested_list = ["A", "B", ["C", "D", ["E", "F", ["G", "H", ["I", "J"]]]]]

equip5_status = {
    "valves": {"working status": 12, "faulty status": 2},
    "Pumps": {"working status": 13, "faulty status": 1},
    "Tires": {"working status": 6, "faulty status": 2},
    "Motors": {"working status": 7, "faulty status": 3},
    "Tubes": {"working status": 8, "faulty status": 4},

}