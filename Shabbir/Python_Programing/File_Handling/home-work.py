with open("data.txt",'r') as file:
    S = file.read()
M = S.swapcase()
with open("data.txt",'w') as file:
    file.write(M)

with open("data.txt",'r') as file:
    S = file.read()
word = S.split()

for M in word:
    if "@" in M and "." in M:
        print(M)