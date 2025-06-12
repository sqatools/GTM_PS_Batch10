# 1.  Python string program to get a string made of 4 copies of the last and first characters
# of a specified string (length must be at least 2).
# str1 = input("Enter the string:")
str1 = "Excellent"
output1 = (str1[0]+str1[-1]) * 4
print(output1)

#2. find the most simultaneously repeated character in the input string.
str2 = "He is a Excellent Volley ball player"
max_count = 1
max_repeat_char = ""
temp = 0
print(len(str2))
print(range(len(str2)-1))
for i in range(len(str2)-1):
    if str2[i] == str2[i+1]:
        temp = temp + 1
        if temp > max_count:
            max_count = temp
            max_repeat_char = str2[i]
    else:
        temp = 1
print("Max Count:", max_count)
print("Max Char:", max_repeat_char)
