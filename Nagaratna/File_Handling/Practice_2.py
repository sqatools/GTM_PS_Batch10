import json
"""
def Read_file(filepath,):
    fold= open(filepath,"r")
    data =fold.read()
    print(data)
    fold.close()
Read_file("My_practice_file.py")

def write_file(filepath,content):
    test=open(filepath,"w")
    test.write(content)
    test.close()
    print(content)
write_file("Created second file","Hello my second file")

def append_file(filepath,content):
    test1=open(filepath,"a")
    test1.write(content)
    test1.close()
    print(content)
append_file("C:\\Users\\nagar\\Downloads\\My_Filename.txt","Updating my python second file second time")
def sec_file(filepath):
    newfile=open(filepath,"r")
    datas=newfile.read()
    newfile.close()
    print(datas)
sec_file("C:\\Users\\nagar\\Downloads\\My_Filename.txt")

def third_file(filepath,content):
    file10=open(filepath,"w")
    file10.write(content)
    print(content)
third_file("Created second file","Python can be used for rapid prototyping, or for production-ready software development.")

#Python file program to get the file’s first three and last three lines.

def first_file(filepath):
  with open(filepath,"r")  as file:
    data5 = file.readlines()
    for i in range(0,4,1):
        print([data5[i]],end="")
    for j in range(-1,-4,-1):
        print([data5[j]],end="")
# Python file program to get a specific line from the file.
def sec_ile(filepath):
   file3= open(filepath,"r")
   data6 = file3.read()
   for m in range(7):
       print(data6[m],end="")
       file3.close()

#Python file program to get odd lines from files and append them to separate files.
def odd_file(filepath,filepath2 ):
    data7= open(filepath,"r")
    data8 =open(filepath2,"w")
    test= data7.readlines()
    print(test)
    for x in range(len(test)):
        if(x % 2!= 0):
            print(test[x])
            data8.write(test[x])
        else:
            pass
odd_file(r"C:\Users\nagar\Downloads\My_Filename.txt","Created second file")
"""
