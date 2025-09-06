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


def get_file_folder_count(tar_path):
    files_list = []
    folder_list = []
    # get list of all file/folder
    all_data = os.listdir(tar_path)
    # loop over file/folder list
    for data in all_data:
        # get path of the file/path
        data_path = os.path.join(tar_path, data)
        # check given path is file or not
        if os.path.isfile(data_path):
            # if isfile is true then add in files_list
            files_list.append(data)
        else:
            # if isfile is False then add in folder_list
            folder_list.append(data)

    print("Total files :", len(files_list))
    print("Total folders :", len(folder_list))


get_file_folder_count(r"/Users/Sathish/Projects/br/")

print("_"*50)
#######################################
# get size of the file
file_path_3 = "/Users/Sathish/Projects/br/f1/f2/f3/f4/f5/DSC_0255_TEST.jpg"
print("File size :", os.path.getsize(file_path_3))  # 492618 bytes

print("File modify time :", os.path.getmtime(file_path_3))

print("_"*50)
####################################
# execute os command with python module
# os.system("control") # open win control panel

#os.system("ls /Users/Sathish") # get list of all files/folder in the given path
os.system("ls")