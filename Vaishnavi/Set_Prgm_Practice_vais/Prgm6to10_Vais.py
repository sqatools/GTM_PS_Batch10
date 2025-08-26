# 6. Write a program to clear all elements from a set using clear() method.
set1={2,3,4,5,6,7}
set1.clear()
print(set1)

#7. Write a program to create two sets and find their union.
set2={2,3,4,5,6,7}
set3={'p','q',2,4,6}
result=set2.union(set3)
print(result,":Result")
print(set2,": set2")
print(set3,"set3")

print("_"*50)

# 8. Write a program to find the intersection of two sets.
set4={2,3,4,5,6,7}
set5={'p','q',2,4,6}
result1=set4.intersection(set5)
print(result1)

print("_"*50)

#9. Write a program to find the difference between two sets (A - B).
set6={2,3,4,5,6,7}
set7={'p','q',2,4,6}
r1=set7.difference(set6)
print(r1)

print("_"*50)
# 10. Write a program to find the symmetric difference between two sets.
set8={2,3,4,5,6,7}
set9={'p','q',2,4,6}
r2=set8.symmetric_difference(set9)
print(r2)