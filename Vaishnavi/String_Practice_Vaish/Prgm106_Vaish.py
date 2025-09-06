"""Input str = “”” We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed
2312245566 we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string.”””
Output = [‘8988858683’, ‘2312245566’, ‘4532892234’, ‘9999234355’]"""

str1="""We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 
2312245566 we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string."""
list1=str1.split()
list2=[]
for word in list1:
    if word.isnumeric() and ((len(word))==10):
        list2.append(word)
print(list2)

