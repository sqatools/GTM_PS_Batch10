"""Write a program to find the first repeated character in a string and its index.
Input = ‘sqatools’
Output = (s,0)"""

i1="sqatools"
set1=set(i1)
for i in set1:
    if i1.count(i)>=2:
      print(i, i1.index(i))

print("*"*100)

"""Write a program to print the index of each character in a string.
Input =  ‘sqatools’"""

inp1="sqatools"
for i in range (len(inp1)):
    print(inp1[i],i)