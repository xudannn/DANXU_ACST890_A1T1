#Q3
integer = int(input("Please enter an integer:"))

if ((integer%400 == 0) or ((integer%4 == 0) and (integer%100 != 0))): 
        print ("It’s a Leap year")
else: 
     print ("It’s not a Leap year")

#Q4
a = int(input("Please enter an integer a="))
b = int(input("Please enter an integer b="))
import random
print (random.randint(a,b))

#Q5
m = int(input("Please enter an integer m="))
d = int(input("Please enter an integer d="))
if (m == 3 and (d <= 31 and d>=21)):
    print ("True")
elif (m == 4 and (d <= 30 and d>=1)):
    print ("True")
elif (m == 5 and (d <= 31 and d>=1)):
    print ("True")
elif (m == 6 and (d <= 19 and d>=1)):
    print ("True")
else:
	print("False")

#Q6
import math
t = float(input("Please enter the number of years t = "))
P = float(input("Please enter the principla P = "))
r = float(input("Please enter the annual interest rate r = "))
e = math.e
FV = P * (e ** (r * t))
print FV

