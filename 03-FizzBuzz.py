#Fizz Buzz problem. This program does the fizz buzz problem in python where it prints "fizz Buzz" for numbers that are divisible by both 3 and 5 
#It prints "Fizz" for numbers that are only divisble by 3 and "Buzz" for numbers only divisible by 5
#Created by: Robert Kiliszewski
#03/10/2017

for num in range(1,101):

	if num % 5 == 0 and num % 3 == 0:
		print ("FizzBuzz")
		
	elif num % 3 == 0:
		print ("Fizz")

	elif num % 5 == 0:
		print ("Buzz")

	else:
		print (num)