#l1=[4,6,8,12,67,34,50,60,70]
#output1=[12,34,50]
#Get values between 10 to 50

l1=[4,6,8,12,67,34,50,60,70]

for num in l1:
    if num>=10 and num<=50:
        print(num)
    else:
        continue


#str1="we are learning phython programming"
#output='gnimmargorp'
#get reverse of longest word
str1 = "we are learning phython programming"
words = str1.split()
long_word = max(words, key=len)
output = long_word[::-1]
print(output)

#find second largest word in given string
#learning
str2 = "we are learning phython programming"
words = str2.split()
largest = ""
second_lar = ""
for word in words:
    if len(word) > len(largest):
        second_lar = largest
        largest = word
    elif len(word) > len(second_lar) and word != largest:
        second_lar = word
print(second_lar)
