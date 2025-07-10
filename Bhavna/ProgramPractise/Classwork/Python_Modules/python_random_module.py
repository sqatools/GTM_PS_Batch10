#04/07/2025 Session continue
import random

print("random value:",random.randint(1,20))
# random value: 11

list = [1,9,6,3,7,2]
print("Random number from the list:",random.choice(list))
# Random number from the list: 9

# Get list of values in suffled order
random.shuffle(list)
print("shuffle result:", list)
# shuffle result: [6, 3, 2, 1, 9, 7]

# Get Random range value
result = random.randrange(1,30,5)
print("Result:",result)
# Result: 16