import os

print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
# with open("test.txt", 'w') as f:
#     pass

for filename in os.listdir('.'):
    if os.path.isdir(filename):
        print(filename)
        continue
    if '.' not in filename:
        os.rename(filename, filename + '.txt')

# os.rename(src, dst)
