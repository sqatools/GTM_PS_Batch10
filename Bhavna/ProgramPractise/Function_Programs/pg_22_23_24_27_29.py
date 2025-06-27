# Function Practice Programs

# 22). Python function program to get unique values from the given list.
# Input : [4, 6, 1, 7, 6, 1, 5]

def unique(*num):
    output = []
    for i in num:
        if i not in output:
            output.append(i)
    print(output)

unique(4,6,1,7,6,1,5)

print('_'*70)

# 23). Python function program to get the duplicate characters from the string.
# Input: Programming

def duplicate(*dup):
    output = []
    for char in dup:
        if char not in output:
            output.append(char)

    print(set(output))

duplicate("Abcbc")

print('_'*70)

# 24). Python function program to get the square of all values in the given dictionary.

def square(num):
    output = {}
    for k,v in num.items():
        output[k] = v**2

    print(output)

square({'a':4,'b':3,'c':12,'d':6})

print('_'*70)


# 27). Python function program to get a list of odd numbers from 1 to 100.

def odd():
    odd1 = []
    for i in range(1,101):
        if i%2!=0:
            odd1.append(i)

    print(odd1)

odd()

print('_'*70)

# 29). Python function program to get the addition with the return statement.

def add(a,b):
    return a+b

result = add(20,30)
print("Addition:",result)