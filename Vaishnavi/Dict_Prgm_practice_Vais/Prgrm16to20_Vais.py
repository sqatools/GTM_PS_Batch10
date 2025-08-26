"""16). Python Dictionary program to get the sum of all the items in a dictionary.
Input = {‘x’ : 23, ‘y’ : 10 , ‘z’ : 7}
Output = 40"""
import sys

inp3={'x':23,'y':10,'z':7}
output=sum(inp3.values())
print(output)

"""17). Python program to get the size of a dictionary in python.
Hint : use sys.getsizeof(var) method.
Input = {‘name’ : ’virat’, ‘sport’ : ’cricket’}
Output = 232bytes"""
inp4={'name':'virat','sport':'cricket'}
output1=str(sys.getsizeof(inp4))
print(output1)

"""18). Python Dictionary program to check whether a key exists in the dictionary or not.
Input:
Dict1 = {city:’pune’, state=’maharashtra’}
Dict1[country]
Output= ‘key does not exist in dictionary"""

d1={'city':'pune','state':'maharashtra'}
dict3=input("Eneter the  key")
for k in d1:
    if dict3!=k:
        print(k,"key does not exist in dictionary")
    else:
        print(k,"key exist in dictionary")


"""19). Python program to iterate over a dictionary.
Input :
Dict1 = {food:’burger’, type:’fast food’}
Output :
food : burger
type : fast food"""
inp5={'food':'burger','type':"fast food"}
for key,value in inp5.items():
    print(key," : ",value)


"""20). Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
Input: n=4
Output ={1 : 1, 2 : 8, 3 : 27, 4 : 64}"""
n=4
output={}
for i in range(n):
    output[i]=i**3
print(output)



