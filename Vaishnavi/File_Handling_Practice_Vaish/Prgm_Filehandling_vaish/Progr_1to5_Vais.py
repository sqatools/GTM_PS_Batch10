#1). Python Program How to read a file in reading mode.

def read_mode(filepath):
    file=open(filepath,"r")
    data=file.read()
    print(data)
    file.close()


read_mode("C:\\SeleniumTraining\\GTM_PS_Batch10\\Vaishnavi\\File_Handling_Practice_Vaish\\my_file2.txt")

#4). Python file program to get the file’s first three and last three lines.

def get_three_line(filepath):
    with open(filepath,"r") as file:
        data=file.readlines()
        for i in range(0,3,1):
            print(data[i],end=" ")

        for j in range(-1,-4,-1):
            print(data[j])

#get_three_line("Practice_file.txt")

#5). Python file program to get all the email ids from a text file.
def get_three_line1(filepath):
    with open(filepath,"r") as file:
        data=file.readlines()
        str1=str(data)
        list1=str1.split()
        output=[]
        for val in list1:
            for char in val:
                if char=="@":
                    output.append(val)
        print(output)


get_three_line1("Practice_file.txt")

