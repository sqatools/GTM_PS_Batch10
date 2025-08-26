import os
import shutil

#############
# get current working directory
print("current working path :", os.getcwd())
# current working path : E:\Trainings\GTM_PS_Batch10_8May25\GTM_PS_Batch10\Deepesh\PythonProgramming\Python_Modules

##### create new directory in current path ######
# os.mkdir("folder1")


# change working directory
"""
os.chdir("E:\\Filesdata")
print("current directory after changing the path :", os.getcwd())
# E:\Filesdata
# create directory in new path
os.mkdir("Batch10")
"""

###############################
# create folder three in target path
# os.makedirs("E:\\Filesdata\\Batch10\\f1\\f2\\f3\\f4\\f5")

#########################
# remove folder in path
"""
os.rmdir("folder1")
"""

print("_" * 50)
#########################
# get environment variable value
print("LANGUAGE Env variable:", os.getenv("LANGUAGE"))
# LANGUAGE Env variable: Python


print("_" * 50)
#########################
# get list of all file folder from target path.
tar_path = "E:\\Filesdata"
all_data = os.listdir(tar_path)
print(all_data)
print("total files/folder :", len(all_data))
for data in all_data:
    print(data)

print("_" * 50)
#########################
# join two paths:
tar_path = "E:\\Filesdata"
file_name = "count_name.txt"
filepath = os.path.join(tar_path, file_name)
print("filepath :", filepath)
# filepath : E:\Filesdata\count_name.txt

print("_" * 50)
#### check given path is exist/file/folder #####
file_path = r"E:\Filesdata\count_name.txt"
file_path2 = r"E:\Filesdata\count_name_new.txt"
folder_path = r"E:\Filesdata\Batch10"
folder_path2 = r"E:\Filesdata\Batch100"
print("check given path exist")
print("check file path exist:", os.path.exists(file_path))  # True
print("check folder path exist:", os.path.exists(folder_path))  # True
print("check folder path exist:", os.path.exists(folder_path2))  # False

print("Check for file path :", os.path.isfile(file_path))  # True
print("Check for file path2 :", os.path.isfile(file_path2))  # False

print("check for folder path :", os.path.isdir(folder_path))  # True
print("check for folder path2 :", os.path.isdir(folder_path2))  # False

print("_" * 50)


########################################################
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


get_file_folder_count(r"E:\Filesdata")


print("_"*50)
#######################################
# get size of the file
file_path_3 = "E:\Filesdata\Login_failure.png"
print("File size :", os.path.getsize(file_path_3))  # 492618 bytes

print("File modify time :", os.path.getmtime(file_path_3))
# epoch time format : 1615561501.667593
"""
GMT: Friday, March 12, 2021 3:05:01.667 PM
Your time zone: Friday, March 12, 2021 8:35:01.667 PM GMT+05:30
Relative: 4 years ago
"""

filepath_4 = r"E:\Filesdata\replace_content.txt"
print("File creation time :", os.path.getctime(filepath_4))
# 1615561501.677287
"""
GMT: Friday, March 12, 2021 3:05:01.677 PM
Your time zone: Friday, March 12, 2021 8:35:01.677 PM GMT+05:30
Relative: 4 years ago

"""

print("modify creation time :", os.path.getmtime(filepath_4))
# File creation time : 1751552742.559418
"""
Assuming that this timestamp is in seconds:
GMT: Thursday, July 3, 2025 2:25:42.559 PM
Your time zone: Thursday, July 3, 2025 7:55:42.559 PM GMT+05:30
Relative: A minute ago
"""

print("_"*50)
####################################
# execute os command with python module
# os.system("control") # open win control panel

os.system("dir C:\\") # get list of all files/folder in the given path
"""
Directory of C:\

01/07/2025  09:58 PM    <DIR>          AutomationCode
09/18/2024  10:52 PM    <DIR>          AutomationRepo
02/28/2022  11:15 PM    <DIR>          BrowserDriver
02/28/2021  10:16 PM    <DIR>          code
06/07/2021  08:30 PM    <DIR>          drivers
03/15/2025  11:03 PM            12,288 DumpStack.log
04/12/2025  02:29 AM    <DIR>          inetpub
06/06/2021  12:22 AM    <DIR>          jenkins
04/01/2024  12:56 PM    <DIR>          PerfLogs
03/15/2025  11:02 PM    <DIR>          Program Files
02/19/2025  03:51 PM    <DIR>          Program Files (x86)
10/27/2023  11:26 PM    <DIR>          Python311
03/08/2024  08:22 AM    <DIR>          Python312
11/08/2023  10:07 PM    <DIR>          PythonSelenium
03/03/2023  04:29 PM    <DIR>          RobotFramework
10/05/2020  08:28 AM    <DIR>          sqalite3
01/28/2021  07:45 PM    <DIR>          target_backup
06/08/2024  10:12 AM    <DIR>          Testdata
04/08/2022  11:02 PM    <DIR>          Training_data
02/19/2025  02:23 AM    <DIR>          Users
06/30/2025  07:16 PM    <DIR>          Windows
10/26/2020  09:04 AM                51 windows-version.txt
09/01/2020  07:37 PM    <DIR>          xampp
05/31/2025  04:45 PM    <DIR>          Youtube
               2 File(s)         12,339 bytes
              22 Dir(s)  27,957,633,024 bytes free


"""
#os.system("notepad.exe")

print("_"*50)
###########################################
# copy file from on location to another location
src_path = r"E:\Filesdata\count_name.txt"
target_path =  r"E:\Filesdata\Batch10\count_name.txt"

# copy file with same name as source
shutil.copy(src_path, target_path)


# copy file with difference name from source
target_path2 =  r"E:\Filesdata\Batch10\count_name_new.txt"
shutil.copy(src_path, target_path2)

print("_"*50)
#################### Copy directory tree to the target location ###############
src_dir_path = r"E:\Filesdata\Batch10"
tar_dir_path = r"E:\Filesdata\folder2"
shutil.copytree(src_dir_path, tar_dir_path)
