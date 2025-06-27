# 23/06/2025
#Q1 list1 = [4, 6, 8, 12, 67, 34, 50 , 60, 70]
# get the value between 10 to 50
# output1 = [12, 34, 50]

list1 = [4,6,8,12,67,34,50,70]
output = []
for i in list1:
    if i>10 and i <= 50:
        output.append(i)

print("output1:",output)
# output1: [12, 34, 50]
print('_'*70)

str1 = "We are Learning Python Programming"
#output = 'gnimmargorp'

str = str1.split()
max = " "
sec_word = " "

for val in str:
   if len(val)>len(max):
       max=val
   elif len(val)> len(sec_word) and val!= max:
       sec_word=val
print("Longest word:",max)
print("Second largest word:",sec_word)
# print("Output2:",max[::-1])


print('_'*70)

