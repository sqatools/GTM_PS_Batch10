######## ASSIGNMENT_3 ###########
"""
# str1 = "Virat is greate Indian Player"
output1 = "Player is greate Indian Virat"
output2 = "VVirat is greate Indian Playerr"
output3 = "VViratt iiss ggreatee IIndiann PPlayerr"
output4 = "(Virat is greate): reverse this part : Indian Player"
"""

str1 = "Virat is great Indian Player"
w1 = str1[:5]
w2 = str1[5:-6]
w3 = str1[-6:]
output1 = f"{w3}{w2}{w1}"
print("Output1:", output1)

f_char = str1[0]
l_char = str1[-1]
output2 = f"{f_char}{str1}{l_char}"
print("Output2:", output2)

a = str1[0]*2+str1[1:4]+str1[4]*2
b = str1[6]*2 + str1[7]*2
c = str1[9]*2 + str1[10:13] + str1[13]*2
d = str1[15]*2 + str1[16:20] + str1[20]*2
e = str1[-6]*2 + str1[-5:-1] + str1[-1]*2
output3 = f"{a}{b}{c}{d}{e}"
print("Output3:", output3)

r1 = str1[13::-1]
r2 = str1[14:28]
Output4 = f"{r1}{r2}"
print("Output4:", Output4)
print('_'*70)

############ Home Work ############

#Q1 write a python program to get palindrom word from given string.
# palindrome :  it word and reverse of word is same then it is palindrome.
str5 = "eWe Are AAAvAAE ThphT OOPOO LLRLLE"
# output = "eWe ThphT OOPOO"

a = str5.split(" ")
# print(a)
palindrome = " "
for char in a:
    if char == char[::-1]:
        palindrome = palindrome+char+" "
        print(palindrome)

print('_'*70)

#Q.2 write a python program count all the vowels from given string.
# str6 = "Python Programming"
#output = 4

str6 = "Python Programming"
A1 = {'A','E','I','O','U','a','e','i','o','u'}
count = 0
for char in str6:
    if char in A1:
        count += 1
        # print(char)
    else:
        continue

print("Output:",count)
print('_'*70)
