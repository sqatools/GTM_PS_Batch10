# 1. Write a program to print T pattern
# * * * * * *
# * * * * * *
#     * *
#     * *
#     * *
#     * *

for i in range(1, 7):
    for j in range(1, 7):
        if i in [1, 2]:
            print("*", end=" ")
        elif i in [3, 4, 5, 6]:
            if j in [3, 4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()


"""
# write a program to print swastik pattern

* *   * * * * *
* *   * * * * *
* *   * *
* * * * * * * *
* * * * * * * *
      * *   * *
* * * * *   * *
* * * * *   * *

"""
print("-" * 50)
for i in range(1, 9):
    for j in range(1, 9):
        if i in [1, 2]:
            if j in [1, 2, 4, 5, 6, 7, 8]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [3]:
            if j in [1, 2, 4, 5]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [4, 5]:
            print("*", end=" ")
        elif i in [6]:
            if j in [4, 5, 7, 8]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [7, 8]:
            if j in [1, 2, 3, 4, 5, 7, 8]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

