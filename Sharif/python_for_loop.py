
#1. Looping through a list

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
# Output
# apple
# banana
# mango

print ("_"*50)

colors = ["red", "green", "black"]
for color in colors:
    print(color)
# Output
# red
# green
# black

print ("_"*50)

#2. Using range

for i in range (5):
    print(i)
# Output
# 0
# 1
# 2
# 3
# 4


print ("_"*50)

#3. Looping through a string

for char in "England":
    print(char)
# output
# E
# n
# g
# l
# a
# n
# d

print ("_"*50)
# 4. Using break in a for loop
for num in range (10):
    if num ==5:
        break
    print(num)
#Output
#0
#1
#2
#3
#4

print ("_"*50)

# 5. Using continue
#### The continue statement is used inside
#loops to skip the rest of the code
#in the current iteration and jump to the next iteration of the loop ####

for num in range (5):
    if num ==3:
        continue
    print(num)
#Output
#0
#1
#2
#4

print ("_" *50)

## Example: Skipping numbers 4 and 7 ##
for i in range (1,10):
    if i == 4 or i == 7:
        continue
    print(i, end= "")
# Output: 1235689

print("_"*50)
#### The break statement is used to exit a loop prematurely.
# When a certain condition is met, it immediately stops the loop
# even if there are more iterations left to run ####

## Example: Stop the loop when number is 5 ##

for j in range (1, 10):
        if j == 5:
            break
        print(j, end= "")
#Output: 1234
