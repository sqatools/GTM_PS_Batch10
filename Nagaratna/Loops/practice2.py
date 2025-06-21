

for a in range(1,7): # a= 1,2,3,4,5
   for b in range (0,a) : #b= 0|0,1|0,1,2|0,1,2,3|0,1,2,3,4|0,1,2,3,4,5|
       print("*",end= ' ')

   print()

print("+++"*30)
################
for h in range(1,7):
    for k in range(1,7-h):
        print("#",end=" ")
    print()

#########################################
#  *******
#    ***
#    ***
#  *******
for x in range(1,6):
    for y in range(1,5):
        if x in [1,5]:
            if y in[1,2,3,4,5]:
                print("*",end=" ")
            else:
                print("@",end=" ")
        elif x in [2,3]:
            if  y in [2,3,4]:
                print("*" ,end=" ")
            else:
               print("$",end=" ")
    else:
       print()

#   #
#
#

for i in range (1,5):
    print("address",i)
    for j in range(1,4):
        print("item",j)
    print("*_*"*20)

######
for m in range( 1,6):
    print("second class",m)
    for k in range(2,6):
        print("first class",k)


list1 = [5,9,2,6,7,1,4,3,11]
for val in list1:
    if val%2 ==0:
        print("square of the number is :-",val**2,type(val))
    else:
        print("cube of the number is :-", val **3, type(val))

