# HomeWork
"""
# str1 = "Virat is great Indian Player"
output1 = "Player is great Indian Virat"
output2 = "VVirat is great Indian Playerr"
output3 = "VViratt iiss ggreatt IIndiann PPlayerr"
output4 = "(Virat is great): reverse this part : Indian Player"
"""

# output1 = "Player is great Indian Virat"
str1 = "Virat is great Indian Player"
w1 = str1[:5]
w3 = str1[-7:]
w2 = str1[5:-7]
output1 = f"{w3}{w2} {w1}"
print("Output1 :", output1)


print("-"*50)
# output2 = "VVirat is great Indian Playerr"
f_char = str1[0]
l_char = str1[-1]
output2 = f"{f_char}{str1}{l_char}"
print("Output2 :", output2)


print("-"*50)
# str1 = "Virat is great Indian Player"
# output3 = "VViratt iiss ggreatt IIndiann PPlayerr"
w1 = str1[0]+str1[:5]+str1[4]
w2 = str1[6]+str1[6:8]+str1[7]
w3 = str1[9]+str1[9:14]+str1[13]
w4 = str1[-13]+str1[-13:-8]+str1[-9]
w5 = str1[-6]+str1[-6:]+str1[-1]
output3 = f"{w1} {w2} {w3} {w4} {w5}"
print("Output3 :", output3)
# Output3 : VViratt iiss ggreatt IIndiaa PPlayerr


print("-"*50)
# str1 = "Virat is great Indian Player"
# output4 = "(Virat is great): reverse this part : Indian Player"

output_a = str1[-14::-1]
# print(output_a)
output_b = str1[14:]
# print(output_b)
output4 = f"{output_a}{output_b}"
print("Output4 :", output4)
# taerg si tariV Indian Player


print("-"*50)
#Q1 write a python program to get palindrom word from given string.
# palindrome :  if word and reverse of word is same then it is palindrome.
str5 = "eWe Are AAAvAAE ThphT OOPOO LLRLLE"
# output = "eWe ThphT OOPOO"

output = [ ]
word_list = str5.split(" ")
for word in word_list:
    reverse = word[-1::-1]
    print(reverse)
    if word == reverse:
        output.append(word)
    else:
        continue
print("Output :", output)
"""
eWe
erA
EAAvAAA
ThphT
OOPOO
ELLRLL
"""
# Output : ['eWe', 'ThphT', 'OOPOO']

print("-"*50)
#Q2 write a python program count all the vowels from given string.
str6 = "Python Programming"
#output = 4

output = 0
vowels = 'aeiou'
for char in str6:
    if char in vowels:
        output += 1
        print(char)
    else:
        continue
print("Count of vowels :", output)
# Count of vowels : 4