num1 = {"mahima" : 23, "Radha": 40}
num2 = {"Krishna" :100 , "JOSHI":45}
nums = {**num1 ,**num2 }
print("merging is",type(nums),nums)

print("*-_-*"*20)

t1 = {"suresh":10, "ganesh":20, "mahesh":30}
t2 = {"nayana":30,"yamuna":40,"bhavana":50}
mer = {**t1, **t2}
print(mer)
##########Calander############

import calendar
currant = calendar.isleap(2024)
print(currant)


print("+++++"*20)
import calendar
date = calendar.month(2025,6)
print(date)

print("**--__--**"*10)

from datetime import datetime
date1 = datetime.now().strftime('%H:%M:%S')
print(date1)

print("**--__--**"*10)

list = [95,87,34,124,89,90,54,12,0,98,43,234,864,9864]
list2 = list.sort(reverse=True)
print(list)
from _datetime import datetime
date1= datetime.now().strftime('%Y:%H:%M')
print(date1)