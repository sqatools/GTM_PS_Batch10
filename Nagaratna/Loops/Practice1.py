str2 = "im happy to learn python"
word = "happy"
for char in str2:
    if char in word:
        print(char)
else:
    print("City not under list")



str1 = " i love my job"
vow = "aeiou"
for char in  str1:
    if char in vow:
        print("vowel:",char)


###################################################
for val in range(1,41):
    if val%2 == 0:
        print(val,end=" ")
    else:
        pass
print( )
for s in range(1,41):
    if s%2 !=0:
        print(s,end=" ")
    else:
        pass

print( )

############################
print("::__::"*10)
import calendar
year = int(input("Enter your year"))
month = int(input("Enter your month"))
cal = calendar.month(year,month)
print(cal)
