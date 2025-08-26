# LIST PRACTICE PROGRAMS

# 31). Python program to merge all elements of the list in a single entity using a special character.
list = ['Hi','how','are','you','all']

result = "@".join(list)
print(result)

print('_'*70)

# 32). Python program to get the difference between two lists.

l1 = [11,22,33,44,55,66]
l2 = [66,55,44,33]

Output = []

for i in l1:
    if i not in l2:
        Output.append(i)

print("Difference between both list:", Output)

print('_'*70)

# 33). Python program to reverse each element of the list.
# Input = [‘Sqa’, ‘Tools’, ‘Online’, ‘Learning’, ‘Platform’]
# output = [‘aqS’, ‘slooT’, ‘enilno’, ‘gninraeL’, ‘mroftalP’]

Input = ['Sqa', 'Tools', 'Online', 'Learning', 'Platform']
Output = []

for val in Input:
    Output.append(val[::-1])

print("Output:",Output)

print('_'*70)

# 36). Python program to get all the unique numbers in the list.

list = [2,11,58,74,2,6,9,11]
output = []

for i in list:
    if i not in output:
        output.append(i)

print("Unique Numbers:",output)

print('_'*70)

# 37). Python program to convert a string into a list.

string = "Hey Good Morning"
result = string.split(" ")

print(result)

print('_'*70)

# 38). Python program to replace the last and the first number of the list with the word.

Input = [12, 32, 33, 5, 4, 7]

Input[0] = 'SQA'
Input[-1] = 'Tools'
print("Result:",Input)

print('_'*70)
