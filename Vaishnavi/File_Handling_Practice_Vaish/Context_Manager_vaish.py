def context_mangr(filepath):
    with open(filepath,"r") as file:
        data=file.read()
        print(data)
        print("file closed ?",file.closed)
    print("outer loop file closed?",file.closed)

context_mangr("my_file.txt")