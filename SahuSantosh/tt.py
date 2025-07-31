s = 'abbca'
h = []

for j in range(len(s)):
    c = 0

    for k in range(len(s)):
        if s[j] == s[k]:
            c += 1
    if c == 1:
        h.append(s[j])
print(''.join(h))
