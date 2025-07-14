"""print("_"*40)
def readline(filepath,count):
    with open(filepath,"r") as file:
        print(file.tell())
        for _ in range(count):
          data=file.readline()
          print(data,end=" ")
        print(file.tell())

readline("Another_file.txt",4)"""
def readline(filepath):
    with open(filepath,"rb") as file:
        file.seek(20,0)
        file.seek(30,1)
        file.seek(-40,2)
        data=file.read(20)
        print(data)

readline("my_file2.txt")





