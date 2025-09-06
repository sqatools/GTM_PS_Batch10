"""Find the longest and smallest word in the input string."""

str1="longesttt and smallest word in the input string"
list1=str1.split()

max_word=max(list1, key=len)
min_word=min(list1, key=len)
print("Max:", max_word , len(max_word))
print("Max:", min_word , len(min_word))
