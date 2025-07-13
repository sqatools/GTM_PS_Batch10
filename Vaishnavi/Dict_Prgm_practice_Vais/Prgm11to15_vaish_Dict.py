"""11). Python Dictionary program to sort a dictionary using keys.
Input = {‘d’ : 21, ‘b’ : 53,  ‘a’: 13, ‘c’: 41}
Output =
(‘a’, 13)
(‘b’, 53)
(‘c’, 41)
(‘d’, 21)"""
inp1={'d':21,'b':53,'a':13,'c':41}
out1=[]

out1=inp1.values()
r1=sorted(out1)
print(r1)
out2=inp1.keys()
r2=sorted(out2)
print(r2)
o1={}
for i,j in zip(r2,r1):
    o1[i]=j
print(o1)

dict1 = {'d':21,'b':53,'a':13,'c':41}

for key in sorted(dict1):
    #print("%s: %s" % (key,dict1[key]))
    print("({} : {})".format(key,dict1[key]))


"""12). Python Dictionary program to sort a dictionary in python using values.
Input = {‘d’ : 14, ‘b’ : 52,  ‘a’: 13, ‘c’: 1 }
Output= (c, 1) (a,13) (d, 14) (b, 52)"""
inp2={'d':14,'b':52,'a':13,'c':1}
temp=sorted(inp2.items())
print(temp)

"""13). Python Dictionary program to add a key in a dictionary.
Input= {1:’a’, 2:’b’}
Output= (1:’a’, 2:’b’, 3:’c’}"""
Input= {1:'a', 2:'b'}
Input.setdefault(3,'c')
print(Input)
Input['D']=200
print(Input)

"""14). Python Dictionary program to concatenate two dictionaries.
Input:
D1 = {‘name’ : ’yash’, ‘city’ :  ‘pune’}
D1 = {‘course’ : ’python’, ‘institute’ : ’sqatools’}
Output :
{ ‘name’ : ’yash’, city: ‘pune’, ‘course’ : ’python’, ‘institute’ : ’sqatools’ }"""

D1={'name':'yash','city':'pune'}
D2={'course':'python','institute':'sqatools'}
D1.update(D2)
print(D1)

"""15). Python Dictionary program to swap the values of the keys in the dictionary.
Input = {name:’yash’, city: ‘pune’}
Output = {name:’pune’, city: ‘yash’}"""
inp3={'name':'yash','city':'pune'}
out1={'name':inp3.get('city'),'city':inp3.get('name')}
print(out1)



