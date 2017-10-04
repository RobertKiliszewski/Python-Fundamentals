#Python problem 10
#This program will reverse a string using a function
#Created by: Robert Kiliszewski
#04/10/2017

#https://stackoverflow.com/questions/18686860/reverse-a-string-without-using-reversed-or-1

from collections import deque

print("Choose a word or sentence to reverse: ")
w = input()

def reverse(iterable):
    d = deque()
    d.extendleft(iterable)
    return ''.join(d)

print("Reverse = ", reverse(w))