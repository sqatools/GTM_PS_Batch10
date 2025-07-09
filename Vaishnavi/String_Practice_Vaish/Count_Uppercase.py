str1="Today Is Sunny Day"
count=0
for i in str1:
    if i.isupper():
        count+=1
    else:
        continue
print(count)

#remove duplicate names from string

str2= "Rahul Manoj Nisha Satya Manoj Nisha"
list1=str2.split(" ")
print(list1)
list2=[]

for word in list1:
        if word not in list2:
            list2.append(word)
        else:
            continue
print(str(list2))


#max and min length

str3="we are learning python programming and it is easy to learn"

list1=str3.split(" ")
max_lenght=0
max_word=''

for word in list1:
    word_len=len(word)
    if word_len>max_lenght:
        max_lenght=word_len
        max_word=word
    else:
        continue
print(max_word)


