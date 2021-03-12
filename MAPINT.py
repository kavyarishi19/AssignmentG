n = int(input())
dictt= {}
count=0
for j in range(n):
    a, b, name, dirr = input().strip().split()
    for i in a, b :
        if i in dictt:
            dictt[i].append(name)

        else:
            dictt[i] = [name]
for key, value in dictt.items():
    aa = []
    if len(list(filter(bool, value))) == 4:
        aa.append(value)
        s=[]
        for i in range(0,4):
            s.append(aa[0][i])
        ss=set(s)
        if len(ss)==2:
            count+=1
print(count)
