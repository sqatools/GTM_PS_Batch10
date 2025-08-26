"""Check whether the given string is a palindrome (similar) or not.
Input= sqatoolssqatools
Output= Given string is not a palindrome"""

Input="sqatoolssqatools"
Reverse=Input[-1::-1]
if Input==Reverse:
    print(Reverse,"Given string is not a palindrome")
else:
    print(Reverse,"Given string is a palindrome")