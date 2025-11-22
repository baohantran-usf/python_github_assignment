#A welcom message
print("Welcome to my Python Program.")

#Define variable
saving = input("How many did you save this month? ")

#Type conversion and Calculation
saving = float(saving) #Convert the variable
annually_saving = saving * 12 #Calculate the amount of annual saving

print(f"You are on track to save ${annually_saving} this year.") #Print the output 

#Handling Error
try:
    saving = float(saving)
except ValueError:
    print("Please enter a valid number.")
    exit()