a = ["flow","flower","floight"]
res = ""
prefix=""
prefix = min(a,key=len)
count = 0
need = len(a)
while(count != need):
    count = 0
    for i in a:
        if(prefix == i[:len(prefix)]):
            count += 1
    res = prefix
    prefix = prefix[:-1]

if(need == count):
    print(res)
else:
    pass




