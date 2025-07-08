# write a python program to convert all the content of the file in upper case.

def convert_to_upper_case(filepath):
    with open(filepath, "r") as file:
        data = file.read()

    upper_case_content = data.upper()

    with open(filepath, "w") as file:
        file.write(upper_case_content)

convert_to_upper_case("read_data2.txt")