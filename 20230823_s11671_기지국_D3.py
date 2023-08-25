T = int(input())
dr = [0,0,-1,1]
dc = [1,-1,0,0]
for t in range(1, T+1):
    N = int(input())
    arr = [ list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 'H' and arr[i][j] != 'X' :
                for k in range(4):
                    for w in range(1,ord(arr[i][j]) - 63):
                        if 0<=i+dr[k]*w < N and 0 <= j+dc[k]*w < N and arr[i+dr[k]*w][j+dc[k]*w] == 'H':
                            arr[i + dr[k] * w][j + dc[k] * w] = 'X'
                                
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                ans += 1
    print(f'#{t} {ans}')