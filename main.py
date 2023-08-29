#####################Bell Ringer#######################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it


# Familiarize yourself with the syntax of the print() function.
# Print your name.
# Print today's date.
# Print the name of your favorite movie.

# Print your name and age on separate lines using a single print() function.
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."


###########################end bell ringer##################################

#work on other file


print('hello world')






###########################String Practice##################################
#syntax is the way we write code
# print("Hello World")
# name = "John"
#in other languages, this is different
# in javascript for example, you define
#variabes with let or const or var
#in python, you just give your variables a
#name and then define it with a value
word = "python is cool and stuff  " #string variable
print(word)
print(word[0]) #prints the first letter of the string variable
print(word[13]) # prints out the 13th letter of the string variable
print(word[19])
print(word[23])
print(word[-1])
print(word[-2])
print(word[-3])
print(word[10:14]) # string slicing, 10 is inclusive, 14 is exlusive
print(word[19:24])
print(word[0:6])
print(word[7:9])
print(word[15:18])
print(word[ :-1 ]) #prints all word
print(len(word)) #prints length of sentence,all letters.
print(word[5:]) #excludes the first 5 letters
#what if i wanted to find a substring?
# a subtring is a word inside of a sentence
print(word.find('is')) #gives you where the word is a, finds the index of a substring
print(word.find('and'))
# how do we uppercase letters?
print(word.upper())
print(word.capitalize()) # this capitalizes the first letter 

cool = word[10:14]
print(cool)
print(cool.capitalize())

print(word.replace('python', 'javascript'))
print(word.replace('cool', 'ugly'))
print()

#challenge
# find a summary of blue beetle online and create a 
# variable called blue_beetle_summary and print it
# hint: google it
# print the length of the summary
# upper case the entire summary
# print the summary
# print the summary in lowercase
# replace the word blue with red
# print the summary
# string index the word beetle and print it out
# print the last word of the summary
# print the summary in reverse

blue_beetle_summary = "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle."

print(blue_beetle_summary)
print(len(blue_beetle_summary))
print(blue_beetle_summary.upper())
print(blue_beetle_summary.lower())
print(blue_beetle_summary.replace('Blue', 'Red'))
print(blue_beetle_summary.find('Beetle'))
print(blue_beetle_summary[-7:]) #or 334
print(blue_beetle_summary[::-1])

# String Practice #1: try this in repl.it
# Define a string containing your full name.
# Print the first 3 letters of your name using string slicing.
# Convert your name to uppercase and print the result.
# Use string formatting to print "My name is [Your Name]."

# String Practice #2
# Write Python code that prints the following, by calling the print function just once:
# Line 1
# Line 2
# Line 3

# String Practice #3
# Write Python code that prints the following:
# A	B	C
# D	E	F
# G	H	I

# String Practice #3
# Write Python code that prints the following:
# Backslash (\)
# Forward Slash (/)

##########################input practice#############################################
# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.

# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.


###########################time for a real challenge!!!!##################################
# last slide