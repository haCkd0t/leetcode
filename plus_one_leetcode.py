a = [9]
a2 =""
a3=[]
for i in range(len(a)):
    j = a[i]
    j = str(j)
    a2 = a2+j
a2 = int(a2)
a2 = a2+1
while(a2!=0):
    r = a2%10
    a3.append(int(r))
    a2 = a2//10

a3.reverse()
a.clear()
a = a3
print(a)

