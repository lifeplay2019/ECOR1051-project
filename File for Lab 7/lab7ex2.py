#accept the cost

cost = int(input("Enter cost of your groceries: "))

#first condition

if cost <= 10:

    discount = cost * 0.00

    print("Sorry you win no coupan.")

#second condition

elif cost >= 10 and cost <= 59:

    discount = cost * 0.08

    print("You win a discount of $",discount,". (8 % of your purchase)",sep='')

#third condition

elif cost >= 60 and cost <= 149:

    discount = cost * 0.10

    print("You win a discount of $",discount,". (10 % of your purchase)",sep='')

#fourth condition

elif cost >= 150 and cost <=209:

    discount = cost * 0.12

    print("You win a discount of $",discount,". (12 % of your purchase)",sep='')

#fifth condition

elif cost >= 210:

    discount = cost * 0.14

    print("You win a discount of $",discount,". (14 % of your purchase)",sep='')
    
    