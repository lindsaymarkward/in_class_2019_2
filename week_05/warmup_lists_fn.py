"""
Write code for a function that takes two lists:
- a list of names
- a corresponding list of ages
(That is, elements at the same list index represent the same person.)
The function should return the name of the oldest person in the list.
(Return the first name if multiple people have the same oldest age.)
"""


def main():
    # first_names = []
    # numbers = []
    first_names = ["A", "B", "C", "D"]
    numbers = [3, 1, 0, 2]
    print(find_oldest_name(first_names, numbers))


def find_oldest_name(names, ages):
    if not ages:
        return None
    index_of_oldest = 0
    age_of_oldest = ages[0]
    for i, age in enumerate(ages[1:], 1):
        if age > age_of_oldest:
            index_of_oldest = i
            age_of_oldest = age
    return names[index_of_oldest]


if __name__ == '__main__':
    main()
