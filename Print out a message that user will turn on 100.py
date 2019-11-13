'''
write a program that ask the user to enter their name and age.
print out a message addressed to them that the year that they will turn 100 years old.

'''
import datetime
name = input('enter your name: ')
print('hello',name)
age=int(input('enter your age: '))
year_now=datetime.datetime.now()
print(year_now)
print('you will be turn 100 in',int(100-age)+int(year_now.year))
input()
