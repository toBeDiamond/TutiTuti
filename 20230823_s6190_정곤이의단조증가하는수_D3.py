def find_b():
    global m
    for i in arr:
        if i > 9:
            flag = 1
            index = 0
            while index != len(str(i))-1:
                if int(str(i)[index]) > int(str(i)[index+1]):
                    flag =0
                    break
                index += 1

            if flag:
                if m < i:
                    m = i



T = int(input())
for t in range(1, T+1):
    N = int(input())
    a = list(map(int,input().split()))
    m = -1
    arr = [0] * 2

    for i in range(N-1):
        for j in range(i+1, N):
            arr.append(a[i]*a[j])
    find_b()

    print(f'#{t} {m}')