# Imports
import math

'''
Remember to rename your CW1StudentNumber.py file to your student number

i.e. if your student number is 123456789, then: CW1StudentNumber.py will be renamed 123456789.py

Your student number is typically the first part of your Aston email address i.e. 123456789@aston.ac.uk

'''

# INSERT STUDENT NUMBER HERE

class Coursework1:
    
    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 7, Step A
    #--------------------------------------------------------------------------------------------
    def Lab2Q7a(self, length, width):
        # returns the perimeter of a shape with length: length and width: width
        # (length + width) * 2
        return ((length + width) * 2)
        
    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 7, Step B
    #--------------------------------------------------------------------------------------------
    def Lab2Q7b(self, supergirl, superman):
        #returns the absolute difference between supermans and supergirls age
        return abs(superman - supergirl)
    
    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 7, Step C
    #--------------------------------------------------------------------------------------------
    def Lab2Q7c(self, fact1, fact2):
        # subtracts 2 factorials (fact1! - fact2!)
        return (math.factorial(fact1) - math.factorial(fact2))
    
    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 7, Step D
    #--------------------------------------------------------------------------------------------
    def Lab2Q7d(self, piNum):
        # returns the value of pi to 5sf
        return format(math.pi, ".5f")
    
    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 7, Step E
    #--------------------------------------------------------------------------------------------
    def Lab2Q7e(self, num1, num2):
        # divide 2 positive integers and return the modulus
        return num1%num2
        
    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 7, Step F
    #--------------------------------------------------------------------------------------------
    def Lab2Q7f(self, num):
        # convert a float to its integer value
        return int(round(num,0))

    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 8 (Called for Steps A/B/C)
    #--------------------------------------------------------------------------------------------
    def Lab2Q8(self, num):
        # reformats num (using exponential notation) to
        # output the num with only one significant digit to the left of the decimal point.
        return format(num, ".1e")

    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 9, Step A
    #--------------------------------------------------------------------------------------------
    def Lab2Q9a(self, num):
        # given a float, return the float with three decimal digits of precision
        return format(num, '.3f')
    
    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 9, Step B
    #--------------------------------------------------------------------------------------------
    def Lab2Q9b(self, num):
        # given a float, return the float with three decimal digits of precision including commas
        return format(num, ',.3f')
    
    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 10
    #--------------------------------------------------------------------------------------------
    def Lab2Q10(self, float1, float2):
        # divide the 2 inputs and return the calculated value to exactly two decimal places
        return format((float1/float2), '.2f')
    
    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 11
    #--------------------------------------------------------------------------------------------
    def Lab2Q11(self, float1, float2):
        # divide the 2 inputs and return the calculated value to exactly two decimal places
        # in scientific notation
        return format((float1/float2), '.2e')

    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 12
    #--------------------------------------------------------------------------------------------
    def Lab2Q12(self, utf):
        # For a given UTF-8 value (between 32 and 126), returns the corresponding character
        return chr(utf)
    
    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 13
    #--------------------------------------------------------------------------------------------
    def Lab2Q13(self, total_seconds):
        # convert the input total seconds into hours, minutes and seconds
        #this is done using divide and modulus to get the largest possible amount of hours,minutes and seconds
        hours = total_seconds//3600
        minuites = (total_seconds%3600)//60
        seconds = (total_seconds%3600)%60
        return f"{hours}:{minuites}:{seconds}"
    
    #--------------------------------------------------------------------------------------------
    #Labsheet 2, Question 14
    #--------------------------------------------------------------------------------------------
    def Lab2Q14(self, num1, num2, sign):
        # uses a match-case on the sign to return the correct calculation
        match sign:
            case "+":
                return num1+num2
            case "-":
                return num1-num2
            case "*":
                return num1*num2
            case "/":
                return num1/num2   
            case "//":
                return num1//num2   
            case "%":
                return num1%num2
    #--------------------------------------------------------------------------------------------
    #Labsheet 4, Question 9
    #--------------------------------------------------------------------------------------------
    def Lab4Q9(self, month, requestedLetter):
        # INSERT FUNCTION DESCRIPTION HERE
        return # Return Value

    #--------------------------------------------------------------------------------------------
    #Labsheet 4, Question 10
    #--------------------------------------------------------------------------------------------
    def Lab4Q10(self, start, end):
        # INSERT FUNCTION DESCRIPTION HERE
        return # Return Value
    
    #--------------------------------------------------------------------------------------------
    #Labsheet 4, Question 11
    #--------------------------------------------------------------------------------------------
    def Lab4Q11(self, chorus):
        # INSERT FUNCTION DESCRIPTION HERE
        return # Return Value
    
    #--------------------------------------------------------------------------------------------
    #Labsheet 4, Question 12
    #--------------------------------------------------------------------------------------------
    def Lab4Q12(self, mark):
        # INSERT FUNCTION DESCRIPTION HERE
        return # Return Value
    
    #--------------------------------------------------------------------------------------------
    #Labsheet 4, Question 13
    #--------------------------------------------------------------------------------------------
    def Lab4Q13(self, num):
        # INSERT FUNCTION DESCRIPTION HERE
        return # Return Value
    
