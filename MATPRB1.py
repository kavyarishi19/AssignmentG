import numpy
def check(a,b,n):
    for i in range(0,n):
        for j in range(0,n):
            if(a[i][j] != b[i][j]):
                return 0
    return 1
def upper(a,n):
    for i in range(1, n):
        for j in range(0, i):
            if (a[i][j] != 0):
                flag = 0
            else:
                flag = 1
    if flag==0:
	    return 0
    return 1
def lower(a,n):
    for i in range(0, n-1):
        for j in range(i+1, n):
            if (a[i][j] != 0):
                flag = 0
            else:
                flag = 1
    if flag==0:
        return 0
    return 1
T=int(input())
for T in range(T):
    n=int(input())
    a = []
    s=int(0)
    t=int(0)
    d=int(0)
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    b=numpy.transpose(a)
    s=check(a,b,n)
    if(s==1):
        s=1
    t1=upper(a,n)
    t2=lower(a,n)
    if t1 or t2:
        t=1
    if t1 and t2:
        d=1
    print(s+(2*t)+(4*d))# cook your dish here
