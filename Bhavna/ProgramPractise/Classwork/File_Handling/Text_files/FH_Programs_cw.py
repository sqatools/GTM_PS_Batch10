# 30/06/2025 session

# write a python program to convert all the content of the file in upper case.

def conver_to_upper(filepath):
    with open(filepath,"r") as file:
        data = file.read()

        upper_case = data.upper()

    with open(filepath,"w") as file:
        file.write(upper_case)

# conver_to_upper("read_data.txt")

# write a python program to read even number lines from one file and add to another file.

def get_even_line(filepath1,filepath2):
    with open(filepath1) as file:
        file_lines = file.readlines()
        print(file_lines)

    with open(filepath2,'a') as file2:
        for i in range(len(file_lines)):
            if (i+1)%2 == 0:
                file2.write(file_lines[i])
            else:
                continue

# get_even_line("read_data.txt","write_data.txt")

# write a python program to change the upper case to lower case lower to upper.

def convert(filepath):
    with open(filepath,'r') as file:
        data = file.read()

    content = data.swapcase()

    with open(filepath,'w') as file:
        file.write(content)

# convert("read_data.txt")

# write a program to get all the email ids from given file.

def email(filepath):
    emails = []
    file = open(filepath,"r")
    data = file.read()
    list = data.split(" ")
    print(list)

    for char in list:
        if "@" in char:
            emails.append(char)
        else:
            continue

    print(emails)
    file.close()
email("Userfile.txt")


