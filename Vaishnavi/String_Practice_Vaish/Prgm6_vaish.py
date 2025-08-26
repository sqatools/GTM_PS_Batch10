"""Python string program to test whether a passed letter is a vowel or consonant."""

str2="hello"
Vowel="aeiou"

for i in str2:
    if i in Vowel:
        print("Vowel :" , i)
    else:
        print("Non vowel :", i)