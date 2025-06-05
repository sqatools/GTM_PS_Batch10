# 1.Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python


for i in range(8):  # range(8) gives numbers from 0 to 8
    if i == 3 or i == 8:
        continue  # Skip 3 and 8
    print(i, end = "") # 0124567

print ("*"* 50)

# 2.Write a program to add odd numbers in an empty list from a given list using Python Loop

list1 = [3, 8, 5, 0, 2, 7, 10, 9]
odd = []
for l in list1:
    if l % 2 !=0:
        odd.append(l)
        print(odd) # [3, 5, 7, 9]

print ("*"* 50)

# 3.Write a program to add even numbers in an empty list from a given list using Python Loops.

list2 = [3, 8, 5, 0, 2, 7, 10, 9, 15, 11, 22]
even = []
for v in list2:
    if v % 2 == 0:
        even.append(v)
        print(v)
        print(even) # [8, 0, 2, 10, 22]

print("*"* 50)
# 4.Write a program to print the days in a week except Sunday using a while loop in Python.

days = ["Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in days:
    if day != "Sunday":
        print(day, end =" ") # Monday Tuesday Wednesday Thursday Friday Saturday



print("*"* 50)

#5. Write a program to print the first 20 natural numbers using a while loop in Python.
##The loop continues as long as n is less than or equal to 20.
##Each iteration prints n and then increases it by 1.
## Will stops when a becomes greater than 20



a = 1
while a  <= 20:
    print(a, end = " ") # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    a +=1

print("*"* 50)
# Example 2

a = 1
while a <= 20:
    print(a, end = " ")  # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 will run nonstop
    # a +=1

    # # Missing: a += 1
    # It prints 1 forever and never stops

print("*"*50)



