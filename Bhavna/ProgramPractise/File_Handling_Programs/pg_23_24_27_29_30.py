# File Handling Practice Program

# 23). Python file program to count the number of lines in a file.
def count(filepath):
    with open(filepath) as file:
        data = file.readlines()
        c = 0

        for line in data:
            c+=1
        print("count:",c)

count("write.txt")
print('_'*70)
# 24). Python file program to get the file size of a file.
import os
file_path = r"C:\AutomationCourse\GTM_PS_Batch10\Bhavna\ProgramPractise\File_Handling_Programs\Read.txt"
print("File Size:",os.path.getsize(file_path))

# OR
print("File size2:",os.path.getsize("Read.txt"))

print("_"*70)

# 27). Python file program to extract characters from a text file into a list.

def list(filepath):
    with open(filepath) as file:
        data = file.read()
        line = data.split()
        list1 = []

        for word in line:
            for i in word:
                list1.append(i)

        print("Characters:",list1)

list("Read.txt")

print('_'*70)

# 29). Python file program to count the total number of characters in a file.
def count(filepath):
    with open(filepath) as file:
        data = file.read()
        line = data.split()
        c = 0

        for word in line:
            for char in word:
                if char.isalpha():
                    c+=1

        print("count:",c)

count("Read.txt ")

print('_'*70)
# 30). Python file program to count the total number of Uppercase characters in a file.

def count_uppercase(filepath):
    with open(filepath) as file:
        data = file.read()
        line = data.split()
        count = 0
        for word in line:
            for char in word:
                if char.isupper():
                    count+=1
        print("Count:",count)

count_uppercase("count.txt")

