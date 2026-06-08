equipment_list = []

# Step 1: Ask number of equipment
num = int(input("How many equipment do you want to monitor? "))

# Step 2: Collect data for each equipment
for i in range(num):
    print(f"\nEquipment {i + 1}")

    name = input("Name: ")
    temperature = float(input("Temperature: "))
    pressure = float(input("Pressure: "))
    status = input("Status (OK/FAULT): ").upper()

    # Store each equipment as a dictionary
    equipment = {
        "name": name,
        "temperature": temperature,
        "pressure": pressure,
        "status": status
    }

    # Add to list
    equipment_list.append(equipment)

# Step 3: Initialize counters
faulty_count = 0
high_temp_count = 0

print("\n--- EQUIPMENT STATUS ---")

# Step 4: Analyze equipment and generate alerts
for eq in equipment_list:
    alert = []

    if eq["temperature"] > 100:
        alert.append("HIGH TEMP ALERT")
        high_temp_count += 1

    if eq["status"] == "FAULT":
        alert.append("FAULT ALERT")
        faulty_count += 1

    if len(alert) == 0:
        print(f'{eq["name"]} → OK')
    else:
        print(f'{eq["name"]} → {" + ".join(alert)}')

# Step 5: Final Summary Report
print("\n--- SUMMARY ---")
print("Total:", num)
print("Faulty:", faulty_count)
print("High Temp:", high_temp_count)