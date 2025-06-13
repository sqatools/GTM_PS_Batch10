# 1.  Python string program to get a string made of 4 copies of the last and first characters
# of a specified string (length must be at least 2).
# str1 = input("Enter the string:")
str1 = "Excellent"
output1 = (str1[0] + str1[-1]) * 4
print(output1)

# 2. find the most simultaneously repeated character in the input string.
str2 = "He is a Excelllent Volley balll player "
max_count = 1
max_repeat_char = ""
temp = 0
for i in range(len(str2) - 1):
    if str2[i] == str2[i + 1]:
        temp += 1
        if temp > max_count:
            max_count = temp
            max_repeat_char = str2[i]
    else:
        temp = 1
print("Max Count:", max_count)
print("Max Char:", max_repeat_char)

# 3. find the most occurance character in the input string.
str2 = "He is a Excelllent Volley balll player "
char_count = {}
max_count = 0
max_repeat_char = ''

for char in str2:
    if char != ' ':  # skip spaces (optional)
        char_count[char] = char_count.get(char, 0) + 1 #char_count.get(char, 0) returns the current count for char, or 0 if it doesn’t exist yet.
        if char_count[char] > max_count:
            max_count = char_count[char]
            max_repeat_char = char

print("Max Count:", max_count)
print("Max Char:", max_repeat_char)

# 4. Calculate the length of a string with loop logic
str3 = "Python is the booming programming language"
count = 0
for char in str3:
    count += 1
print("The length of the string is :", count)

# 5. Replace the second occurrence of a character with $ symbol
str4 = "excellent"
f_occ_char = ""
for char in str4:
    if char in f_occ_char:
        f_occ_char = f_occ_char + "$"
    else:
        f_occ_char = f_occ_char + char
print("The updated code is:", f_occ_char)

# 6. Swap the last character of a string using indexing
str5 = "Program"
print(str5[-1]+str5[1:-1]+str5[0])


l1 = ['a','b','c']
l2 =[2,3]
"output = [('a,2'),('b,3'),('b,2'),('b,3'),('c,2'),('c,3')]"

for i in l1:
    for j in l2:
        print(i,j)


