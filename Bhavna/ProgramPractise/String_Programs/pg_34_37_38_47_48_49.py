#String Practice Programs

# 34). Write a program to print characters at odd places in a string.
# Input = ‘abcdefg’
# Output = ‘bdf’

input = "abcdefg"

for i in range(len(input)):
    if i%2 != 0:
        print(input[i],end=" ")
print()
print('_'*70)

# 37). Write a program to exchange the first and last letters of the string
# Input = We are learning python
# Output = ne are learning pythoW

Input = "We are learning python"
ft = Input[0]
lt = Input[-1]
mt = Input[1:-1]
print(f"{lt}{mt}{ft}")

print('_'*70)

# 38). Write a program to convert all the characters in a string to Upper Case.

Input = "I live in pune"
print(Input.upper())

print('_'*70)

# 47). Write a program to get the first 4 characters of a string.

Input = "Sqatools"
print(Input[0:4])

print('_'*70)

# 48). Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
Input = "Sqatools"
a = Input[:2]
b = Input[-2:]
print("Output:", a+b)

print('_'*70)

# 49). Write a python program to print the mirror image of the string.

Input = "Python"
print(Input[::-1])

print('_'*70)
