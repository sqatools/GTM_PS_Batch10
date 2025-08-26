"""
# Python file program to overwrite the existing file content.
file = open("my_file", 'w')
file.write("hello my name is nagarana")

# Python function program to add two numbers.

file = open('my_file','a')
data = file.read()
print(data)
file.close()
"""
#3). Python file program to append data to an existing file.
file =open('my_file','a')
file.write("Testing in bangalore office")
file.close()

#4). Python file program to get the file’s first three and last three lines.

file= open('my_file','r')
file.readlines()
for i in range():
    print(i)
for i in ('my_file'[:-3]):
    print(i)
#6). Python file program to get a specific line from the file.
def odd_file(filepath ):
    data7= open("C:\\Users\\nagar\\Downloads\\My_Filename.txt","r")
    data8 =open("JSON File/Dummy docs/Created second file", "w")
    test= data7.read()
    for x in range(0,len(test)):
        if((x+1) % 2!= 0):
            data8.write(test[x])
        else:
            pass
