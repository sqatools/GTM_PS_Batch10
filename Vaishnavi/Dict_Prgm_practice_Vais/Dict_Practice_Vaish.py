#Q1 write a python program to get the square of even value and cube of odd values in dict
dict2 = {'p': 5, 'q': 8, 'r': 11, 's': 12, 't': 7}
#output = {'p': 125, 'q': 64, 'r': 1331, 's': 144, 't': 343}
output={}
for k,v in dict2.items():
    if v%2==0:
        output[k]=v**2
    else:
        output[k]=v**3
print(output)

# write a python to get count of each character in the given string without using count method.

str1 = "Python ProgrammingPPPPP"
#output = {'P': 2, 'y':1, 't':1, 'h':1, 'o': 2, 'n': 2, ' ': 1, 'r':2, 'g': 2, 'a': 1, 'm': 2, 'i':1}
output = {}
for val in str1:
    if val in output:
        output[val]+=1
    else:
        output[val]=1
print(output)

print("_"*50)
dict1 = {'name': 'Mehul', 'password': "$$#$#$$", 'email': 'test_email@gmail.com'}
dict2 = {'a': 123, 'b': 456}
dict2.update(dict1)
print(dict2)
print(dict1)

# write a program to move data from one dict to another.
dict4 = {'A': 567, 'B': 789, 'C': 456}
d5={}
temp=dict4.copy()
for key in temp:
    d5[key]=dict4.pop(key)
print(d5)

#fromkeys()
l1=['a','b','c']
var=dict.fromkeys(l1,"Apple")
print(var)

#setdefault:
dict11 = {'A': 567, 'B': 789, 'C': 456, 'E': 443}
var1=dict11.setdefault('H',200)
print(var1)
print(dict11)