#Write a program to create a set and print its elements.
sets = {4,90,23,'a',1,90}
for eliments in sets:
    print(eliments)
"""
output:
1
4
23
90
a
"""
#Write a program to add a single element to a set using add() method.
set1 = {8,'w',61,91,5,12}
set1.add(999)
print(set1)
"""
Output:
{'w', 5, 999, 8, 91, 12, 61}
"""
#Write a program to add multiple elements to a set using update() method.
set3 = {1,9,45,94,'z','y'}
set3.update([111,2])
print(set3)
"""
Output:
{1, 'z', 2, 9, 'y', 45, 94, 111}
"""
# 4. Write a program to remove a specific element from a set using remove() method.
set5 = {'w',45,12,1,6,34}
set5.remove(12)
print(set5)
"""
output:
{1, 34, 'w', 6, 45}
"""
#5.Write a program to discard an element from a set using discard() method (no error if not found).
set5.discard(34)
print(set5)
set5.discard(100)
print(set5)
"""
Output:
{1, 6, 45, 'w'}
{1, 6, 45, 'w'}
"""
# Write a program to clear all elements from a set using clear() method

set6 ={11,66,88,99,44,34}
set6.clear()
print(set6)
"""
Output:
set()

"""
#10. Write a program to find the symmetric difference between two sets.
set_a= {7,56,43,9,23,12}
set_b= {9,56,8,43,23,12}
test = set_a.symmetric_difference(set_b)
print(test)
"""
output:
{7, 8}
"""

# 11.Write a program to check if a set is a subset of another.
set_c = {1, 2, 3}
set_d= {1, 2, 3, 4, 5}
if set_c.issubset(set_d):
    print("d is subset of c ")
else:
    print("d is not subset of c")
"""
output:
d is suvset of c 
"""

# 12. Write a program to check if a set is a superset of another.
set_t ={ 5,34,56,89,45,2,22}
set_r ={ 45,2,22 ,7}
if set_t.issuperset(set_r):
    print("its superset")
else:
    print("Its not supreset")
"""
output:
its superset
"""
set_t1 = {1,2,3,4,5,6,7}
set_r1 = {5,6,7}
x =set_t1.issuperset(set_r1)
z = set_r1.issuperset(set_t1)
print(x)
print(z)

"""
output:
True
False
"""