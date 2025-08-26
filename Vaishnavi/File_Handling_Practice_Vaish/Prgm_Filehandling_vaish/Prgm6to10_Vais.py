#6). Python file program to get a specific line from the file.

def read_specific_line(filepath):
    with open(filepath,"r") as f:
        data=f.readlines()
        print(data[2])

#read_specific_line("Practice_file.txt")

#7). Python file program to get odd lines from files and append them to separate files.

def read_specific_line_even(filepath,filepath2,end):
    with open(filepath,"r") as f:
        data=f.readlines()
        data1=""
        for i in range(0,end):
            if i%2==0:
                print(data[i])
                data1+=str(data[i])+"\n"
    with open(filepath2,"w") as f1:
        f1.write(data1)
#read_specific_line_even("Practice_file.txt","AnotherPractice_file.txt",18)

#8). Python file program to read a file line by line and store it in a list.
def read_specific_line_list(filepath,end):
    with open(filepath,"r") as f:
        data = f.readlines()
        list1=[]
        for i in range(0,end):
            print(data[i])
            list1.append(data[i])
        print("list :",list1)

#read_specific_line_list("Practice_file.txt",17)

#9). Python file program to find the longest word in a file.

def read_longest(filepath):
    with open(filepath,"r") as file:
        data=file.read()
        str1=str(data)
        list1=str1.split()
        output=max(list1,key=len)
        out1=min(list1,key=len)
        print("longest word:",output)
        print("shortest word:",out1)
#read_longest("AnotherPractice_file.txt")

#10). Python file program to get the count of a specific word in a file.

def count_word(filepath,word):
    with open(filepath,"r") as s:
        data=s.read().split()
        count=0
        for v in data:
            if v==word:
                count+=1
        print(word," - count :", count)

data1="consectetuer"
count_word("AnotherPractice_file.txt",data1)







