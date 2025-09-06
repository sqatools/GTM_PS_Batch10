# File Handling Practice Program

# 31). Python file program to count the total number of Lowercase characters in a file.

def count_lowercase(filepath):
    with open(filepath) as file:
        data = file.read()
        line = data.split()
        count = 0
        for word in line:
            for char in word:
                if char.islower():
                    count+=1

        print("Count:",count)

count_lowercase("count.txt")

print('_'*70)

# 32). Python file program to count the total number of digits in a file.
def count_Digit(filepath):
    with open(filepath) as file:
        data = file.read()
        line = data.split()
        count = 0
        for word in line:
            for i in word:
                if i.isnumeric():
                    count+=1

        print("Count of Digits:",count)

count_Digit("Read.txt")

print('_'*70)


# 42). Python file program to replace space by an underscore in a file.

def new(filepath,filepath2):
    with open(filepath) as file_1:
        data = file_1.read()

    result = data.replace(" ","@")

    with open(filepath2,'w') as file_2:
        file_2.write(result)

new("write.txt","new1.txt")