# Home Work
"""
# str1 = "Virat is great Indian Player"
output1 = "Player is greate Indian Virat"
output2 = "VVirat is greate Indian Playerr"
output3 = "VViratt iiss ggreatee Indiann PPlayerr"
output4 = "(Virat is greate): reverse this part : Indian Player"
"""
str1 = "Virat is greate Indian Player"
words = sentence.split()
rearranged = f"{words[4]} {words[1]} {words[2]} {words[3]} {words[0]}"
print(rearranged)