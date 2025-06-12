"""""
A = int(input("Enter the 1st Numbrer :"))
B = int(input("Enter the 2nd Number :"))
print(A+B)
"""""
print("_"*50)
'''
A = int(input("Enter the 1st Numbrer :"))
B = int(input("Enter the 2nd Number :"))
print(A-B)
print("_"*50)
'''

srt1 = "SQATools"
print(srt1 * 5)
print("_"*50)

a = 40
b = 50
c = 30
d = a+b+c
print("The averge of :",d/3)
print("_"*50)

# 6). Python program to get the median of given numbers.
# Note: all the numbers should be arranged in ascending order
# Formula : (n+1)/2
# n = Number of values
N = [40,60, 61, 66, 70, 77, 80]
num = len(N)
median_value = (num+1)//2-1
print("Median is:", N[median_value])
print("_"*50)

# 7). Python program to print the square and cube of a given number.
num1 = 9
print("The square of :",num1*2)
print("The cube of :",num1**3)
print("_"*50)

# 8). Python program to interchange values between variables.
a = 10
b = 20

a,b = b,a
print("a :",a)
print("b :",b)