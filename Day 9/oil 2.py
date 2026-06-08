operators ={
    "Aisha": "Night shift",
    "John": "Day shift",
}
equipment =[
    {
    "name":"pump A",
    "temperature":70,
    "pressure":120,
    "status":"working",

},

    {
    "name":"pump B",
    "temperature":60,
    "pressure":90,
    "status": "working",

    },
]




incidents = [
    {
    "equipment":"Generator",
    "issue":"overheating",
    "severity":"high",
    "reported":"Aisha",

}

]

def check_equipment_risk(eq):
    if eq["temperature"] > 80:
        return "HIGH RISK (Temperature critical)"
    elif eq["pressure"] > 150:
        return "HIGH RISK (Pressure critical)"
    elif eq["status"] == "faulty":
        return "INCIDENT REQUIRED"
    else:
        return "ok"

def assign_priority(severity):
    if severity == "high":
        return "Emergency Team Assigned"
    elif severity == "medium":
        return "Maintenance Team Assigned"
    else:
        return "Monitoring Team Assigned"

print("\n EQUIPMENT STATUS  ")
critical_count = 0

for eq in equipment:
    result = check_equipment_risk(eq)
    print(eq["name"],"→", result)

    if "HIGH RISK" in result:
        critical_count += 1
print("\n INCIDENT REPORTS")
print("Total Equipment:", len(equipment))
print("Active Incidents:", len(incidents))
print("Critical Alerts:", critical_count)


