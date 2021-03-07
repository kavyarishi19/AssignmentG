T = int(input())
for q in range(T):
    M = int(input())
    flag = 0
    arr=[]
    for i in range(1, M+ 1):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                arr.append(i)
    print(arr)
    for ii in range(len(arr)):
        if arr[ii] < M and M - arr[ii] > 0 and M - arr[ii] in arr  :
            print(arr[ii],end=" " )
            print((M - arr[ii]))
            flag=1
            break

    if flag == 0 :
        print(-1 , end=" ")
        print(-1)
