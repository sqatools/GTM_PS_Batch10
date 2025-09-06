import random

rst=random.randint(1,10)
print(rst)
rst1=random.randrange(100,500)
print(rst1)
rst2=random.choice([1,4,7,8])
print(rst2)
list1=[12,34,78,56,36,1,9]
random.shuffle(list1)
print(list1)