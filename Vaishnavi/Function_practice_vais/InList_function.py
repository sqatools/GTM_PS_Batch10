"""
11). Python function program to find the even numbers from a given list.
Input :
Output : [2, 4, 6, 8]
"""
def in_list(*args):
    output=[]
    for i in args:
        if isinstance(i,list):
            len2=len(i)
            print(len2)
            for k in range(len2):
                if i[k]%2==0:
                    output.append(i[k])
                else:
                    continue
            return output


print(in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 20, 24, "Hi"))



