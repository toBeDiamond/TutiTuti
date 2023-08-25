T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    m = k = N//2
    ans =0
    flag = 1
    for i in range(N):
        for j in range(m, k+1):
            ans += int(arr[i][j])
        if flag:
            m -= 1
            k += 1
        else:
            m += 1
            k -= 1
        if k == N-1:
            flag = 0
    print(f'#{t} {ans}')
