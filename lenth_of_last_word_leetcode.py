s = "Hello World"
s = s.strip()
s2 = s[::-1]
c= 0
for i in s2:
    if i.isspace():
        break
    else:
        c = c+1

print(c)