dict1={'A':267,'B':"Hello",'C':786}
dict2={}
dict2['x']=dict1.pop('A')
dict2['y']=dict1.pop('B')
dict2['z']=dict1.pop('C')
print(dict2)