l1=['a','b','c']
l2=[2,3]
output=[]

for i in l1:
    for j in l2:
        result=(i,j)
        output.append(result)
print(output)

result3=[(p,q)for p in l1 for q in l2]
print(result3, "Comphrehension method")