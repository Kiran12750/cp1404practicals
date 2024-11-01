# Dictionary of state codes to names
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

print(CODE_TO_NAME)

# Allow lowercase input
state_code = input("Enter short state: ").upper()
while state_code:
    if state_code in CODE_TO_NAME:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Print all states and names
print("\nList of states:")
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")