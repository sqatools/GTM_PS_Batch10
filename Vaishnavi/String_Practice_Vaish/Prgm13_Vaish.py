"""Write a python to count vowels from each word in the given string show as dictionary output."""
input1 = "We are Learning Python Codding"
word=input1.split()
vowel="aeiou"
dictionary=dict()
for i in word:
    count = 0
    for k in i:
        if k in vowel:
            count+=1
            dictionary[i]=count
        else:
            continue
print(dictionary)