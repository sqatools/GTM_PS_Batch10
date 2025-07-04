#Q) write a python program to get all values from above setup

l2 = {'python','programming','language'}
output = set()
for word in l2:
    if len(word) >= 2:
        output.add(word[:2])  # first 2 letters
    if 'an' in word:
        output.add('an')
    if 'ng' in word:
        output.add('ng')
    if word.endswith('age'):
        output.add('age')
    if word.startswith('pr'):
        output.add('pr')
    if word.startswith('la'):
        output.add('la')
print(output)

for word in l2:
    if len(word) >=6:
        output.add(word[:6])
    if 'Python' in word:
        output.add('Python')
    if 'Programin'