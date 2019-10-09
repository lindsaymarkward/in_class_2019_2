"""
Do this now
Write a program to create n files, each named like
"file_nn"
i = 5
file_05
"""

NUMBER_OF_FILES = 5
for i in range(NUMBER_OF_FILES):
    with open("file_{:02}".format(i), 'w'):
        pass
