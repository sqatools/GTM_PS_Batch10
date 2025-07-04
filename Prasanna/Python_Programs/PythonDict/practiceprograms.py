# q1 get the value
list1 = [4, 6, 8, 12, 67, 34, 50, 60, 70]
output1 = []
for value in list1:
    if 10 <= value <= 50:
        output1.append(value)
print(output1)
# Q 2)
str1 = "we are learning Python Programming"
word_list = str1.split()
max_len = ""
second_max_len_word = ""
print(word_list)
for word in word_list:
    if len(word) > len(max_len):
        second_max_len_word = max_len
        max_len = word
    elif len(word) > len(second_max_len_word) and word != max_len:
        second_max_len_word = word
print("First and second Maximum length of word are:", word, second_max_len_word)