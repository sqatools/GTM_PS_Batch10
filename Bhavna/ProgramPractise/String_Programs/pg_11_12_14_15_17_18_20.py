#String practice program

# 11. Write a python program to get to swap the last character of a given string.

str_7 = "SqaTool"
a = str_7[0]
b = str_7[1:7]
c = str_7[-1]
print(f"{c}{b}{a}")

print('_'*70)

# 12. Write a python program to exchange the first and last character of each word from the given string.

str_1 = "Its Online Learning"
h = str_1.split()
print(h)

j = h[0][2]+h[0][1]+h[0][0]
k = h[1][5]+h[1][1:5]+h[1][0]
l = h[2][-1]+h[2][-7:-1:1]+h[2][-8]
print(f"{j} {k} {l}")

print('_'*70)

# 14. Write a python to repeat vowels 3 times and consonants 2 times.

Input = "Sqa Tools Learning"
V = ('a','e','i','o','u')
output = ""
for char in Input:
    if char in V:
        output=output+char*3
    else:
        output=output+char*2
print(output)

print('_'*70)
# 15. Write a python program to re-arrange the string.

Input = "Cricket Plays Virat"
f_word = Input[0:7]
l_word = Input[-6:]
m_word = Input[8:13]

print(f"{l_word} {m_word} {f_word}")

print('_'*70)

# 17. Write a python program to replace the words “Java” with “Python” in the given string.
str_1 = "JAVA is the Best Programming Language in the Market"

output = str_1.replace("JAVA","Python")
print(output)

print('_'*70)

# 18). Write a Python program to get all the palindrome words from the string.
# Input = “Python efe language aakaa hellolleh”
# output = [“efe”, “aakaa”, “hellolleh”]

Input = "Python efe language aakaa hellolleh"
palindrome = " "
a = Input.split(" ")
print(a)

for char in a:
    # print(char
    if char == char[::-1]:
        palindrome = palindrome + char + " "

print("Output:", palindrome)

print('_'*70)

# 20). Write a Python program to remove duplicate words from the string.
str_i = "John jany sabi row john sabi"
a = str_i.split(" ")
print(a)
output = ""

for word in a:
    # print(word)
    if word not in output:
        output = output+word+" "
        print(output)
    else:
        continue

print('_'*70)

