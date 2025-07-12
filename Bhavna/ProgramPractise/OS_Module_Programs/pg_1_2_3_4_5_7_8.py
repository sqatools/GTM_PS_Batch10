# OS Module Programs

# 1). Write a Python Program To Get The Current Working Directory.
import os

print("current Working Directory:",os.getcwd())

print('_'*70)

# 2). Write a Python Program To Get The Environment Variable

print("Environment Variable:",os.getenv("USERNAME"))

print('_'*70)

# 3). Write a Python Program To Set The Environment Variable

os.environ["TEST"] = "Hello"
print(os.environ["Test"])

print('_'*70)

# 4). Write a Python Program To Get a List Of All Environment Variable Using os.environ.

print(os.environ)

# 5). Write a Python Program To Create a Directory Using os.mkdir()

# os.mkdir("F1")

print('_'*70)

# 7). Write a Python Program To Create 10 DirecTories On a Nested Level.

# os.makedirs(r"D:\Demo\Practice\F1\F2\F3\F4\F5\F6\F7\F8\F9\F10")

# 8). Write a Python Program To Remove An Empty Directory Using os.rmdir()

# os.rmdir("F2")