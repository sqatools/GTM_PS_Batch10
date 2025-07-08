"""Write a python program to re-arrange the string.
Input = “Cricket Plays Virat”
Output = “Virat Plays Cricket”"""
input1="Cricket Plays Virat"
output=input1.split()
result=output[2]+ " " +output[1]+" "+output[0]
print(result)