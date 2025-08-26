# get even no from list
def Even_no(*args):
    try:
        for item in args:
            if isinstance(item, list):
                for num in item:
                    if num % 2 == 0:
                        print(num, ": No is even")
    except Exception as e:
        print("Error:", e)
    else:
        print("Execution successful!!")


Even_no(2, 3, [2, "heelo", 6, 5, 67, 82])
