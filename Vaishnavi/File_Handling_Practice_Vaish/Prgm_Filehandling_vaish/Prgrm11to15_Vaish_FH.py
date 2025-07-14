#11). Python file program to read a random line from a file.

def read_random_line(filepath):
    import random
    with open(filepath,"r") as f:
        data=f.read().splitlines()
        randomline=random.choice(data)
        print(randomline)

#read_random_line("Practice_file.txt")

#12). Python file program to copy the file’s contents to another file after converting it to lowercase.
#13). Python file program to copy the file’s contents to another file after converting it to uppercase.

def copy_file(filepath,filepath2,filepath3):
    with open(filepath,"r") as f:
        data=f.read()
        content=data.lower()
        content2=data.upper()
        print(content)
    with open(filepath2,"w") as f1:
        f1.write(content)
    with open(filepath3,"w") as f2:
        f2.write(content2)
#copy_file("Practice_file.txt","new_practice_file.txt","Uppercase_file.txt")

#14). Python file program to count all the words from a file

def count_words(filepath):
    with open(filepath) as g:
        data=g.read().split()
        print(data)
        count=0
        for i in data:
            count+=1
        print(count)

#count_words("AnotherPractice_file.txt")

#15). Python file program to sort all the lines File as per line length size.

def sort_line(filepath):
    with open(filepath,"r") as f:
        data=f.readlines()
        data.sort()
        for val in data:
            print(val)
sort_line("Uppercase_file.txt")
