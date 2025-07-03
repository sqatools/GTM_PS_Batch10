# File Handling Practice Program

# 1). Python Program How to read a file in reading mode.

def read_file(filepath):
    file = open(filepath,'r')
    data = file.read()
    print(data)
    file.close()

read_file("Read.txt")

print('_'*70)

# 2). Python file program to overwrite the existing file content.

def write_to_existing_file(filepath,content):
    file = open(filepath,'w')
    file.write(content)
    file.close()

userdata = """
1. We cannot solve problems with the kind of thinking we employed when we came up with them. 
2. Learn as if you will live forever, live like you will die tomorrow. 
3. Stay away from those people who try to disparage your ambitions.
4. When you give joy to other people, you get more joy in return.

"""
write_to_existing_file("write.txt",userdata)

print('_'*70)

# 3). Python file program to append data to an existing file.

def append_data_existing_file(filepath,content):
    file = open(filepath,'a')
    file.write(content)
    file.close()

new_data = "Appending content to the existing file"

append_data_existing_file("write.txt",new_data)

print('_'*70)

# 4). Python file program to get the file’s first three and last three lines.
def get_first_last_3lines(filepath):
    file = open(filepath,"r")
    data = file.readlines()
    for i in (data[:3]):
        print(i)

    for i in (data[-3:]):
        print(i)


get_first_last_3lines("Read.txt")
#####################################

print('_'*70)

# 5). Python file program to get all the email ids from a text file.

def email_id(filepath):
    email = []
    file = open(filepath,"r")
    data = file.read()
    list = data.split(" ")
    print(list)

    for char in list:
        if "@" in char:
            email.append(char)
        else:
            continue

    print(email)
    file.close()

email_id("Read.txt")

print('_'*70)

# 6). Python file program to get a specific line from the file.

def line(filepath):
    file = open(filepath,"r")
    data = file.readlines()
    line = data[3]
    print(line)
    file.close()

line("Read.txt")

print('_'*70)

# 7). Python file program to get odd lines from files and append them to separate files.

def odd_lines(filepath1,filepath2):
    with open(filepath1)as file:
        file_lines = file.readlines()
        print(file_lines)

    with open(filepath2,'a') as file2:
        for i in range(len(file_lines)):
            if (i+1)%2 != 0:
                file2.write(file_lines[i])
            else:
                continue

# odd_lines("Read.txt","Write_odd.txt")

print('_'*70)

# 8). Python file program to read a file line by line and store it in a list.

def line_by_line(filepath):
    list = []
    with open(filepath) as file:
        find_lines = file.readlines()
        list.append(find_lines)
        print(list)

line_by_line("Read.txt")

print('_'*70)

