#get comman values tup1=(4,7,9,23,5,6,12)
#tup2=(12,4,7,9,34,6,45)

tup1=(4,7,9,23,5,6,12)
tup2=(12,4,7,9,34,6,45)
output=[]

for val in tup1:
    for val1 in tup2:
        if val==val1:
            output.append(val)
        else:
            continue
print(tuple(output))
            