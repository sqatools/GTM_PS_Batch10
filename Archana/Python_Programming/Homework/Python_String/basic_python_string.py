"""
# Home Work
# str1 = "Virat is greate Indian Player"
output1 = "Player is greate Indian Virat"
output2 = "VVirat is greate Indian Playerr"
output3 = "VViratt iiss ggreatee IIndiann PPlayerr"
output4 = "(Virat is greate): reverse this part : Indian Player"
"""
print("#Output 1")
print("*" * 10)
str1 = "Virat is great Indian Player"
#output1 = "Player is great Indian Virat"words
words = str1.split() #['Virat', 'is', 'great', 'Indian', 'Player']
words[0], words[-1] = words[-1], words[0]
output1 = ' '.join(words)
print(output1)

print("-" * 50)
print("#Output 2")
print("*" * 10)
words = str1.split() #['Virat', 'is', 'great', 'Indian', 'Player']
words[0] = 'V'+ words[0]
words[4] = words[4] + 'r'
output2 = ' '.join(words)
print(output2)

print("-" * 50)
print("#Output 3")
print("*" * 10)
#output3 = "VViratt iiss ggreat IIndiann PPlayerr"
str1 = "Virat is great Indian Player"
# rule: add first letter + word + last letter
words = str1.split()
modified_words = []
for char in words:
    modified_word = char[0].upper() + char + char[-1].lower()
    modified_words.append(modified_word)

output3 = ' '.join(modified_words)
print(output3)
