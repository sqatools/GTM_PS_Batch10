"""
str1 = " Hello My name is nithish and living in city bangalore and my age is 26"
name =input("Enter your name")
city = input("Enter your city name")
age = int(input("Enter your age"))

value = " Hello My name is {} and living in city {} and my age is {}".format(name,city,age)
print(value)

value2=f" Hello My name is {name} and living in {city}  and my age is {age}"
print(value2)

# str1 = "Virat is great Indian Player"
output1 = "Player is great Indian Virat"
output2 = "VVirat is great Indian Playerr"
output3 = "VViratt iiss ggreatt IIndiann PPlayerr"
output4 = "(Virat is great): reverse this part : Indian Player"
"""
str1 = "Virat is great Indian Player"
"""
m1 = "Virat"
m2 =" player"
output5 = f"{m2} is great Indian {m1}"
print(output5) # player is great Indian Virat
output6= str1[0]+"Virat is great Indian Player"+str1[-1]
print(output6)
"""
str1 = "Virat is great Indian Player"
for char in str1:
    if char=="Virat":
        o1= char[0]
        o2=char[-1]

    elif char=="is":
        o3= char[0]
        o4=char[-1]
    elif char == "great":
        o5 = char[0]
        o6=char[-1]
    elif char == "Indian":
        o7 = char[0]
        o8 =char[-1]
    elif char == "player":
        o9 = char[0]
        o10=char[-1]
output8 =f"{o1}Virat{o2} {o3}is{o4} {o5}great{o6} {o7}Indian{o8} {o9}Player{o10}"
print(output8)

