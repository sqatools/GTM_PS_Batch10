# Q1: write a program to get count of upper case characters.

str1 = "TodaY Is SuNNy Day"
temp = 0
for char in str1:
    if char.isupper():
        temp += 1
        print(char)
    else:
        continue

print("total capital characters :", temp)
# total capital characters : 7


print("_"*50)
#################################
# Q2: write a program to remove duplicate names from given string.

str2 = "Rahul Manoj Nisha Satya Manoj Nisha"
# output = "Rahul Manoj Nisha Satya"
word_list = str2.split(" ")
print(word_list) # ['Rahul', 'Manoj', 'Nisha', 'Satya', 'Manoj', 'Nisha']
output = ""
for word in word_list:
    print(word)
    if word not in output:
        output = output + word + " "
        print("output :", output)
    else:
        continue

print("Output :", output)
# Output : Rahul Manoj Nisha Satya



print("_"*50)
#################################
# Q3: write a program to get max length word from given string.
str3 = "We Are Learning Python Programming , Its easy to learn"
# split string with space to get word list
word_list = str3.split(" ")

max_len = 0
max_len_word = ''
for word in word_list:
    word_len = len(word)
    print(word, word_len)
    if word_len > max_len: # 2 > 0 | 3 > 2 | 8 > 3 | 6> 8 | 11 > 8 | 1> 11 | 3 > 11 | 4> 11 ...
        max_len = word_len # 2, 3, 8, 11
        max_len_word = word # We, Are, Learning, Programming
    else:
        continue

print("Max len :", max_len) # Max len : 11
print("Max len word :", max_len_word) # Max len word : Programming


# ########### Home Work ############
# Q1 write a python program to get palindrome word from given string.
# palindrome :  it word and reverse of word is same then it is palindrome.
str5 = "eWe Are AAAvAAE ThphT OOPOO LLRLLE"
output = "eWe ThphT OOPOO"
words_list = str5.split(" ")
pal_word_count = 0
for char in words_list:
    if char[::-1] == char:
        pal_word_count += 1
        print("The  palindrome word is:", char)
    else:
        continue
print("The number of palindrome words are:", pal_word_count)


# Q2). write a python program count all the vowels from given string.
str6 = "Python Programming"
vowels_list = "aeiou"
# output = 4
count = 0
for char in str6:
    if char in vowels_list:
        count += 1
    else:
        continue
print("Number of vowels:", count)
