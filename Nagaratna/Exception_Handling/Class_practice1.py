numbers = [10, 15, 22, 33, 44, 56,109,22,101,45]

even_numbers = []

for num in numbers:
    try:
        if num % 2 == 0:
                print("Even numbers:", num)
        else:
            continue
    except Exception as e:
        print(e)
