
for i in range(1 , 10): #lenght
    for j in range(1, 9): #width
        if i in (1,2):
            if j in (1,2,3,4,5,6,7,8,9,10):
                print( "*",end=" ")

            else:
                print(" ",end= " ")
        elif i in(3,4,5,6,7,8,9):
            if j in (4,5):
              print("*",end=" ")
            else:
             print(" ",end= " ")
        else:
             print("*", end=" ")

    print()