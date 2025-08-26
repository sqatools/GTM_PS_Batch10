import json
def readfile(filepath):
    file =open(filepath,"r")
    data=file.read()
    print(data)
    file.close()
readfile("my_file")

"""def writefile(filepath,content):
    file1= open(filepath,"w")
    file1.write(content)
    file1.close()
writefile("Write_new file","Hello Good morning")"""

def writefile1(filepath,content):
    file2=open(filepath,"a")
    file2.write(content)
    print(content)
    file2.close()
writefile1("JSON File/Write_new file", " python library used for working with arrays.")
