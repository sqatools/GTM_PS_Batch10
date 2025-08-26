"""Write a program to get all the email id’s from given string using python.
Input str = “”” We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string.”””
Output = [‘john@gmail.com’, ‘ jay@lic.com’, ‘hari@facebook.com’, ‘mery@hotmail.com’ ]"""
str1= """We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com 
we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string."""
word=str1.split()
print(word)
list1=[]
for i in word:
    for k in i:
        if k=='@':
            list1.append(i)
print(list1)
