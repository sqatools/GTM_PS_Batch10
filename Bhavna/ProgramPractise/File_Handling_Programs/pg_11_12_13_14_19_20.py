# File Handling Practice Program

# 11). Python file program to read a random line from a file.
import random

def read(filepath):
    with open(filepath,"r") as file:
        data = file.read()
        line = data.splitlines()
        output = random.choice(line)
        print(output)

read("Read.txt")

print('_'*70)

# 12). Python file program to copy the file’s contents to another file after converting it to lowercase.

def lowercase_file(filepath1,filepath2):
    with open(filepath1,'r') as file1:
        data = file1.readlines()
        print(data)

    with open(filepath2,"a") as file2:
        for i in data:
            file2.write(i.lower())

# lowercase_file("Read.txt","lowercase.txt")

print('_'*70)
# 13). Python file program to copy the file’s contents to another file after converting it to uppercase.

def uppercase_file(filepath1,filepath2):
    with open(filepath1,'r') as file:
        lines = file.readlines()
        print(lines)

    with open(filepath2,'w') as file2:
        for j in lines:
            file2.write(j.upper())

uppercase_file("Read.txt","uppercase.txt")

print('_'*70)

# 14). Python file program to count all the words from a file.
def count(filepath):
    with open(filepath) as file:
        data = file.read()
        c = 0
        word = data.split()
        for char in word:
            c+=1
        print("count of all words",c)

count("Read.txt")

print('_'*70)

# 19). Python file program to get all odd and even length words in two lists.

def even_odd(filepath):
    with open(filepath,"r") as file:
        data = file.read()
        line = data.split()
        even = []
        odd = []

        for word in line:
            if len(word)%2 == 0:
                even.append(word)
            else:
                odd.append(word)

        print("Even list:",even)
        print("Odd list:",odd)

even_odd("Write_odd.txt")

print('_'*70)

# 20). Python file program to get all mobile numbers from a file. e.g each mobile number size should be 10.
def mobile_no(filepath):
    with open(filepath) as file:
        data = file.read()
        lines = data.split()
        Mobile_number = []

        for i in lines:
            if i.isnumeric():
                if len(i) == 10:
                    Mobile_number.append(i)

        print("Mobile Numbers:",Mobile_number)

mobile_no("Read.txt")

print('_'*70)

