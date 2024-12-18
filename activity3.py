print("Select your ride: ")
print("1. Bike")
print("2. Car")

# Take input of number 1 or 2
#Select your ride
choice = int(input("Enter your choice:  "))


#User entering option 1
if (choice == 1): #condition 1 outer if statement
    print("What type of bike? ")
    print("1. Scooty with gear\n")
    print("2. scooter without gear\n")

#Condition for selecting the type of bike
    choice2=int(input("Enter your choice: "))
    if choice2==1: #inner if statement
        print("You have selected Scooty") 
    else:
        print("You have selected Scooter")

#User entering the option 2
elif(choice==2): #outer elif statement
    print("What type of car? ")
    print("1. Sedan\n")
    print("2. XUV\n")
     