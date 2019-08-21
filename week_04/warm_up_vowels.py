"""
Week 04 warmup
Ask the user for their name
Tell them how many vowels are in their name

Name: Bobby McAardvark
Out of 16 letters, Bobby McAardvark has 4 vowels
"""

VOWELS = "aeiou"
number_of_vowels = 0
name = input("Name: ")
for char in name:
    if char.lower() in VOWELS:
        number_of_vowels += 1
print("Out of {} letters, {} has {} vowels".format(len(name), name, number_of_vowels))
