"""Write a python to repeat vowels 3 times and consonants 2 times.
Input = “Sqa Tools Learning”
Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”"""
input1 = "Sqa Tools Learning"
vowel="aeiou"
output=''
for i in input1:
    if i in vowel:
        output=output+i*3
    else:
        output=output+i*2
print(output)