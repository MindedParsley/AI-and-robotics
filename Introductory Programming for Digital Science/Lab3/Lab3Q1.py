def avg(num1,num2,num3):
    return (num1+num2+num3)/3.0

n1 = 37
n2 = 108
n3 = 67
n4 = 48
n5 = 18
n6 = 6

#a) error as not enough arguments
#result = avg(n1,n2)

#b) works but no output as there is none
avg(n1,n2,n3)

#c) works as it combines the 2 variables into one argument for the function 
# so the 6 turn into the 3 that where needed  
#  but no output again as there is none
result = avg(n1+n2,n3+n4,n5+n6)

#d)returns the value 70.66666666666667 so works
print(avg(n1,n2,n3))

#e) has the correct value of 63.111111111111111
result = avg(n1,n2,avg(n3,n4,n5))