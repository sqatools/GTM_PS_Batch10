for i in range(1 , 12): #lenght
    for j in range(1, 10): #width
        if i in (1,2,10,11):
            if j in (1,2,3,4,5,6,7,8,9,10,11,12):
                print( "*",end=" ")

            else:
                print(" ",end= " ")
        elif i in(3,4,5,6,7,8,9,10,11,12):
            if j in (4,5,8,9):
              print("*",end=" ")
            else:
             print(" ",end= " ")
        else:
             print("*", end=" ")

    print()
##

print("*"*50)

for i in range(1,12):
    for j in (1,10):
        if i in (1,2,12):
            if j in (1,2,3,4,5,6,7,8,9,10):
                print("*",end=" ")
            else:
                print(" ", end= " ")
        elif i in(3,4,5,6):

             if j in range(2,4,6):
                 print("%" , end= " ")
             else:
                 print(" ", end="")
    print()



