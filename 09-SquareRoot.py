#Python problem 9
#This program shows how 2 separate functions calculate square roots, one is using the math library in python and the other is using Newtons square root method 
#Created by Robert Kiliszewski
#04/10/2017

import math

x = 100.0

print("Using Math.sqrt() = ", math.sqrt(x))

#Newtons Method for Square Roots
z_next = lambda z: (z - ((z*z - x) / (2 * z)))

repeat = 1.0


while repeat != z_next(repeat):
	repeat = z_next(repeat)
	
print("Using newtons method for square roots", repeat)
