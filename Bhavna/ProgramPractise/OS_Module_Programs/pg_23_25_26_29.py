# OS Module Practice Programs

# 23). Write a Python Program To Run The Windows Commands.

os.system("dir")

print('_'*70)

# 25). Write a Python Program To Get System Version Information.
import sys
print(sys.version_info)

print('_'*70)

# 26). Write a Python Program To List Path Set Using os.get_exec_path() Method.
a = os.get_exec_path()
print(a)

print('_'*70)

# 29). Write a python Program To Get The File Size Using os.path.getsize() Method.

file_path_1 = r"D:\testScenario (1).xlsx"
print("File size:",os.path.getsize(file_path_1))

print('_'*70)
