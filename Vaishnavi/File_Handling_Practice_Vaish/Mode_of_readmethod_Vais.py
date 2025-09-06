#1.Read bytes

def read_no_of_bytes(filepath,bytes):
    with open(filepath,"r") as file:
        data=file.read(bytes)
        print(data)
read_no_of_bytes("my_file.txt",5)

print("_"*80)

#2.read line

def read_line(filepath):
    with open(filepath,"r") as f1:
        print("is readable file?",f1.readable())
        data1=f1.readline()
        print(data1)
read_line("write_file.txt")

print("_"*80)

def read_line(filepath,count):
    with open(filepath,"r") as f1:
        print("is readable file?",f1.readable())
        for i in range(count):
            data1=f1.readline()
            print(data1)
read_line("write_file.txt",4)

print("_"*80)
#3.Read list of lines

def read_list(filepath,start,end):
    with open(filepath,"r") as file:
        list=file.readlines()
        print(list)

        for i in range(start-1,end,1):
            print(list[i],end=" ")

read_list("write_file.txt",2,6)

print("_"*80)
#tell() method

def read_list1(filepath):
    with open(filepath,"r") as file:
        print("start:",file.tell())
        list=file.readlines()
        print(list)
        print("End:", file.tell())

read_list1("write_file.txt")
