# write a python program to convert all the content of the file in upper case.

def convert_to_upper_case(filepath):
    with open(filepath, "r") as file:
        data = file.read()

    upper_case_content = data.upper()

    with open(filepath, "w") as file:
        file.write(upper_case_content)

# convert_to_upper_case("read_data2.txt")


# write a python program to read even number lines from one file and add to another file.
def get_even_file_lines(filepath1, filepath2):
    with open(filepath1) as file:
        # get list of lines
        file_lines = file.readlines()
        print(file_lines)

    with open(filepath2, "a") as file2:
        for i in range(len(file_lines)):
            if (i+1)%2 == 0:
                file2.write(file_lines[i])
            else:
                continue

get_even_file_lines("read_data.txt", "even_lines.txt")


# write a python program to change the upper case to lower case lower to upper.

# write a program to get all the email ids from given file.


