import fileinput


def read_file(filepath):
    file=open(filepath,"r")
    data= file.read()
    print(data)
# read_file("Readfile_1.py")
read_file(r"C:\Users\nagar\Downloads\My_Filename.txt")

def mydata(filepath,content):
    doc = open(filepath,"w")
    doc.write(content)
    doc.close()

