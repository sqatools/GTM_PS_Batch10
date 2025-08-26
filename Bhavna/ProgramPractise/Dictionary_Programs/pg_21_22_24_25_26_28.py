# Dictionary Practice Programs

# 21). Python Dictionary program to insert a key at the beginning of the dictionary.
Input = { 'course' : 'python',  'institute' : 'sqatools' }
Insert = {'name' : 'omkar'}

Insert.update(Input)
print(Insert)

print('_'*70)

# 22). Python Dictionary  program to create a dictionary where keys are between 1 to 5 and values are squares of the keys.

output={}
for i in range(1,6):
    output[i]=i**2

print(output)
print('_'*70)

# 24). Python Dictionary program to remove a key from the dictionary.
Input = {'a':2,'b':4,'c':5}

result = Input.pop('c')
print(Input)

print('_'*70)

# 25). Python Dictionary program to map two lists into a dictionary.

a = [ 'name', 'sport', 'rank', 'age']
b = ['Virat', 'cricket', 1,  32]

d = zip(a,b)
print(dict(d))

# 26). Python Dictionary program to find maximum and minimum values in a dictionary.

Dict = { 'a' : 10, 'b' : 44 , 'c' : 60, 'd' : 25}
list = []
for i in Dict.values():
    list.append(i)

print("Maximum value:",max(list))
print("Minimum Value:",min(list))

print('_'*70)

# 28). Python Dictionary program to replace words in a string using a dictionary.
String = 'learning python at sqa-tools'
Dict = { 'at' : 'is', 'sqa-tools' : 'fun'}
# Output = ‘learning python is fun’


for k, v in Dict.items():
    String = String.replace(k,v)

print(String)

print('_'*70)

