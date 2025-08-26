######## list #########
"""
Properties:
->  List is mutable data type. we can modify the list at any point of time.
->  List store values in comma separated format
->  List can contain all the type of data, e.g. int, float, complex, string, list
    tuple, dict, set, bool.
->  List follows positive negative indexing as like string.
->  list store data in square brackets.
->  Usage of the list data type, where we update data regularly
    e.g employee management, there we can add, delete, and update employee info.
"""

list1 = [4, 5.6, 'Hello', 5 + 8j, [3, 5, 6], (1, 2, 3), {'a': 123}, {4, 7, 8, 4}, True]

print(list1, type(list1))
# [4, 5.6, 'Hello', (5+8j), [3, 5, 6], (1, 2, 3), {'a': 123}, {8, 4, 7}, True] <class 'list'>

# list follows positive and negative indexing

print(list1[4])  # [3, 5, 6]
print(list1[-2])  # {8, 4, 7}
print(list1[-6])  # (5+8j)
print(list1[6])  # {'a': 123}
print(list1[4][1])  # 5

list2 = [4, 6, 8]
list2.append(10)
print("list2 :", list2)  # list2 : [4, 6, 8, 10]

print("_" * 50)