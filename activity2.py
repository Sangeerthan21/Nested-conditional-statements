#Take input of the number of units consumed by the user
units = int(input("Enter the number of units you consumed:  "))

# Checking conditions of the amounts consumed
# Then calculate the amount and surcharge accordingly
# surcharge is the tax value

# Checking for units less than 50
if(units < 50):
    amount = units * 2.60
    surcharge = 25

# Checking for units less than 100
if(units < 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 45

# Checking for units less than or equal to 200
if(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45

#Checking for all the cases other than mentioned
# When units consumed are more than 200
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75


# Calculate and Display the total electricity bill
# Total amount = amont + surcharge
total = amount + surcharge
print("\nElectricity Bill = %.2f"  %total)