def write_file(filepath,content):
    file=open(filepath,"w")
    file.write(content)
    file.close()

data="""
1.The ocean is Earth’s final frontier
2.The word "bookkeeper" (and its variants) is the only unhyphenated
3.A day on Venus is longer than its year. It takes about 243 Earth days to rotate once
"""
write_file("write_file.txt",data)
write_file("my_file2.txt",data)
