""" Warm up for 01 - Beginnings
Write pseudocode to ask the user for their age and
tell them if they are an adult or child
Write Python code for that
"""

"""
get age
if age > 18
    print adult
else
    print child 
"""

AGE_THRESHOLD = 18

age = int(input("Age: "))
if age >= 18:
    print("Adult")
else:
    print("Child")

number_of_items = 0

print(number_of_items)


def determine_adult(age):
    return age >= AGE_THRESHOLD

