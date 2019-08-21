
numbers = []  # empty list  
subjects = ["CP1404", "CP1804", "CP5632"]

things = ["word", True, 3.14, int(7 / 2), [1, 2, 3], 'z']
for thing in things:
    print(thing, type(thing), end=' ')
print()

"""
Produce output:
1 - CP1404
2 - CP1804
3 - CP5632
"""
# for i in range(len(subjects)):
#     print("{} - {}".format(i + 1, subjects[i]))
for i, subject in enumerate(subjects):
    print("{} - {}".format(i, subject))

subjects.append("MA1000")
print(subjects)

# cp_subjects = []
# for subject in subjects:
#     if subject.startswith("CP"):
#         cp_subjects.append(subject)

cp_subjects = [subject for subject in subjects if subject.startswith("CP")]
print(cp_subjects)

year_numbers = [int(subject[2]) for subject in subjects if subject.startswith("CP")]
print(year_numbers)

# Generator expression (round brackets instead of square; don't store list)
number_of_cp_subjects = sum((1 for subject in subjects if subject.startswith("CP")))
print(number_of_cp_subjects)
