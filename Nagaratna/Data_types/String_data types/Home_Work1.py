str1 = "Virat is great Indian Player"
# question "Player is great Indian Virat"
w1 = str1[0:5]
w3 = str1[-7:]
w2 = str1[5:-7]
output = f"{w3} {w2} {w1}"
print(output) #Ans: Player  is great Indian Virat

print("*-_-"*30)
output2= f"V{w1} {w2} {w3}r"
print(output2) #Ans:VVirat  is great Indian  Playerr
print("*-_-"*30)
#Vviratt iiss ggreatee IIndiann PPlayerr

##
str3 = "Virat is great Indian Player"
m1 ="Virat"
m2 ="is"
m3 ="Great"
m4 = "Indian"
m5 = "Player"
w4 = str3[0]
w5 = str3[4]
w6 = str3[6]
w7 = str3[7]
w8 = str3[9]
w9 = str3[13]
w10 = str3[15]
w11 = str3[20]
w12= str3[22]
w13 = str3[27]
output3 = f"{w4} {m1} {w5} {w6} {m2} {w7} {w8} {m3} {w9} {w10} {m4} {w11} {w12} {m5} {w13}"
print(output3) #V Virat t i is s g Great t I Indian n P Player r

tr= "hello good morning"
print("Upper cases is:",str.upper(tr)) # Upper cases is: HELLO GOOD MORNING
str10 = "HELOO HW ARE YOU"
print("lower letter is : ",str.lower(str10)) # lower letter is :  heloo hw are you

sen = "Hello good morning"
print("is upper cases is : ", str.isupper(sen)) #is upper cases is :  False


