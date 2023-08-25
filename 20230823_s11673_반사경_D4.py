dx = [1,0,0,-1]
dy = [0,-1,1,0]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    ps = 2
    arr = [ list(map(int,input().split())) for _ in range(N)]
    r = c = 0
    ans = 0
    while 0 <= r < N and 0 <= c < N:
        if arr[r][c] != 0:
            ans += 1
            if ps == 0:
                ps += arr[r][c]
            elif ps == 1:
                    ps = ((ps - arr[r][c])+4) % 4
            elif ps == 2:
                ps = (ps + arr[r][c]) % 4
            else: # ps == 3
                ps -= arr[r][c]
        r += dx[ps]
        c += dy[ps]
    print(f'#{t} {ans}')