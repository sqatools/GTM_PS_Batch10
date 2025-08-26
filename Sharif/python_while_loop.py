
#While loop

# While loop code executes until certain condition is matching

n = 1

while n <= 7: # The loop runs while count <= 7 is true.
    print (n) # When count becomes 8, the condition is false, and the loop stops.
    n +=1
#Output:#1
#2
#3
#4
#5
#6
#7

print ("*"*50)

count = 1

while count <=5: #  The loop runs while count <= 5 is true.
    print(count) #  When count becomes 6, the condition is false, and the loop stops.
    count +=1
# Output
# 1
# 2
# 3
# 4
# 5

print("*"*50)
##### infinite loop #####
# infinite loop is a loop that never ends because its condition always remains True

#Example 1
#while True: means the loop will run forever unless interrupted.
#Each time, it prints the current value of n.
#Then it increments n by 1.
#When n reaches 50, the if condition is true and break stops the loop.

n = 1
while True: # This loop will run indefinitely until we break out of it
    print(n)
    n +=1
# Need to stop
    if n == 50: # When n becomes 50, stop the loop
        break

print("*" * 50)




