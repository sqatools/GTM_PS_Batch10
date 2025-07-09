# pass by values

def rank1(test):
    print(test)
rank1("Hello Python")

def date1(date1):
    print(date1) #Hello Python
date1("11/06/1997") # 11/06/1997

#Pass by reference:

x="Hello Good morning"
rank1(x)

def my_message(msg):
    print(msg)
my_message("Selenuim is very easy to learn") #Selenuim is very easy to learn

y="I want to learn python quickly"
my_message(y)  #I want to learn python quickly


def name ( test):
    print()

# 1). Python function program to add two numbers.
def adding(x,y):
 value=x+y
 print(value)
adding(10,20)
#####
def mult(a,b):
    mult=int(a*b)
    print(mult)
num1= int(input("Enter your number1"))
num2= int(input("Enter your number2"))
mult(num1,num2)
"""
output:
Enter your number1 5
Enter your number2 10
50
"""



    


