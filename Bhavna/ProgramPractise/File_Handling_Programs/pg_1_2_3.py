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

# 4). Python file program to get the file’s first three and last three lines.
def get_first_last_3lines(filepath):
    file = open(filepath,"r")
    data = file.readlines()
    for i in (data[:3]):
        print(i)

    for i in (data[-3:]):
        print(i)


get_first_last_3lines("Read.txt")

