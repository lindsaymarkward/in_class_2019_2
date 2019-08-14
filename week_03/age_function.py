""" Functions demos """


# original from week 1
# age = int(input("Age: "))
# if age >= 18:
#     print("Adult")
# else:
#     print("Child")


def main():
    age = int(input("Age: "))
    print("Adult" if is_adult(age) else "Child")

    # By removing the English interface (input prompts and prints)
    # we can make our interface whatever language we want
    if is_adult(age):
        print("matanda")  # in Filipino

    # By not getting user input inside the function
    # we can use whatever inputs we want from whatever source
    ages = [1, 34, 0]
    number_of_children = 0
    for age in ages:
        if not is_adult(age):
            number_of_children += 1

    print("There are {} kids".format(number_of_children))


def is_adult(age):
    """Determine if age represents an adult."""
    if age >= 18:
        return True
    else:
        return False


main()

# DTN
# def count_letters(string):
#     """Count the letters in string."""
#     count = 0
#     for character in string:
#         if character.isalpha():
#             count += 1
#     return count
#
#
# print(count_letters("abcD  1"))
