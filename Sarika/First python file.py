print("Hello world")
print("_"*40)
a = 10
#a= variable
#10 = value
# : = assignment operator

print(a)
print(id(a))
# id = 140704426894536 (place where it variable is stored)

b = 10
c = 10
print("address of a:",id(a))
print("address of b:",id(b))
print("address of c:",id(c))

p, q, r = 40, 50, 60
print("value of p:" , p)
print("value of q:" , q)
print("value of r:" , r)

###Assign same values to different variables

x = y = z = 100
print("value of x:", x )
print("value of y:", y )
print("value of z:", z )
# or
print("value of x, y, z:", x, y, z )

print("_"*50)

# Rules to define the varaibale name
#1. cannot contain space in variable name
#eg var1 = 123
#var 23 = 456 incorrect

#2. Variable should not start with number
#var567 = 12436
#56var = 789456 incorrect

#3. There is no limit for variable name
we_are_learning_python_programming = "Paython Programming" correct
# m = 200 correct
