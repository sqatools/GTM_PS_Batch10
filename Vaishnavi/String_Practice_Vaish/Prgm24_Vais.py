"""Write a Python program to find the smallest and largest word in a given string.
Input = “Learning is a part of life and we strive”
Output = “a”, “Learning”"""

i1="Learning is a part of life and we strive"
i1=i1.split()
Large=max(i1,key=len)
Small=min(i1,key=len)
print("Large:",Large)
print("Small:",Small)