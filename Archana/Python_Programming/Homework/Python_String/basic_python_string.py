# """
# # Home Work
# # str1 = "Virat is greate Indian Player"
# output1 = "Player is greate Indian Virat"
# output2 = "VVirat is greate Indian Playerr"
# output3 = "VViratt iiss ggreatee IIndiann PPlayerr"
# output4 = "(Virat is greate): reverse this part : Indian Player"
# """
# print("#Output 1")
# print("*" * 10)
# str1 = "Virat is great Indian Player"
# # output1 = "Player is great Indian Virat"words
# words = str1.split()  # ['Virat', 'is', 'great', 'Indian', 'Player']
# words[0], words[-1] = words[-1], words[0]
# output1 = ' '.join(words)
# print(output1)
#
# print("-" * 50)
# print("#Output 2")
# print("*" * 10)
# words = str1.split()  # ['Virat', 'is', 'great', 'Indian', 'Player']
# words[0] = 'V' + words[0]
# words[4] = words[4] + 'r'
# output2 = ' '.join(words)
# print(output2)
#
# print("-" * 50)
# print("#Output 3")
# print("*" * 10)
# # output3 = "VViratt iiss ggreat IIndiann PPlayerr"
# str1 = "Virat is great Indian Player"
# # rule: add first letter + word + last letter
# words = str1.split()
# modified_words = []
# for char in words:
#     modified_word = char[0].upper() + char + char[-1].lower()
#     modified_words.append(modified_word)
#
# output3 = ' '.join(modified_words)
# print(output3)
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
#     print("Cannot reverse the word", end=" ")
#
# # 4).Python string program to test whether a passed letter is a vowel or consonant.
#
# vowels = "aeiou"
# str3 = input("Enter the letter:").lower()
# if str3 in vowels:
#     print("The letter is a vowel:", str3)

# 5). Find the longest and smallest word in the input string.
str4 = "This is sentence with long and short words"
words_list = str4.split()
temp_len1 = 0
longest_word = ""
for word in words_list:
    if len(word) > temp_len1:
        temp_len1 = len(word)
        longest_word = word
print("The longest word is:", longest_word)

Short_word = words_list[0]
for word2 in words_list:
    if len(word2) < len(Short_word):
        Short_word = word2
print("The Shortest word is:", Short_word)




