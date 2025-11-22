print("Welcome to my Python Program.")

saving = input("How many did you save this month? ")

saving = float(saving)
annually_saving = saving * 12

print(f"You are on track to save ${annually_saving} this year.")

try:
    saving = float(saving)
except ValueError:
    print("Please enter a valid number.")
    exit()