##############################################################################
'''
*** Function Calls ***

When you run/excute this Template, the following print() statements will
display the result (return) of your function calls - these results/returns
will be checked for correctness within our Test Program.

Therefore, it is important that you check the results/returns of the below
print() statements, so that you understand what is being returned (and by
extension, what you are being assessed upon)


*** Remember to replace the placeholder paremeter values, WITH YOUR OWN VALUES ***

i.e. change
           print(instance.TestQ(0, 0))
     to
           print(instance.TestQ(5, 5))

(Assuming that you are wanting to pass the vales, 5 and 5, into the function)

'''

instance = Coursework1()

# *** Lab Sheet 2 – Data & Expressions ***
# Function calls for the following questions/tasks and related steps
print(instance.Lab2Q7a(0, 0))
print(instance.Lab2Q7b(50, 0))
print(instance.Lab2Q7c(0, 0))
print(instance.Lab2Q7d(0.0)) 
print(instance.Lab2Q7e(0, 0))
print(instance.Lab2Q7f(0.0))

# Lab 2, Question 8, Steps A - C 
print(instance.Lab2Q8(0.0)) 
print(instance.Lab2Q8(0.0)) 
print(instance.Lab2Q8(0.0))

print(instance.Lab2Q9a(0.0)) 
print(instance.Lab2Q9b(0.0)) 

print(instance.Lab2Q10(0, 0))
print(instance.Lab2Q11(0, 0)) 
print(instance.Lab2Q12(0)) 
print(instance.Lab2Q13(0)) 

# Testing for the 5 operators
print(instance.Lab2Q14(0, 0, 'sign'))
print(instance.Lab2Q14(0, 0, 'sign'))
print(instance.Lab2Q14(0, 0, 'sign'))
print(instance.Lab2Q14(0, 0, 'sign'))
print(instance.Lab2Q14(0, 0, 'sign'))

# *** Lab Sheet 4 – Boolean Expressions / Control Structures ***
# Test calls for the following questions/tasks and related steps
print(instance.Lab4Q9('string', 'character'))
print(instance.Lab4Q10(0, 0))
print(instance.Lab4Q11("string"))

# Testing for the different Degree Classifications
print(instance.Lab4Q12(0)) 
print(instance.Lab4Q12(0)) 
print(instance.Lab4Q12(0)) 
print(instance.Lab4Q12(0)) 
print(instance.Lab4Q12(0)) 
print(instance.Lab4Q12(0)) 

# Testing for the 3 different outcomes of if statement
print(instance.Lab4Q13(0)) 
print(instance.Lab4Q13(0)) 
print(instance.Lab4Q13(0)) 
