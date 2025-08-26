#Get values from any person house
l2={'Python','Programming','Language'}
#output= {'py','Pr','La','on','ng','ng','age'}
list1=list(l2)
output =[]

for word in list1:
    if word=='Python':
       output.append('py')
       output.append('on')
    elif word=='Programming':
        output.append('Pr')
        output.append('ng')
    else:
        output.append('La')
        output.append('age')
print(set(output))

l3 = {'Python', 'Programming', 'Language'}
# output2 = {'Python', 'Progmin',  'Langue'}
output1=[]
list2=list(l3)

for words in list2:
    if words=='Python':
        str1=str(words)
        output1.append(str1[0:6])
    elif words=='Programming':
        str1 = str(words)
        output1.append(str1[0:6])
    else:
        str1 = str(words)
        output1.append(str1[0:6])
print(set(output1))

