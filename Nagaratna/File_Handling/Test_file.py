"""
def readfile(filepath):
    with open(filepath,"r") as file:
        data1= file.read()
        print(data1)
readfile("file1.py")

def readfile2(filepath):
    with open(filepath,"r") as file2:
        data2= file2.read()
        print(data2)
readfile2("C:\\Users\\nagar\\Documents\\upload dummy docs\\Dummy_documents.txt")

def writefile(filepath,content):
    with open(filepath,"w") as file3:
        data3 = file3.write(content)
        print(data3)
writefile("Write_new file","Hello Nagaratna how your python learning going on")

def appendfile(filepath,content):
    with open(filepath,"a")as file4:
        data4 = file4.write(content)
        print(content)
appendfile("C:\\Users\\nagar\\Documents\\upload dummy docs\\My_Filename.txt","Hello python")

#4). Python function program to find the maximum of three numbers.

def findfun():
    test2=[3,89,76]
    result= max(test2)
    print(result)
findfun()

#Python function program to find the sum of all the numbers in a list.
def addnum():
   input =[6,9,4,5,3]
   result = sum(input)
   print(result)
addnum()
"""
# Python function program to multiply all the numbers in a list.
def mulnum():
    count =1
    input1=[-8, 6, 1, 9, 2]
    for i in input1:
        count=i*count
    print("Final multiplication result:", count)
mulnum()
#Python function program to reverse a string.
def reversest():
    input11 ="Python1234"
    for j in input11:
        result=input11[::-1]
    print(result)
reversest()
#Python function program to check whether a number is in a given range.
"""def numrange():
    i =int(input("Enter your number"))
    if i in range(1,21):
            print("Value is in range",i)
    else:
            print("value not in range",i)
numrange()"""

#Python function program that takes a list and returns a new list with unique elements of the first list.

def unique():
    tinput= [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
    element =set(tinput)
    print(element)
unique()

#Python function program that take a number as a parameter and checks whether the number is prime or not
"""def prime():
    m = (int(input("Enter the number")))
    if m % 2==1 :
        print("Its prime number",m)
    else:
        print("Its not a prime number",m)
prime()"""

def prime2(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    if count == 0 and num > 1:
        print("It's a prime number")
    else:
        print("It's not a prime number")

num = int(input("Enter number to check prime: "))
prime2(num)

