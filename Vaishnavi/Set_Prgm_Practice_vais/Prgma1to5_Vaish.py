#1. Write a program to create a set and print its elements.
set1={'hello',12,23.23,(2,3,4)}
print(set1,type(set1))

#2. Write a program to add a single element to a set using add() method.
set1.add(100)
print("added set:",set1)

print("_"*50)
# 3. Write a program to add multiple elements to a set using update() method.
set2={2,3,4}
set1.update(set2)
print("Set1:",set1)
print("Set2:",set2)

print("_"*50)
# 4. Write a program to remove a specific element from a set using remove() method.
set2.remove(3)
set1.remove(12)
print("Set1:",set1)
print("Set2:",set2)

print("_"*50)
# 5. Write a program to discard an element from a set using discard() method (no error if not found).
set3={'hello',12,23.23,(2,3,4)}
set3.discard(21)
print("Set3:",set3)

