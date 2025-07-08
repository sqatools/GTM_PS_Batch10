import random

print("random value :", random.randint(1, 10))
# random value : 10

list1 = [5, 7, 3, 6, 10]
print("random number from list of values :", random.choice(list1))
# random number from list of values : 7

# get list of values in suffled order
random.shuffle(list1)
print("shuffle result :", list1) # [6, 10, 7, 3, 5]


# get random range value
result2 = random.randrange(1, 20, 3)
print("result2 :", result2)
# result2 : 13


