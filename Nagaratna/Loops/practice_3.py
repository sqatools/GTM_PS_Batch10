# *******
# *******
#   ***
#   ***
#   ***

for i in range(1,7):
    for j in range(1,7):
        if i in(1,2):
            if j in[1,2,3,4,5,6]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i in[3,4,5]:
            if j in [3,4]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print( )


print("__--__"*10)
#######
# ********
# **
# ********
# **
# ********

for m in range(1,7):
    for n in range(1,6):
        if m in [1,3,5]:
            if n in [1,2,3,4,5,6,7,8]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif m in [2,4]:
            if n in [1,2]:
                print("*",end=" ")
            else:
                print(" ",end=" ")

    print()

# *********
# *********
#    ***
#    ***
#    ***
# *********
# *********

for p in range (1,8):
    for q in range(1,10):
        if p in [1,2,6,7]:
            if q in[1,2,3,4,5,6,7,8,9]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif p in [3,4,5]:
            if q in[4,5,6]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
print ("::::::"*20)

#   ***
#  **   **

for i in range ( 1,7):
    for j in range(1,7):
        if i in [1,6]:
            if j in [1,2,5,6]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i in [2,3,4,5]:
            if j in [3,4]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

print("*_-*"*10)
#  *       *
 #   *   *
 #     *
 #   *   *
#  *        *

for c in range(1,6):
    for d in range(1,6):
        if c in [1,5]:
            if d in[1,5]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif c in [2,4]:
            if d in [2,4]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif c ==3:
            if d==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")

    print()

print()
print("&-_&"*20)
print()

#    **    **
#    **    **
#    ********
#    ********
#    **    **
#    **    **
for v in range(1,7):
    for w in range(1,9):
        if v in [1,2,5,6]:
            if w in [1,2,7,8]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif v in [3,4]:
            if w in [1,2,3,4,5,6,7,8]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()