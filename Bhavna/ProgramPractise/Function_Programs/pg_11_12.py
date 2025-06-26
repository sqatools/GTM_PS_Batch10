# Function Practice Programs

# 11). Python function program to find the even numbers from a given list.

def even(list):
    even1=[]
    for i in list:
        if i%2 == 0:
            even1.append(i)

    print(even1)

Input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even(Input)

print('_'*70)

# 12). Python function program to create and print a list where the values are squares of numbers between 1 to 10.

def square():
    for i in range(1,10):
        print(i**2,end=" ")

square()
print()
print('_'*70)
