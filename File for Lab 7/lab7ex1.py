#Prompting the user to give an input for the bill amount
bill = input("Please enter the bill amount(in $): ");

#Prompting the user to give an input for the satisfaction level
satisfactionLevel = input("\nEnter the satisfaction level( 1= Totally    Satisfied,2=Satisfied, 3=Dissatisfied): ");

#Calculate the tip with respect to the satisfaction level
if (satisfactionLevel == '1'):
    tip = 0.2 * float(bill)
    
elif(satisfactionLevel == '2'):
    tip=0.15*float(bill)

elif(satisfactionLevel == '3'):
    tip=0.1*float(bill)
    
#Printing the Satisfaction Level and the tip
print("\nSatisfaction Level : "+str(satisfactionLevel));
print("\nTip is : $"+str(int(tip))+" and "+str(tip-int(tip))+" cents.");

    