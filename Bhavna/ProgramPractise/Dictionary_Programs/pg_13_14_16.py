# Dictionary Practice Programs

# 13). Python Dictionary program to add a key in a dictionary.

Input = {1:'a', 2:'b'}

dict = {3:'c'}
Input.update(dict)
print(Input)

print('_'*70)

# 14). Python Dictionary program to concatenate two dictionaries.

D1 = {'name' : 'yash', 'city' : 'pune'}
D2 = {'course' : 'python', 'institute' : 'sqatools'}

D1.update(D2)
print("Output:",D1)

print('_'*70)

# 16). Python Dictionary program to get the sum of all the items in a dictionary.
Input = {'x' : 23, 'y' : 10 , 'z' : 7}
sum = 0
for i,j in Input.items():
    sum = sum+Input[i]

print("Sum of all items:",sum)

print('_'*70)
