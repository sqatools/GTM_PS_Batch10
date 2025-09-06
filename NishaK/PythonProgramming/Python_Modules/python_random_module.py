import random


print("Random Value :", random.randint(1, 10))
# Random Value : 7

list1 = [5, 7, 3, 6, 10]
print("Random value from list :", random.choice(list1))
# Random value from list : 5


# get list of values in suffled order
random.shuffle(list1)
print("shuffle result :", list1)
# shuffle result : [10, 6, 5, 3, 7]

# get random range value
Result2 = random.randrange(1, 20, 5)
print("Result :", Result2)
# Result : 11
