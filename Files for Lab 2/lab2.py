ECOR 1051 F19 Lab 2 Solutions

Type your solutions to the exercises in the lab handout (file F19_ECOR1051_Lab2.pdf) in the indicated areas.

===========
Exercise 1: 

Copy/paste the two assignment statements from Python Tutor, then answer the questions.
degrees_c=20.0
degrees_f=degrees_c*9/5+32
When does variable degrees_c appear in the diagram?
degrees_c=20.0
What is the name of the frame containing degrees_c ?
Global frame degrees_c=20.0
What does the arrow that points from degrees_c to 20.0 represent?
The arrow represeant that the variable of the degree_c is equal to 20.0 which means that degrees_c's input value is 20.0
When does variable degrees_f appear in the diagram?
degrees_f=68.0
The arrow in degrees_f points to an object. What is the type and value of this object?

===========
Exercise 2:

Copy/paste the two assignment statements from Python Tutor, then answer the questions.
1	mpg=32
2	LITRES_PER_GALLON=4.54609
3	KMS_PER_MILE=1.60934
4	fuel_consumption=(100*LITRES_PER_GALLON)/(mpg*KMS_PER_MILE)

When do the variables and objects appear in the diagram?
variable are the value that could be change which can cause the result get into another solution, so the variable
is mpg.
The objective are the value that do not change or has any kind of effect tothe solution, the objective are 
LITRES_PER_GALLON and KMS_PER_MILE
What are the types and values of the objects?
An object's type is also unchangeable. It determines the operations that an object supports
objective's type is fuel_consumption
value is mpg

===========
Exercise 3:

Copy/paste the five assignment statements from Python Tutor.
principal=1500
rate=0.043
n=4
time=6
amount = principal*(1 + rate/n)**(n*time)
===========
Exercise 4:

What value is bound to c before a = 2 and b = 3 are executed? 
The c value is still 36---- c=36
Does this value change when the two statements are executed?

What value is bound to d before b = 3 is executed? 
d=4
Does this value change when b = 3 is executed?
The value does not change
===========
Exercise 5:

Write a short step-by-step explanation of how Python evaluates the statement x *= x - x
when x is bound to 4.
>>> x = 4 
>>> x  *= x - x
x-x=0
so x*=0
which means that x*0=0
so Global frame x=0	
 


===========
Last edited: Sept. 10, 2019