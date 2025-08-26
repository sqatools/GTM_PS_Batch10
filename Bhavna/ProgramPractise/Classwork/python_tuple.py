# 13/06/2025 Session continue

# tuple has all the properties as like list, but once we define the data in the tuple.
# then we can not change it.

tup = (9, 2.2, 'q', (5,2,3), 99, 17)
print(tup,type(tup))
# (9, 2.2, 'q', (5, 2, 3), 99, 17) <class 'tuple'>

##### Apply loop on the tuple ######
# Loop without indexing

for i in tup:
    print(i, end=" ")
# 9 2.2 q (5, 2, 3) 99 17

print()

print('_'*70)

# Loop with indexing
for j in range(len(tup)):
    print(j,tup[j])
'''
0 9
1 2.2
2 q
3 (5, 2, 3)
4 99
5 17
'''
print('_'*70)

########################## Slicing in the tuple #################

tup1 = (9,8,7,4,(99,88),[8,5,2],'Hi')
print(tup1[3:5]) #(4, (99, 88))
print(tup1[-2][::-1]) #[2, 5, 8]
print(tup1[-1::-2]) #('Hi', (99, 88), 7, 9)
print(tup1[::-2])   #('Hi', (99, 88), 7, 9)
print(tup1[-1][-1]) #i
print(tup1[::-1])   #('Hi', [8, 5, 2], (99, 88), 4, 7, 8, 9)

print('_'*70)

########################## Methods in tuple #################

tup2 = (8,95,6,32,41,2,8,66,12,8)
print(dir(tup2))

print('_'*70)

print("Count of 8:",tup2.count(8))  #Count of 8: 3

print("Index of 2:", tup2.index(2)) # Index of 2: 5

print('_'*70)
############### Tuple variable ##########################

result = tup2*2
print(result)
# (8, 95, 6, 32, 41, 2, 8, 66, 12, 8, 8, 95, 6, 32, 41, 2, 8, 66, 12, 8)

print('_'*70)

################################################
# 16/06/2025 Session

################### Get Max, Min, and sum of all value in  given tuple ###################

tup3 = (7,4,5,23,69,55,1)
print("Max value:",max(tup3))
print("Min value:",min(tup3))
print("Sum of values:",sum(tup3))

print('_'*70)

##############################################
# Q1 write a tuple program to get factorial of numbers.

tup4 = (5,2,9,4)
output = []

# Loop to get each value of tuple
for val in tup4:
    print(val)
    fact = 1
    for i in range(val,0,-1):
        fact = fact*i
    output.append(fact)

print(tuple(output))   #(120, 2, 362880, 24)

print('_'*70)
##############################################
# p2 :  write a python program to get all email from given tuple value
tup5 = ('id1@gmial.com',9898989898,'id2@gmial.com',7878787878,
        'id3@gmial.com')

output_list = []

for i in tup5:
    if isinstance(i,str) and "@" in i:
        print(i)
        output_list.append(i)
    else:
        continue

print("email:", output_list)
# email: ['id1@gmial.com', 'id2@gmial.com', 'id3@gmial.com']

print('_'*70)

# get common values from both tuples
tup6 = (4, 7, 9, 23, 5, 6, 12)
tup7 = (12, 4, 7, 9, 34, 6, 45)

output = []
for i in tup6:
    if i in tup7:
        output.append(i)

print(tuple(output))
