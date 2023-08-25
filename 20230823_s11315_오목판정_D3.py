T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    di = [-1, -1, 0, 1]
    dj = [0, 1, 1, 1]
    flag = 0
  
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    cnt = 1
                    for p in range(1, 5):
                        ni = i + di[k] * p
                        nj = j + dj[k] * p
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                            cnt += 1
                        else:
                            break
  
                    if cnt == 5:
                        flag = 1
                        break
                if flag:
                    break
        if flag:
            break
  
    if flag:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')