"""
Ask the user to guess a number between 1 and 10 and keep asking until they get it right.
Use a CONSTANT for the secret number
Just use "? " as the prompt for now
"""

# SECRET_NUMBER = 6
# number = int(input("? "))
# while number != SECRET_NUMBER:
#     print("No")
#     number = int(input("? "))
# print("Right")

# number_of_people = 0
# total = 0
# age = int(input("Age: "))
# while age >= 0:
#     total += age
#     number_of_people += 1
#     age = int(input("Age: "))
# # TODO: use Exceptions
# if number_of_people == 0:
#     print("Not defined")
# else:
#     print(total / number_of_people)
# name = "Lindsay"
# for i in range(0, 130, 40):
#     print("{1:8} {0:3}".format(i, name[i:]))

name = "Lindsay Ward"
for i, character in enumerate(name):
    print("{:2} = {} ({:3})".format(i, character, ord(character)))