import sys


# argv accepts the parameter in the form of list values.
file_params = sys.argv
print(file_params)
# ['.\\python_sys_module.py', 'Hello', 'Good', 'Morning', '123']

###################### get version info ##########
print(sys.version_info)
# sys.version_info(major=3, minor=12, micro=2, releaselevel='final', serial=0)

print(sys.version)
# 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]

##################### Get platform name #############
print("platform name :", sys.platform)
# platform name : win32
