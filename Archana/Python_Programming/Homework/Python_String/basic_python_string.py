# """
# # Home Work
# # str1 = "Virat is greate Indian Player"
# output1 = "Player is greate Indian Virat"
# output2 = "VVirat is greate Indian Playerr"
# output3 = "VViratt iiss ggreatee IIndiann PPlayerr"
# output4 = "(Virat is greate): reverse this part : Indian Player"
# """
# # Output1:Player is great Indian Virat
# print("#Output 1")
# print("*" * 10)
# str1 = "Virat is great Indian Player"
# wrd1 = str1[:5]
# wrd2 = str1[-6:]
# wrd3 = str1[5:-6]
# str2 = wrd2 + wrd3 + wrd1
# print(str2)
#
#
# # output2 = "VVirat is greate Indian Playerr"
# print("-" * 50)
# print("#Output 2")
# print("*" * 10)
# str1 = "Virat is great Indian Player"
# wrd4 = str1[0]
# wrd5 = str1[-1]
# output2 = wrd4 + str1 + wrd5
# print(output2)
#
# # output3 = "VViratt iiss ggreat IIndiann PPlayerr"
# print("-" * 50)
# print("#Output 3")
# print("*" * 10)
# str1 = "Virat is great Indian Player"
# # rule: add first letter + word + last letter
# # Manually slice out each word based on known positions
# w1 = str1[0:5]  # Virat
# w2 = str1[6:8]  # is
# w3 = str1[9:14]  # great
# w4 = str1[15:21]  # Indian
# w5 = str1[22:]  # Player
#
# # Build output using rule: first letter + word + last letter
# output3 = w1[0] + w1 + w1[-1] + " " + \
#           w2[0] + w2 + w2[-1] + " " + \
#           w3[0] + w3 + w3[-1] + " " + \
#           w4[0] + w4 + w4[-1] + " " + \
#           w5[0] + w5 + w5[-1]
#
# print(output3)
#
# #output4 = "(Virat is great): reverse this part : Indian Player"
# print("-" * 50)
# print("#Output 4")
# print("*" * 10)
# str1 = "Virat is great Indian Player"
# wd1 = str1[0:14]
# wd2 = str1[14:]
# output4 = wd1[::-1] + wd2
# print(output4)
#
#
# # .1). Write a Python program to get a string made of the
# # first and the last 2 chars from a given string.
# # If the string length is less than 2,
# # return instead of the empty string
# str1 = input("Enter the String:")
# if len(str1) > 2:
#     new_str = str1[:2] + str1[-2:]
#     print(new_str)
# else:
#     print("Cannot make a new word", end=" ")
#
# # 2). Python string program that takes a list of strings and returns the length of the longest string.
#
# str_list1 = ["Apple", "Banana", "Jack Fruit", "Strawberry", "Raspberry"]
# temp_len = 0
# for word in str_list1:
#     if len(word) > temp_len:
#         temp_len = len(word)
#         longest = word
# print("The Length of longest string is:", temp_len)
# print("The longest string is:", longest)
#
# # 3). Python string program to reverse a string if it’s length is a multiple of 4.
# str2 = input("Enter the String:")
# len_str2 = len(str2)
# if len_str2 % 4 == 0:
#     print(str2[::-1])
# else:
#     print("Cannot reverse the word")
#
# # 4).Python string program to test whether a passed letter is a vowel or consonant.
#
# vowels = "aeiou"
# str3 = input("Enter any letter:").lower()
# if str3 in vowels:
#     print(f"The letter {str3} is a vowel")
# else:
#     print(f"The letter {str3} is not a vowel")
#
# # 5). Find the longest and smallest word in the input string.
# str4 = "This is sentence with long and short words"
# words_list = str4.split()
# temp_len1 = 0
# longest_word = ""
# for word in words_list:
#     if len(word) > temp_len1:
#         temp_len1 = len(word)
#         longest_word = word
# print("The longest word is:", longest_word)
#
# Short_word = words_list[0]
# for word2 in words_list:
#     if len(word2) < len(Short_word):
#         Short_word = word2
# print("The Shortest word is:", Short_word)
#
# # 6). Write a python program to replace the words “Java” with “Python” in the given
# # Input = “JAVA is the Best Programming Language in the Market”
# # Output = “Python is the Best Programming Language in the Market”
# in_str = "JAVA is the Best Programming Language in the Market"
# new_word = in_str.replace("JAVA", "Python")
# print(new_word)
#
# # # 7). Python string program to get a string made of 4 copies of the
# # # last two characters of a specified string (length must be at least 2).
# # str4 = input("Enter the string:")
# # print(str4[-2:]*4)
#
# # 8). Python string program to count occurrences of a substring in a string.
# str4 = "school"
# sub_string = "ol"
# # Printing output
# count = str4.count(sub_string)
# print(count)

# 9) Python program to find the count of palindrome words in a  given string

str_1 = "The ewe ara madam copy tamat sihthis lebel in cat"
words_list = str_1.split(" ")
pal_word_count = 0
for char in words_list:
    if char[::-1] == char:
        pal_word_count += 1
        print(" The  palindrome word is:", char)
    else:
        continue
print(" The number of palindrome words are:", pal_word_count)

