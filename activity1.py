#Take input from the student that he can atteend the exam or not
medical_cause = input("Did you have a medical cause Y or N: ")
#Take input of the attendance
atten = int(input("Enter the attendance of the student:  "))


#Checking the user input predicting output accordingly


if medical_cause == 'Y': #checking the condition 1
    print("Allowed")
else:
    if atten>=75: #checking the condition 2
        print("Allowed")
    else:
        print("Not allowed")