#Python problem 5
#This is a solution to the python guessing game where the user has to guess the randomly generated number between 1 - 10 
#if the number is smaller than the random number then the user will be told the number is too small and vice versa 
#once the user guesses the number they will be told how many tries it took in order for them to win 
#Created by: Robert Kiliszewski	
#04/10/2017

#Imports the random number generator Library
import random

#Assigns a rundom number to a variable
randomNo = random.randint(1,10)

#This is a variable for the user guess amounts
guessNumbers = 1

#Takes the user input
print("Guess The Random Number: ")
guess = input()
guess = int(guess)

#Checks if the number is smaller or greated than the random number generated
if guess > randomNo:
	print ("Guess is too large")
	
if guess < randomNo:
	print ("Guess is too small")

#This while loop is for when the user input is not equal to the number generated	
while guess != randomNo:
	print("Try Again!")
	guess = input()
	guess = int(guess)
	
	guessNumbers = guessNumbers + 1
	if guess > randomNo:
		print ("Guess is too large")
	
	if guess < randomNo:
		print ("Guess is too small")
	
	if guess == randomNo:
		print("Congrats you Won!")
		break
		
#When the user guesses the number it will tell them how many tries it took in order to guess the number
if guess == randomNo:
	guessNumbers = str(guessNumbers)
	print('You guessed the number in ' + guessNumbers + ' guesses!')