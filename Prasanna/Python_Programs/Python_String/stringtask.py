str1 = "Virat is great Indian Player"
#0utput1 = "Player is great Indian Virat"
w1 = str1[-7:]
w2 = str1[5:-7]
w3 = str1[:5]
output1 = f"{w1} {w2} {w3}"
print( "_"*50)
print(output1)
"""output2 = "VVirat is great Indian Playerr" """
w4 = str1[:1]
w5 = str1[0:]
w6 = str1[27:]
output2 = f"{w4}{w5}{w6}"
print( "_"*50)
print(output2)
#output4 = "(Virat is great): reverse this part : Indian Player"
w7 = str1[-13:]
w8 = str1[0:14]
output4 = f"{w7} {w8}"
print( "_"*50)
print(output4)

