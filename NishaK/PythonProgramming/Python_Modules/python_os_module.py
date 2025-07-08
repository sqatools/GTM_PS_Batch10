import os
import shutil

# get current working directory
print("Current working path :", os.getcwd())
# Current working path : C:\SeleniumTraining\AutomationRepo\GTM_PS_Batch10\NishaK\PythonProgramming\Python_Modules


# create new directory
# os.mkdir("Folder1")


# change working directory
# os.chdir("C:\SeleniumTraining\AutomationRepo")
# print("Current working path after change:", os.getcwd())
# Current working path after change: C:\SeleniumTraining\AutomationRepo


# create folder three in target path
# os.mkdir("C:\\SeleniumTraining\\AutomationRepo\\GTM_PS_Batch10\\NishaK\\PythonProgramming\\Python_Modules\\Folder1\\f1\\f2")


# remove folder in path
# os.rmdir("Folder1")


print("-"*50)
# get environment variable value
print("USERNAME Env variable:", os.getenv("USERNAME"))
# USERNAME Env variable: Shree Laptop


print("-"*50)
# get list of all file folder from target path.
tar_path = "C:\SeleniumTraining\AutomationRepo\GTM_PS_Batch10"
all_data = os.listdir(tar_path)
print(all_data)
print("total files/folder :", len(all_data))
for data in all_data:
    print(data)


print("-"*50)
# join two paths

tar_path = "C:\SeleniumTraining\AutomationRepo\GTM_PS_Batch10"
file_name = "Test_Git_File.txt"
filepath = os.path.join(tar_path, file_name)
print("filepath :", filepath)
# filepath : C:\SeleniumTraining\AutomationRepo\GTM_PS_Batch10\Test_Git_File.txt


print("-"*50)
# check given path is exist/file/folder
file_path = "C:\SeleniumTraining\AutomationRepo\First_Git_File.txt"
file_path2 = "C:\SeleniumTraining\AutomationRepo\First_Git_File_2.txt"
folder_path = "C:\SeleniumTraining\AutomationRepo\GTM_PS_Batch10"
folder_path2 = "C:\SeleniumTraining\AutomationRepo\GTM_PS_Batch100"
print("Check given path exist")
print("Check the file path exist :", os.path.exists(file_path))
print("Check the folder path exist :", os.path.exists(folder_path))
print("Check the file path exist :", os.path.exists(folder_path2))
# Check given path exist
# Check the file path exist : True
# Check the folder path exist : True
# Check the file path exist : False


print("-"*50)
print("Check for file path :", os.path.isfile(file_path))
print("Check for file path2 :", os.path.isfile(file_path2))
print("Check for folder path :", os.path.isfile(folder_path))
print("Check for folder path2 :", os.path.isfile(folder_path2))
# Check for file path : True
# Check for file path2 : False
# Check for folder path : False
# Check for folder path2 : False


print("-"*50)
# write  a program to get count of files and folder in target path.

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


get_file_folder_count("C:\SeleniumTraining\AutomationRepo\GTM_PS_Batch10")
# Total files : 3
# Total folders : 23


print("-"*50)
# get size of the file
file_path3 = "C:\SeleniumTraining\AutomationRepo\First_Git_File.txt"
print("File size :", os.path.getsize(file_path3))
# File size : 70


print("-"*50)
print("File modify time :", os.path.getmtime(file_path3))
# File modify time : 1747129123.2265024
"""
GMT: Tuesday, May 13, 2025 9:38:43.226 AM
Your time zone: Tuesday, May 13, 2025 3:08:43.226 PM GMT+05:30
Relative: 2 months ago
"""


print("-"*50)
os.system("dir C:\\")
"""
Volume in drive C has no label.
 Volume Serial Number is E82B-B394

 Directory of C:\

10-04-2025  13:12    <DIR>          inetpub
02-07-2025  21:09    <DIR>          Intel
03-07-2025  16:15                90 logUploaderSettings.ini
03-07-2025  16:15                90 logUploaderSettings_temp.ini
07-12-2019  14:44    <DIR>          PerfLogs
16-05-2025  19:25    <DIR>          Program Files
25-04-2025  18:46    <DIR>          Program Files (x86)
16-05-2025  19:19    <DIR>          Python3
09-05-2025  19:54    <DIR>          SeleniumTraining
10-04-2025  12:51    <DIR>          Users
24-06-2025  12:43    <DIR>          Windows
               2 File(s)            180 bytes
               9 Dir(s)  204,268,916,736 bytes free
"""

# os.system("notepad.exe")


print("-"*50)
# copy file from one location to another
src_path = "C:\SeleniumTraining\Test_File.txt"
target_path = "C:\SeleniumTraining\AutomationRepo\Test_File.txt"

shutil.copy(src_path, target_path)

target_path2 = "C:\SeleniumTraining\AutomationRepo\Test_File_New.txt"
shutil.copy(src_path, target_path2)