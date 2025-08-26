# Q1 Write a program to get count of upper case characteristics

str1 = "TodaY Is SuNNy Day"
temp = 0
for char in str1:
     if char.isupper():
         temp +=1
         print(char)
     else:
         continue
print("total capital characteristics :",temp)

print("_"*24)



# Q2: write a program to remove duplicate names from given string.

str2 = "Rahul Manoj Nisha Satya Manoj Nisha"

word_list = str2.split(" ")  #splits the sentence into a list of words:
print(word_list)  #['Rahul', 'Manoj', 'Nisha', 'Satya', 'Manoj', 'Nisha']
output = " "
for word in word_list:
    print(word)
    if word not in output:
        output = output + word + " "
        print("output :", output)
    else:
        continue

    print("output :", output) #Rahul Manoj Nisha Satya



print("_"*24)

#################################################
# Q3: write a program to get max length word from given string.

str3 = "We Are Learning Python Programming , Its easy to learn"
# split string with space to get word list

word_list = str3.split(" ")


max_len = 0
max_len_word = ''
for word in word_list:
    word_len = len(word)
    print(word, word_len)
    if word_len > max_len:
        max_len = word_len
        max_len_word= word
    else:
        continue

    print("max len :",max_len)  #11
    print("max_len word :", max_len_word) #Programming




print("_" * 24)

#################################################

#Q.1 write a Python Program to get below output.

str1 = "We Are Learning Python Program"
# output = {'W': 'WWEE', "A": "AArEE", "L": "LLearninGG", "P": "PPythoNN PPrograMM"}

output = {}
# get word with split method and split by space.
word_list = str1.split(" ")
for word in word_list:
    f_ltr = word[0] # first letter
    l_ltr = word[-1] # last letter
    print("Output :", output)
    if f_ltr not in output:
        output[f_ltr] = f"{f_ltr.upper()*2}{word[1:-1]}{l_ltr.upper()*2}"
    else:
        output[f_ltr]  = output[f_ltr] + " " + f"{f_ltr.upper()*2}{word[1:-1]}{l_ltr.upper()*2}"

print("Output :", output)



