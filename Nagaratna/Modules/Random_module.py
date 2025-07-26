import random

print("random value:",random.randint(1,20))

list = [3,98,56,23,26,12]
print("random values in list=",random.choice(list))

list1 =[ 4,20,12,89,99]
random.shuffle(list1)
print("random values is",list1)
result2= random.randrange(1,7,2)
print("random choice is ",result2)