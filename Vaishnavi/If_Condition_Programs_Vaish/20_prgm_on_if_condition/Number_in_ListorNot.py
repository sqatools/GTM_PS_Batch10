#Python program to determine whether a given number is available in the list of numbers or not.

List1 = [1,2,34,35,45,6,7,8,9,46,78,98]
Val = int(input("Enter the value"))

if Val in List1:
    print("Values is present in list")
else:
    print("Values is not present in list")