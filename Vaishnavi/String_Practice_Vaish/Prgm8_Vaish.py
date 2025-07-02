"""Print most simultaneously repeated characters in the input string."""

str1=input("enter the string")
list1=str1.split()
print(str1)

for word in list1:
    new_word=word[-1]+word[1:-1]+word[0]
    index1=list1.index(word)
    list1[index1]=new_word
print(list1)