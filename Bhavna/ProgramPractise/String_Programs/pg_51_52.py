# String Practice Programs

# 51). Write a python program to replace multiple words with certain words.
# Input = “I’m learning python at Sqatools”
# Replace python with SQA  and sqatools with TOOLS

Input = "I’m learning python at Sqatools"
print(Input.replace('python','SQA').replace('Sqatools','TOOLS'))

print('_'*70)

# 52). Write a python program to replace different characters in the string at once.
Input = "Sqatool python"
a = Input.replace('a','1').replace('t','2').replace('o','3')
print(a)

print('_'*70)
