# Q1: write a program to get count of upper case characters.

str_1 = "Today Is SuNny DaY"
a = 0
for char in str_1:
    if char.isupper():
        # print(char)
        a += 1
    else:
        continue

print("Total Uppercase Character:", a)

print('_'*70)

# Q2: write a program to remove duplicate names from given string.

str_2 = "Alia Asha Rina Ravi Asha Rina Rita"

word_list = str_2.split(" ")
print(word_list)
output = ""

for word in word_list:
    print(word)
    if word not in output:
        output= output+word+" "
        print("output:", output)
    else:
        continue

# output: Alia Asha Rina Ravi Rita
print('_'*70)

# Q3: write a program to get max length word from given string.
str_3 = "The time is always right to do what is right."

word_list = str_3.split(" ")
# print(word_list)
max_len = 0
max_len_word = ''
for word in word_list:
    word_len = len(word)
    print(word, word_len)
    if word_len > max_len:
        max_len = word_len
        max_len_word = word
    else:
        continue

print("max len:", max_len)
print("Max len word:", max_len_word)

print('_'*70)

str3 = "We Are Learning Python Programming , Its easy to learn"
# split string with space to get word list
word_list = str3.split(" ")

max_len = 0
max_len_word = ' '
for word in word_list:
    word_len = len(word)
    print(word, word_len)
    if word_len > max_len: # 2 > 0 | 3 > 2 | 8 > 3 | 6> 8 | 11 > 8 | 1> 11 | 3 > 11 | 4> 11 ...
        max_len = word_len # 2, 3, 8, 11
        max_len_word = word # We, Are, Learning, Programming
    else:
        continue

print("Max len :", max_len) # Max len : 11
print("Max len word :",max_len_word) # Max len word : Programming

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
############################
# 10/06/2025 Session
#Q.1 write a Python Program to get below output.

str1 = "We Are Learning Python Program"
# output = {'W': 'WWEE', "A": "AArEE", "L": "LLearninGG", "P": "PPythoNN PPrograMM"}

output = {}
# get word with split method and split by space.
word_list = str1.split(" ")
for word in word_list:
    f_ltr = word[0]
    l_ltr = word[-1]
    print("Output:",output)
    if f_ltr not in output:
        output[f_ltr] = f"{f_ltr.upper()*2}{word[1:-1]}{l_ltr.upper()*2}"
    else:
        output[f_ltr]  = output[f_ltr] + " " + f"{f_ltr.upper()*2}{word[1:-1]}{l_ltr.upper()*2}"

    print("Output:", output)
