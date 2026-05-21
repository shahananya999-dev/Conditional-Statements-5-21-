#Take input for the student that he can attend the exam or not
medical_cause = input ("Did you have a medical cause? (Y/N): ").strip().upper()

#check the user input and predicting output accordingly 
if medical_cause == 'Y': # Condition 1
    print("You are eligible to take the exam")
    
else:
    #Take input of the attendance
    attendance = int(input("Enter the attendance of the student: "))
    
    if attendance >= 75: #Condition 2
        print("Allowed")
        
    else:
        print("Not Allowed")