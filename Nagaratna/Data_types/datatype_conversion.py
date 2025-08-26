#Interger

n=10
m=20
print("value is:",type(n),type(m),n, m)
#######################################################################################
a=90.9876
u=70
print("values is", type(a),type(u))

n="hello"
print("values:",type(n))
m= "my name is"
o="nagaratna"
q=n+" "+m+" "+o
print(q)
####################################################################################################
y = [67,90,12,7,34,96]
i=34
if i in list(y):
    print(i,type(i))
else:
    print("i is not in list",i)
######list to string########################
print("**_-_"*10)
list = [8,90,65,12,56]
str1 = str(list)
print(str1,type(str1),str1[1],str1[3])
##########################list to tuple#######################
print("**_-_"*10)
list = [58,4,87,92,34]
tup = tuple(list)
print(tup,type(tup))

###############################
print("**_-_"*50)
lista = [9,67,23,54,0]
listb = [5,8,65,23,12]
output = dict(zip(lista,listb))
print(output,type(output))
# manu has scored[23,12,40] in english and [50,10,32]in maths what all the marks he scored in both exam and what is the sum of it

print("**_-_"*10)
eng =[23,12,40]
mat = [50,10,32]
total =dict(zip(eng,mat))
print("all the marks he scored is:",total,type(total))
score = eng[0]+eng[1]+eng[2]+mat[0]+mat[1]+mat[2]
print("total score he scored is",score )
av = score/2
print("avg of score is :",av)
####################################### list to set#####################
print("**_-_"*10)
lis = [34,90,12]
set1 = set(lis)
print(set1,type(set1))

###################################tuple----->string##################################
print("**_-_"*10)
tup=(56,90,12)
str1 = str(tup)
print("value",str1,type(str1))
######################################tuple----->list#####################
