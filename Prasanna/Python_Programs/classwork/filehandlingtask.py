"""# 3) write a python program to change upper case to lowercase and lower to upper

def swap_case_file(readdata,outputfile):
    with open(readdata, "r") as file:
        data = file.read()

    swapped_content = data.swapcase()

    with open(outputfile, "w") as file:
        outputfile.write(swapped_content)
print(f"Swapped content written to '{outputfile}' successfully.")
"""
# WAP to get the all email IDs from the given file

import re

# Function to extract emails from a file
def extract_emails(input_file):

    with open(input_file, 'r') as file:
        content = file.read()
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)

    if emails:
        print("Email IDs found in the file:")
        for email in emails:
            print(email)
    else:
        print("No email addresses found.")


# Example usage
filename = "sample.txt"  # Make sure this file exists
extract_emails(filename)
