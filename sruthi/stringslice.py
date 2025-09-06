 """
str1 = "Virat is greate Indian Player"
output1 = "Player is greate Indian Virat"
output2 = "VVirat is greate Indian Playerr"
output3 = "VViratt iiss ggreatee IIndiann PPlayerr"
output4 = "(Virat is greate): reverse this part : Indian Player"
"""
str1= "Virat is greate Indian Player"
print("_"*50)
W1 = str1[:5]
W3 = str1[-7:]
W2 = str1[5:-7]
output1= f"{W3} {W2} {W1}"
print(output1)

print("_"*50)
#O2 :
f_chr= str1[0]
l_chr = str1[-1]
output2= f"{f_chr}{str1}{l_chr} "
print(output2)

print("_"*50)
#str1="virat is great Indian Player"
#output3="VViratt iiss ggreatee IIndiann PPlayerr"
W1 = str1[0]+str1[:5]+str1[4]
W2 = str1[6]+str1[6:8]+str1[7]
W3 = str1[9]+str1[9:14]+str1[13]
W4 = str1[16]+str1[16:22]+str1[21]
W5 = str1[-6]+str1[-6:]+str1[-1]
output3= f"{W1} {W2} {W3} {W4} {W5}"
print(output3)

print("-"*50)
# str1 = "Virat is great Indian Player"
# output4 = "(Virat is great): reverse this part : Indian Player"
W1 = str1[-14::-1]
W2 = str1[-14:]
output5= f"{W1} {W2}"
print(output5)




