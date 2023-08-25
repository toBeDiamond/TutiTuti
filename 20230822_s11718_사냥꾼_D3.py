T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dx = [-1,0,1,1,1,0,-1,-1]
    dy = [1,1,1,0,-1,-1,-1,0]
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1: # 사냥꾼일때 사냥 시작
                for k in range(8):
                    tmp = 0
                    flag = 1
                    w = 1
                    while 1:
                        if 0 <= i+dx[k]*w < N and 0 <= j+dy[k]*w < N:
                            if arr[i+dx[k]*w][j+dy[k]*w] == 1:
                                flag = 0
                                break
                            elif arr[i+dx[k]*w][j+dy[k]*w] == 2:
                                tmp += 1
                            elif arr[i+dx[k]*w][j+dy[k]*w] == 3:
                                break
                            w += 1
                        else:
                            break
                    if flag:
                        ans += tmp
    print(f'#{t} {ans}')