def read_file(filepath):
    file=open(filepath,"r")
    data=file.read()
    print(data)

read_file("my_file.txt")
read_file(r"C:\Users\vaish\Downloads\Github Day2.txt")