# 03/07/2025 Session

import os

##########
# get current working directory
print("current working Path:",os.getcwd())
# current working Path: C:\AutomationCourse\GTM_PS_Batch10\Bhavna\ProgramPractise\Classwork\Python_Modules

######## Create new directory in current path #########
# os.mkdir("Folder1")

# Change working Directory
"""
os.chdir("D:\\Demo")
print("current directory after changing the path:",os.getcwd())

# current working Path: C:\AutomationCourse\GTM_PS_Batch10\Bhavna\ProgramPractise\Classwork\Python_Modules
# current directory after changing the path: D:\Demo

#Create directory in new path
os.mkdir("Batch1")

"""
##############################
# Create folder three in target path

# os.makedirs("D:\\Demo\\Batch1\\F1\\F2\\F3")

####################################
#remove folder in path

# os.rmdir("Folder1")

print('_'*70)
#############################################
# get environment variable value
print("USERNAME Environment variable:",os.getenv("USERNAME"))
# USERNAME Environment variable: BHAVANA P

print("_"*70)

###########################################
# Get list of all file folder from target path
target_path = "D:\\Demo"
all_data = os.listdir(target_path)
print(all_data)
print("total files/folders:",len(all_data))
for data in all_data:
    print(data)

print("_"*70)
##############################################
# join two paths:
target_path = "D:\\Demo"
file_name = "read1"
file_path = os.path.join(target_path,file_name)
print("filepath:",file_path)
# filepath: D:\Demo\read1
print('_'*70)

#### check given path is exist/file/folder #####
file_path1 = r"D:\Demo\read1.txt"
folder_path = r"D:\Demo\Batch1"
print("check given path exist:",os.path.exists(file_path1))
print("check given folder exist:",os.path.exists(folder_path))
folder_path3 = r"D:\Demo\Batch2"
print("check given folder exist:",os.path.exists(folder_path3))
file_path4 = r"D:\abc.txt.txt"
print("check given path exist:",os.path.exists(file_path4))

print("check for file path:",os.path.isfile(file_path4)) #True
print("check for folder path:",os.path.isdir(folder_path3)) #True


########################################################
# write  a program to get count of files and folder in target path.

def get_file_folder_count(tar_path):
    file_list = []
    folder_list = []
    all_data = os.listdir(tar_path)
    # loop over file/folder list
    for data in all_data:
        # get path of the file/path
        data_path = os.path.join(tar_path,data)
        # check given path is file or not
        if os.path.isfile(data_path):
            # if isfile is true then add in files_list
            file_list.append(data)
        else:
            # if isfile is False then add in folder_list
            folder_list.append(data)

    print("Total Files:",len(file_list))
    print("Total Folders:",len(folder_list))

get_file_folder_count(r"D:\Demo")

print('_'*70)

###############################################
# get size of the file
filepath1 = r"D:\Iphone\202302__\IMG_0064.MOV"
print("File Size:",os.path.getsize(filepath1)) #4217275 bytes

print("File Modify Time:",os.path.getmtime(filepath1)) # 1731980286.0
# epoch time format : 1731980286
'''
GMT: Tuesday, 19 November 2024 01:38:06
Your time zone: Tuesday, 19 November 2024 07:08:06 GMT+05:30
Relative: 8 months ago
'''

print('_'*70)

####################################
# execute os command with python module
# os.system("control") # open win control panel

# os.system("dir D:\\")

# os.system("notepad")
