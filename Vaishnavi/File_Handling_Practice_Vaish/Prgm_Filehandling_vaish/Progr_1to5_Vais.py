#1). Python Program How to read a file in reading mode.

def read_mode(filepath):
    file=open(filepath,"r")
    data=file.read()
    print(data)
    file.close()


read_mode("C:\\SeleniumTraining\\GTM_PS_Batch10\\Vaishnavi\\File_Handling_Practice_Vaish\\my_file2.txt")

#4). Python file program to get the file’s first three and last three lines.

