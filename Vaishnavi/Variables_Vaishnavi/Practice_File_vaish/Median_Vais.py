list1=[70, 77, 80,45, 60, 61, 66 , 56]
# ((n/2 – 1) + n/2)/2
n=len(list1)
print(n) #8
list1.sort()
print(list1)#[45, 56, 60, 61, 66, 70, 77, 80]
print(list1[(n//2-1)])#61
print(list1[(n//2)])#66
median=(list1[(n//2-1)]+list1[(n//2)])/2
print(median)#63.5