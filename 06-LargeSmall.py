#Python problem 6
#This program allows the user to input 10 different numbers into a list and at the end it will display the smallest and largest number 
#Created by: Robert Kilisewski	
#04/10/2017

#Create an empty List
numberList = []

print("Enter your numbers: ")

#Loop for user input
for n in range (10):
	numbers = int(input("Enter Number: "))
	
	#This adds all the user input numbers into the list
	numberList.append(numbers)

#pritns the largest and smallest number 
print('The smallest number input = ', min(numberList),'\nThe Largest Number input is = ', max(numberList))
	