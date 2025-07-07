import sys


# argv accepts the parameter in the form of list values.
file_prams = sys.argv
print(file_prams)
# ['.\\python_sys_module.py',  'Hello', 'Good', 'Morning', '123']


print("-"*50)
# get version info
print(sys.version_info)
# sys.version_info(major=3, minor=13, micro=3, releaselevel='final', serial=0)


print("-"*50)
print(sys.version)
# 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)]


print("-"*50)
# Get platform name
print(sys.platform)
# win32