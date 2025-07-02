"""
Different mode to open the file
1. read mode(r) : When we want to read file content , then will open file in read mode.
2. write mode(w): When we want to overwrite existing content with new one, then will open file in write mode
3. Append mode (a): When we want to add content at the end of existing file, then will open file in append mode.
"""

def read_file(filepath):
    file = open(filepath, "r")
    data = file.read()
    print(data)
    file.close()

# read file from current location
# read_file("read_data.txt")

# read file from specific path location
# read_file(r"E:\Filesdata\count_name.txt")


def write_content_to_file(filepath, content):
    file = open(filepath, "w")
    file.write(content)
    file.close()


# 1. file does not exist: write content to the file that does not exist, it will create new file with provided name
#     and content to the file.

user_data = """
We are Learning Python
India is great country
Hope you are doing good
"""

#write_content_to_file("write_data.txt", user_data)


# 2. write to existing file: write content to the exiting file, it will overwrite the existing content of the file.
#

user_data2 = """1. We are Learning Python
2. India is great country
3. Hope you are doing good
4. overwrite existing content
"""

# write_content_to_file("new_data.txt", user_data2)


################################# Append content to the file ############################
def append_content_to_file(filepath, content):
    file = open(filepath, "a")
    file.write(content)
    file.close()

#1. append to non existing file:  It will create new file and add content to that file
#new_data = "We are learning Python and its fresh file\n"
#append_content_to_file("new_append_file.txt", new_data)

# 2. append to existing file:  It will append content to exiting file at the end.
#new_data = "Appending content to existing file\n"
#append_content_to_file("new_append_file.txt", new_data)


###########################################
# context manager :  context has its own enter and exit method internally, once we open file with context manager
# then no need to close explicitly.

def read_with_context_manager(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        print(data)
        print(dir(file))
        print("is file closed in side context manager :", file.closed) # False

    print("is file closed in outside context manager :", file.closed) # True

#read_with_context_manager("read_data.txt")

print("_"*50)
####################### File read options ####################

"""
1.  Read specific numbers bytes data.
2.  Read line  with file.readline()
3.  Read list of lines with file.readlines()
"""


# 1.  Read specific numbers bytes data.
def read_no_of_bytes(filepath, no_of_bytes):
    with open(filepath, "r") as file:
        data = file.read(no_of_bytes)
        print(data)


#read_no_of_bytes("read_data.txt", 20)
# Python is a high-lev


# 2.  Read line  with file.readline()
def read_line_of_file(filepath, line_no):
    with open(filepath, "r") as file:
        print("Is file readable :", file.readable())
        # line1 = file.readline()
        # print(line1)
        # line2 = file.readline()
        # print(line2)
        for _ in range(line_no):
            line = file.readline()
            print(line, end="")


#read_line_of_file("read_data.txt", 2)
"""
1.Python is a high-level, general-purpose
2.programming language. Its design philosophy
"""

print("_"*50)
#########################################
#3.  Read list of lines with file.readlines()

def read_specific_range_of_file(filepath, start, end):
    with open(filepath, "r") as file:
        lines_list = file.readlines()
        print(lines_list)
        for i in range(start-1, end, 1):
            print(lines_list[i], end="")


#read_specific_range_of_file("read_data.txt", 2, 8)



###############################################################
# tell method() :  This method tell you the current location of the cursor
# seek method(bytes, offset) : This method help us to set the cursor position with respect to the offset value.  T

# offset values in seek method
# 0. from start point of the file. e.g. seek(10, 0)
# 1. from current position of the cursor e.g. seek(20, 1)
# 2. end of the file. seek(-50, 2)


def tell_with_seek_method_offset_zero(filepath):
    with open(filepath, "r") as file:
        print("start location :", file.tell())
        file.seek(30, 0) # set new cursor position from begining of the file.
        print("updated location :", file.tell())
        char_20 = file.read(20)
        print("20 chars :", char_20)
        print("new cursor location :", file.tell())


#tell_with_seek_method_offset_zero("read_data.txt")


def tell_with_seek_method_offset_one(filepath):
    with open(filepath, "rb") as file:
        print("start location :", file.tell())
        file.seek(30, 0) # set new cursor position from begining of the file.
        print("updated location :", file.tell())
        file.seek(30, 1)
        print("new location :", file.tell())
        char_10 = file.read(10)
        print("10 characters :", char_10)
        print("new location 2 :", file.tell())


#tell_with_seek_method_offset_one("read_data.txt")



def tell_with_seek_method_offset_two(filepath):
    with open(filepath, "rb") as file:
        print("start location :", file.tell())
        file.seek(-50, 2) # set new cursor position from begining of the file.
        print("updated location :", file.tell())
        char_50 = file.read()
        print("last char50 characters :", char_50)
        print("new location 2 :", file.tell())

tell_with_seek_method_offset_two("read_data.txt")
