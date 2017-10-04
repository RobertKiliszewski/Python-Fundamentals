#Python Problem 7
#This sofware asks a user to input a word or words and it checks if the words input are a Palindrome(whether the words are read the same from left to right as right to left)
#Created by: Robert Kiliszewski
#04/10/2017

print()
print("Enter your word you want to check if it's a Palindrome: ")

#user input
wordCheck = input()

wordCheck = wordCheck.casefold()

#Checks if the word is a palindrome
#https://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic
if(wordCheck == wordCheck[::-1]):
	print("This word is a palindrome")

else:
	print("This word is not a palindrome")

