"""
list = [7,98,23,34,12,98]
# without indexing
for i in list:
    print(i)
# with index
for j in range(len(list)):
    print(j,list[j])
#
my_list = [10, 20, 30, 40, 50]
value = 30
#without index
if value in my_list:
    print("Value is available:",value)
else:
    print("value not available")
    #with index
for q in range(len(my_list)):
    if my_list[q] == 30:
        print("Its available:",my_list[q])
    else:
        print("its not available")
print("**__**__"*20)
list3= [3,67,21,'a',10,'z']
for m in range(len(list3)):
    print(m,list3[m])
print(list3[0:5])
"""
##
List1 = [2,56,89,23,'A','Z',55]
List1.append(200)
print(List1)
print("*_-_"*30)
List2= [34,7,54,'f','r',10,'y']
List2.insert(40,4)
print(List2)
print("*_-_"*40)
list_1 = [6,8,67,23,34]
list_2 = ['g','w','y']
results = list_2+list_1
result1 = list_1+list_2
print(result1)
print(results)