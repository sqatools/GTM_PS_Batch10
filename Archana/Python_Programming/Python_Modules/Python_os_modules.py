import os
#############
# get current working directory
print("current working path :", os.getcwd())
#current working path : /Users/Sathish/Documents/SeliniumTraining/GTM_PS_Batch10/Archana/Python_Programming/Python_Modules

##### create new directory in current path ######
#os.mkdir("folder1")


# change working directory
os.chdir("/Users/Sathish/Projects/br")
print("current working path after change :", os.getcwd())
#current working path after change : /Users/Sathish/Projects/br

# create directory in new path
#os.mkdir("Batch10")

###############################
# create folder tree in target path
#os.makedirs("/Users/Sathish/Projects/br/f1/f2/f3/f4/f5")
# nested files created successfully
print("current working path :", os.getcwd())

print("_" * 50)
#########################
# get list of all file folder from target path.
tar_path = "/Users/Sathish/Projects/br/f1"
all_data = os.listdir(tar_path)
print(all_data)
print("total files/folder :", len(all_data))
for data in all_data:
    print(data)

print("_" * 50)
#########################
# join two paths:
tar_path = "/Users/Sathish/Projects/br"
file_name = "count_name.txt"
filepath = os.path.join(tar_path, file_name)
print("filepath :", filepath)




print("_" * 50)
#### check given path is exist/file/folder #####
file_path = "/Users/Sathish/Projects/br/count_name.txt"
#file_path2 = r"E:\Filesdata\count_name_new.txt"
folder_path = "/Users/Sathish/Projects/br/"
folder_path2 = "/Users/Sathish/Projects/br1/"
print("check given path exist")
print("check file path exist:", os.path.exists(file_path))  # True
print("check folder path exist:", os.path.exists(folder_path))  # True
print("check folder path exist:", os.path.exists(folder_path2))  # False


# find a python program to get ecven numbers from list with exception handling
def Exception_handling_even(list1):

    try:
        for i in list1:
            if i % 2 == 0:
                print("Is a even number:", i)
            else:
                continue
    except Exception as e:
        print("Can not validate a string value ")
        print(e)

list1 = [3, 5, 6, 8, 10]
Exception_handling_even('Good Morning')