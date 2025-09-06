#Custom Exception Class

class AgeIsTooSmall(Exception):
    pass

def Age(n):
    try:
        if n<18:
           raise AgeIsTooSmall("Age is too small")
        else:
            print("eligible")

    except Exception as f:
        print(f)

Age(14)

try:
    with open("file.txt", "r") as f:
        content = f.read()
        print(content)
except Exception as e:
    print(e)
"""except FileNotFoundError:
    print("The file does not exist.")"""