#11. Write a program to check if a set is a subset of another.
s8={2,3,4,5,6,7}
s9={'p','q',2,4,6}
s10={2,3,4,5,6,7}
r1=s8.issubset(s9)
r2=s8.issubset(s10)
print(r2)
print(r1)

# 12. Write a program to check if a set is a superset of another.
s1={2,3,4,5,6,7}
s2={2,3,4}
r3=s1.issuperset(s2)
print("superset",r3)

print("_"*50)
#13. Write a program to check if two sets are disjoint.
s1={2,3,4,5,6,7}
s2={'p','q'}
r4=s2.isdisjoint(s1)
print(r4)

print("_"*50)
#14. Write a program to remove an element from a set using pop() method.
s1={2,3,4,5,6,7,9}
p1=s1.pop()
print(p1)
p2=s1.pop()
print("2nd:",p2)
print(s1)

print("_"*50)
#15. Write a program to copy a set using copy() method.
s3={2,3,4,5,6,7,9}
s5={1,22,23}
s3=s5.copy()
print(s3)
print(s5)