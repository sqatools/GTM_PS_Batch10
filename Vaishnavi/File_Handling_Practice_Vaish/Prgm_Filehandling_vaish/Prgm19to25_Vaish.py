#19). Python file program to get all odd and even length words in two lists.
def read_file(filepath):
    with open(filepath,"r") as f:
        data=f.readlines()
        len1=len(data)
        even=[]
        odd=[]
        for i in range(len1):
            if i%2==0:
                even.append(data[i])
            else:
                odd.append(data[i])
        print(even)
        print(odd)



#read_file("new_practice_file.txt")

#20). Python file program to get all mobile numbers from a file. e.g each mobile number size should be 10.
def read_mobile(filepath):
     with open(filepath,"r") as f:
         data=f.read().split()
         result=[]
         for word in data:
             if word.isnumeric() and word.isdigit() and len(word)==10:
                 result.append(word)
             else:
                 continue

         print(result)
#read_mobile("sort.txt")

#21). Python file program to get a list of all domains from a file. e.g. .com, .au, .in
def read_domain(filepath):
    with open(filepath,"r") as d:
        data=d.read().split()
        print(data)
        resut=[]
        for val in data:
            if (val in ['.in'] or val in ['.com'] or [val in '.au']) and val.startswith("www"):
                resut.append(val)
            else:
                continue
        print(resut)

#read_domain("sort.txt")
#23). Python file program to count the number of lines in a file.
def count_no_line(filepath):
    with open(filepath,"r") as s:
        data=len(s.readlines())
        print(data)
#count_no_line("sort.txt")

#24). Python file program to get the file size of a file.


import os
info=os.stat("sort.txt")
print(info.st_size)

#25). Python file program to write a tuple to a file.
#26). Python file program to check whether a file is closed or not.

with open("sort2.txt","w") as w:
    tup=('1','2','3')
    w.write(" ".join(tup))
print(w.closed)

#29). Python file program to count the total number of characters in a file
def count_no_char(filepath):
    with open(filepath,"r") as d:
        data=d.read().split()
        count=0
        for word in data:
            for i in word:
                count+=1
        print(count)

#count_no_char("sort.txt")
#30). Python file program to count the total number of Uppercase characters in a file.
#31). Python file program to count the total number of Lowercase characters in a file.
#32). Python file program to count the total number of digits in a file.
#33). Python file program to count the total number of special characters in a file.

def count_upper_lower_cases(filepath):
    with open(filepath,"r") as d:
        data=d.read().split()
        upper=0
        lower=0
        Numeric=0
        special=0
        for word in data:
            for char in word:
                if char.isupper():
                    upper+=1
                elif char.islower():
                    lower+=1
                elif char.isnumeric():
                    Numeric+=1
                else:
                    special+=1

        print("no of Upper cases:",upper)
        print("no of Lower cases:", lower)
        print("no of Numeric cases:", Numeric)
        print("no of Special characters:", special)
count_upper_lower_cases("sort.txt")









