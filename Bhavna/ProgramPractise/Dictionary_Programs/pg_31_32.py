# Dictionary Practice Programs

# 31). Python Dictionary program to check whether a dictionary is empty or not.
Dict1 = {}

if len(Dict1)>0:
    print("Given Dictionary is not empty")
else:
    print("Given Dictionary is empty")

print('_'*70)

# 32). Python Dictionary program to add two dictionaries if the keys are the same then add their value.
Dict1 = { 'x':10, 'y':20, 'c':50, 'f':44 }
Dict2 = {'x':60,'c':25,'y':56}

for k1 in Dict1:
    for k2 in Dict2:
        if k1 == k2:
            out = Dict1[k1]+Dict2[k2]
            Dict2[k1]=out
        else:
            pass
print(Dict2)

