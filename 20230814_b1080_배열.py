N, M = map(int,input().split())
arr1 = [list(map(int,input())) for _ in range(N)]
arr2 = [list(map(int,input())) for _ in range(N)]

ans = 0
for i in range(N-2):
    for j in range(M-2):
        if arr1[i][j] != arr2[i][j]:
            ans += 1
            for k in range(3):
                for w in range(3):
                    if arr1[i+k][j+w] == 1:
                        arr1[i + k][j + w] -= 1
                    else:
                        arr1[i + k][j + w] += 1+

for i in range(N):
    for j in range(M):
        if arr1[i][j] != arr2[i][j]:
            ans = -1
    
print(ans)