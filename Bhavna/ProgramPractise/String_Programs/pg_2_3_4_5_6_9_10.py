# 2). Python string program that takes a list of strings and returns the length of the longest string.


str = "friends are the family we choose."
a = str.split(" ")
print(a)
dm = 0
for k in a:
    c = len(k)
    if c > dm:
        dm = c
print(dm)
print('_'*70)

# 3. Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).

str1 = "Python"
output = str1[-2::1]*4
print(output)

print('_'*70)

# 4. Python string program to reverse a string if it’s length is a multiple of 4.
str2 = "staypositive"
len = len(str2)
if len%4==0:
    print(str2[-1::-1])


# 5. Python string program to count occurrences of a substring in a string.

str3 = "You will never regret being kind"
print(str3.count("re"))

print('_'*70)

# 6. Python string program to test whether a passed letter is a vowel or consonant.
str4 = "calmnsuperpower"
vowel = ('a','e','i','o','u','s')
for char in str4:
    if char in vowel:
        print("The letter is vowel:",char)
    else:
        print("The letter is consonant:",char)

print('_'*70)

# 9. Write a Python program to calculate the length of a string with loop logic.

str5 = "thequeen"
length = 0

for i in str5:
    length+=1

print(length)

print('_'*70)

# 10. Write a Python program to replace the second occurrence of any char with the special character $.
str6 = "Programming"
# for i in str6:
a = str6.replace("r","$",1).replace("m","$",1)
print(a)

print('_'*70)
