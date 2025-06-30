str = "Hello my name is Nagaratna and im learning python"
name = "Ganesh"
learn = "C++"
value = "Hello my name is"" "+name+" and im learning"" "+learn+""
print(value,type(value))
################### format methods######################
str1 = "My name is ananya and my score in maths is 93 it means its distinctions"
Name1 = "Mahima"
Sub = "Eng"
grade = "first class"
value_is = "My name is {} and my score in {} is 93 it means its {}".format(Name1,Sub,grade)
print(value_is, type(value_is))

############################# f string method #######################
str1 = "My name is ananya and my score in maths is 93 it means its distinctions"
name1 = "Fathima"
Sub = "Maths"
grade = "Second class"
values = f"My name is {name1} and my score in {Sub} is 93 it means its {grade}"
print (values)
print("&"*30)
######################################################################
sen = " I am working in Accenture as a QA and work base location is bangalore. "
Company = "TCS"
Location = "Chennai"
Role = "Developer"
Value1 = "I am working in "+Company+" as a "+Role+" and work base location is "+Location+""
print(Value1)
print("*"*100)
#################################Format methods######################
sen = " I am working in Accenture as a QA and work base location is bangalore. "
Company1 = "TECHM"
Location1 = "Hydrabad"
Role1 = "Analyst"
Value_2 = " I am working in {} as a {} and work base location is {}".format(Company1,Role1,Location1)
print(Value_2)

print("*"*100)
######################################## F string methods #################################
sen3 = " I am working in Accenture as a QA and work base location is bangalore. "
Comp = "LG"
Loc = " Gurugraw"
Rol= "HR"
Value3 = f" I am working in {Comp} as a {Rol} and work base location is {Loc}"
print(Value3)
print("*_-_*"*100)
#######################Slice indexing#####################################
str2="Hello Good morning"
print(str2[0:6])
print(str2[-7:])
print(str2[4:7])
print(str2[-20:-1])
print(str2[2:-1])
print(str2[0:18])

