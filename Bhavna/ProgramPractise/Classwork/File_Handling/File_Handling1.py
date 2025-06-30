# 28/06/2025 Session
'''
Different mode to open file
1. read mode(r): When we want to read file content then will open in read mode
2. write mode(w): when we want to overwrite exisiting content with new one, then will open file in write mode
3. Append mode (a): When we want to add content at the end of existing file, then will open file in append mode.

'''

def read_file(filepath):
    file = open(filepath,'r')
    data = file.read()
    print(data)
    file.close()

# read file from the current location
# read_file("read_data.txt")

# read file from the specific path location
# read_file(r"D:\read.txt")


def write_content_to_file(filepath,content):
    file = open(filepath,'w')
    file.write(content)
    file.close()

# 1. File does not exist: write content to the file that does not exist
# it will create new file provided name and add content to the file

user_data = """
Hi
we are learning python
hope you are understanding and enjoying the course
"""
# write_content_to_file("write_data.txt",user_data)

# 2. write to existing file: write content to the existing file, it will overwrite the existing content of the file.


user_data1 = """
1.Believe in yourself, and you will achieve great things.
2.A smile is the best gift you can give to others.
3.Every day is a new chance to be kind and helpful.
4.Small actions can make a big difference.
5.Work hard, and success will follow.
6.Being honest makes you strong and trusted.
"""
# write_content_to_file("write_data2.txt",user_data1)


#################Append content to the file#############

def append_content_to_file(filepath,content):
    file = open(filepath,'a')
    file.write(content)
    file.close()

# 1. Append to non existing file: it will create new file and add content to that file.

# new_data = "Best Thoughts of the day\n"
# append_content_to_file("new_append_file.txt",new_data)

# 2. Append to the existing file: it will append content to that existing file.

new_data = "Appending content to the existing file\n"
append_content_to_file("new_append_file.txt",new_data)


##########################
# Context Manager: context has its own enter and exit method internally, once we open file with context manager
# ten no need to close file explicitly.

def read_with_content_manager(filepath):
    with open(filepath,"r") as file:
        data = file.read()
        print(data)
        print("is file closed inside context manager:",file.closed)

    print("is file closed outside context manager:",file.closed)

read_with_content_manager("read_data.txt")

print('_'*70)
####################File read option ###########

"""
1. Read specific number bytes data
2. Read line with file.readlines()
3. Read list of lines with file.readlines()
"""

#  1. Read specific number bytes data
def read_of_bytes(filepath, no_of_bytes):
    with open(filepath,"r") as file:
        data = file.read(no_of_bytes)
        print(data)

# read_of_bytes("read_data.txt",20)

# 2. Read line with file.readlines()

def read_line_of_file(filepath,line_no):
    with open(filepath,"r") as file:
        print("Is file readable:",file.readable())
        # line1 = file.readline()
        # print(line1)
        # line2 = file.readline()
        # print(line2)
        for _ in range(line_no):
            line = file.readline()
            print(line,end="")

read_line_of_file("read_data.txt",3)

#######################################

# 3. Read list of lines with file.readlines()

def read_specific_range_of_file(filepath,start,end):
    with open(filepath,"r") as file:
        lines_list = file.readlines()
        print(lines_list)
        for i in range(start-1,end,1):
            print(lines_list[i],end="")

read_specific_range_of_file("read_data.txt",2,4)

print('_'*70)

# Tell method(): thus method tell you thr current location of the cursor.
#seek method(bytes, offset): This method helps us to set the cursor position with respect the offset value.

# offset values in seek method
# 0. from start point of the file. seek(10,0)
# 1. from current position of the cursor. seek (20,1)
# 2. end of the file seek(-50,2)