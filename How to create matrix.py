N = int(input())
matrix = []
for i in range(N):
    c = []
    for j in range(N):
        j = int(input(str(i)+" "+str(j)+ " "))
        c.append(j)
    print()
    matrix.append(c)
for i in range(N):
    for j in range(N):
        print(matrix[i][j],end=" ")
    print()
