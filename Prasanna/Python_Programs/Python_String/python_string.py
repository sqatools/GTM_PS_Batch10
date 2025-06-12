str1 = "Hi hello prasanna this is python programing hope are you intrested to learn python"
print(str1, type)
language = " python "
name = "chandu"
str2 = "Hi hello"  +  name  + "this is"  +  language  +  "programing"
print(str2)
# 2. Format Method:
str2 = "hi hell0 {} i am learning {}".format(name, language)
print(str2)
# F string formating:
str3 = f"Hi hello {name} i am learning {language}"
for i in range(len(str3)):
    print(i, str3)
for char in str3:
    print(str3)

# slicing in string
"""
Rule1 : str[start_index: last index]
->  Default step value is 1
->  Result will include start_index character and exclude last index char in the output
->  Result value will always print from left to right:
->  start and index index value could be positive or negative
->  If we dont provide the last index the default last index would end of string. 
    e.g.  str[4:] # here output will be from 4 to end of string.
->  Default start_index is zero str[:3] # Here output will output value from 0 to 2
# String Method
print(dir(str))
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
# 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
# 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
# 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
# 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', # 
'zfill']
"""





