T = int(input())
for i in range(T):
    x, y , xe , ye = map(int, input().split())
    m = xe - x
    n = ye - y
    ar=[]
    while x is not xe :
        if m >= 0 :
            x=x+1
            ar.append("E")
        else:
            x=x-1
            ar.append("W")
    while y is not ye:

        if n >= 0 :
            y = y+1
            ar.append("N")
        else:
            y = y-1
            ar.append("S")
    print(len(ar))
    ar = ''.join(map(str, ar))
    print(ar)


