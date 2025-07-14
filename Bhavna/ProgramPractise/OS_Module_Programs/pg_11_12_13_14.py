# OS Module Practice Programs

import os.path

# 11). Write a Python Program To Check The File On a Given Path.

filepath = r"D:\Demo\Batch2\abc_new.txt"
print("Check file on a given path:",os.path.exists(filepath))
# Check file on a given path: True

print('_'*70)

# 12). Write a Python Program To Check The Directory On The Given Path

folderpath = r"D:\Demo\Batch2\F1"
print("Check the directory on given path:",os.path.exists(folderpath))

print('_'*70)

# 13). Write a Python Program To Get a list Of all data from the Target Path.

target_path = r"D:\Demo"
all_data = os.listdir(target_path)
print(all_data)
print("Total files/folders:",len(all_data))

print('_'*70)

# 14). Write a Python Program To Get The Total File Count In The Target Path.

def get_file_count(target_path_1):
    file_list = []

    all_data = os.listdir(target_path_1)

    for data in all_data:
        data_path = os.path.join(target_path_1,data)
        if os.path.isfile(data_path):
            file_list.append(data)

    print("Total files:",len(file_list))

get_file_count(r"D:\Demo/Batch2")