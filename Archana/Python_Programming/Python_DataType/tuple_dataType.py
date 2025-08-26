################################# Tuple ####################################

"""
Properties:
->  Tuple is immutable data type. we can not modify the tuple.
->  Tuple store values in comma separated format.
->  Tuple can contain all the type of data, e.g. int, float, complex, string, list
    tuple, dict, set, bool.
->  Tuple follows positive negative indexing as like string and list.
->  Tuple store data in round brackets.
->  Usage of the tuple data type, where the data is fixed.
    e.g store days in a months, days in week, months in year.
->  Tuple is faster than list in terms of performance.
"""

tup1 = (2, 5.6, 'Python', (4, 6, 7), [1, 3, 5], {'b': 456}, {6, 8, 9}, True, False)

print(tup1, type(tup1))
# (2, 5.6, 'Python', (4, 6, 7), [1, 3, 5], {'b': 456}, {8, 9, 6}, True, False) <class 'tuple'>


print(tup1[4])  # [1, 3, 5]
print(tup1[2][2])  # t
print(tup1[-6][-1])  # 7
print(tup1[3][-1])  # 7

tup2 = (3, 6, 7)
# we don't have any method to update the tuple values


print("_" * 50)