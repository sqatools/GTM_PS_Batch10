#String Practice Program

# 25. Check whether the given string is a palindrome (similar) or not.
Input = "sqatoolssqatools"

if Input == Input[::-1]:
    print("The string is Palindrome")
else:
    print("The string is not Palindrome")

print('_'*70)

# 26. Write a program using python to reverse the words in a string.

Input = "sqatools python"
j = Input.split(" ")

print(j[1] + " " +j[0])

print('_'*70)

# 27). Write a program to calculate the length of a string.

Input = "python"
print("Output:",len(Input))

print('_'*70)

# 29). Write a program to combine two strings into one.

# Input:
A = "abc"
B = "def"
C = A + B

print("Output:", C)

print('_'*70)

# 30). Write a program to print characters at even places in a string.
# Input = ‘sqatools’
# Output = saol

c = "sqatools"

for char in range(len(c)):
    if char%2 == 0:
        print(c[char])

print('_'*70)
