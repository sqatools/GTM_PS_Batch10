# Filter and print only the strings. below list

data = [10, "cat", 2.5, False, "dog", 99, None, "bird",True, False,]

val = []
for item in data:
     if type(item) == str:
         val.append(item)

print("The sting are:",val)
print("_"*50)

# Filter and print only the int. below list
val1 = []
for int1 in data:
    if type(int1) == int:
        val1.append(int1)
print(sum(val1))
print("_"*50)
# Filter and print only the boolen. below list

val2 =[]
for i in data:
    if type(i) == bool:
        val2.append(i)

print("The boolen expression are :", val2)
print("_"*50)

# Filter and print only the float. below list

val3 = []
for floa in data:
    if type(floa) == float:
        val3.append(floa)

print("The boolen expression are :", val3)
print("_" * 50)
# fileter not in string value only
data1 = [12, "red", 3.3, "blue", None, True, 88, "green"]
ss =[]
for s in data1:
    if type(s) != str:
        ss.append(s)
print(ss)
print("_"*50)
# filter integer and float value only
data11 = [12, "red", 3.3, "blue", None, True, 88, "green",1]
data2=[]
for H in data11:
    if type(H) == int or type(H) == float:
        data2.append(H)
print(data2)
print("_"*50)
# fiter not integer value only
data22 = ["a", "b", 1, 2.2, 3, "c", True]
data3 = []
for A in data22:
    if type(A) != int:
        data3.append(A)
print(data3)
print("_"*50)

# filter int or float value only
data23 = ["sun", 22, 3.14, "moon", "star", False, 7]
data4 =[]
for B in data23:
    if type(B) == int or type(B)==bool:
        data4.append(B)
print(data4)
print("_"*50)
# Filter and print values that are not boolean or None.
data24 = [100, 200.0, "three hundred", None, True, 500, 3.14]
data4 = []
for B1 in data24:
    if type(B1) != bool and B1 !=None:
        data4.append(B1)
print(data4)