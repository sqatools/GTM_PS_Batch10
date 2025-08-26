"""
Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5
"""

even=0
odd=0
for i in range (1,10):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even :",even)
print("odd :",odd)

