"""Python function program to check whether a number is in a given range.
Input : num = 7, range = 2 to 20
Output: 7 is in the range"""

def Range_fuc(num):
    for i in range(2,21,1):
        if num==i:
            print(f"{num} is in range")
        else:
            continue

Range_fuc(71)