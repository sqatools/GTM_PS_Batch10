# 04/07/2025 Session Continue

import sys

# argv accepts the parameter in the form of list values
file_parameter = sys.argv
print(file_parameter)
# ['.\\python_sys_module.py', 'Hello', 'Good', 'Evening', 'Guys', '147']

###################### get version info ##########

print(sys.version_info)
# sys.version_info(major=3, minor=13, micro=3, releaselevel='final', serial=0)

print(sys.version)
# 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)]

##################### Get platform name #############
print("Platform name:",sys.platform)
# Platform name: win32