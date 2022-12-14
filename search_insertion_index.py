a = [111]
t =71
print(len(a))
size = len(a)-1
if(((len(a)) == 1) and t>a[0]):
    print(len(a))
elif(((len(a)) == 1) and t<a[0]):
    print(len(a)-1)
elif((a[len(a)-1])<t):
    print(len(a))
else:
    for i in range(len(a)):
        if(a[i]==t):
            print(i)
        elif((a[i]<t) and (a[i+1]>t) ):
            print(i+1)
            break
        else:
            continue
