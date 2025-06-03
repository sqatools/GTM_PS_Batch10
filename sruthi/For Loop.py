print("_"*50)
########Nested Loop#######

#Outerloop
for i in range(1,6): # i=1,2,3
   print("Address :", i)
#Innerloop
   for j in range(1,4): # j=1,2,3
    print("Item :", j)


print("_"*50)
#write a triangular pattern
"""
*
* *
* * *
* * * *
* * * * *
"""
for i in range(1,6):
    for j in range(0,i):
        print("*", end='')

    print()
print("_"*50)

#Reverse triangular pattern
""" 
* * * * *
* * * *
* * *
* *
*
"""
for i in range(1,6):
    for j in range(0,7-i):
        print("*", end='')
    print()

#0 pattern
"""
  * * *   #i=1
*       * #i=2
*       * #i=3
*       * #i=4
*       * #i=5
  * * *   #i=6
"""
for i in range(1,7):
  for j in range(1,6):
     if i in [1,6]:
         if j in [2,3,4]:
            print("*", end='')
        else:
            print(" ", end='')
     elif i in [2,3,4,5]:
     if j in [2,3,4]:







