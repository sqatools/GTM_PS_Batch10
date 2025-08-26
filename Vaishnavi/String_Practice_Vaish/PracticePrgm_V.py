"""str7 = "Good Morning"
print(str7[3:-4])
str8 = "Very Good Morning"

print(str8[2::2]) # r odMrig
str_x = "Python Pycon and Learning is easy"
print(str_x.index('o'))"""

paragraph = """Java was introduced in 1995 by Sun Microsystems. Python gained popularity after 2000, 
but it was first introduced by Guido van Rossum in 1991. JavaScript came into existence in 1995 too."""
para=paragraph.split('.')
print((para))

for senntece in para:
   if 'Python' in senntece:
       word=senntece.split()
       print(word)
for words in word:
    if words.isdigit() and (words.startswith('20') or words.startswith('19')):
        output=words
        print(output)
    else:
        continue
print("*"*90)
info = """While Python was created in 1991, its adoption skyrocketed in the 2000s. 
Java, although launched in 1995, gained enterprise traction later. 
Interestingly, JavaScript was developed in just 10 days in 1995 and revolutionized web development."""

Para1=info.split('.')
print(Para1)

for sentence in Para1:
    if 'JavaScript' in sentence:
        words=sentence.split()
        print(words)
for word in words:
    if word.isdigit() and word.isnumeric() and word.startswith("19"):
        print(word)
    else:
        continue