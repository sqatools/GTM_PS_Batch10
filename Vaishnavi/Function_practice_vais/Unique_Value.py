"""9). Python function program that takes a list and returns a new list with unique elements of the first list.
Input : [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
Output : [2, 3, 1, 4, 6 ]"""

def get_unique_from_args(*args):
    for item in args:
        if isinstance(item, list):  # Only process the list input
            output = []
            for val in item:
                if val not in output:
                    output.append(val)
            return output
    return []  # If no list is found in args

# Test the function
print(get_unique_from_args([2, 2, 3, 1, 4, 4, 4, 4, 4, 6], 20, 24, "Hi"))
