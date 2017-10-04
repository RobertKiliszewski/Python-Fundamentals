#Python problem 4
#This is a solution to the python poblem 4 where the prgram displays the factorial for the number 10 and adds all the numbers in the answer.
#Created by Robert Kiliszewski
#01/10/2017

#Import the maths library into the program
import math

print()

#10 Factorial
print ("10! = ",math.factorial(10))
print()
#giving 'n' the value of 10 factorial
myFactorial = math.factorial(10)

# Create a list of integers
# List is populated from a string that contains the long number from 10!
allNumbers = [int(d) for d in str(myFactorial)]

#Prints the list of numbers that are in the answer as an array 
print(allNumbers)
print()

# Print the sum of the digits in the number 10!
print("The sum of all the digits in 10! = ", sum(allNumbers))