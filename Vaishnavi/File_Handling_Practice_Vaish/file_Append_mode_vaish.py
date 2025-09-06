def append_mode(filepath,content):
    file=open(filepath,"a")
    file.write(content)
    file.close()

data="""
Append method will update thee file
it wont override the file\n
"""

append_mode("append_file.txt",data)