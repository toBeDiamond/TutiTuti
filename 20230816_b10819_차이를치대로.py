def find(v, d, a):
    global max
    if d == N:
        tmp_s = 0
        for i in range(N-1):
            tmp_s += abs(a[i] - a[i+1])
        if tmp_s > max:
            max = tmp_s
    else:
        for i in range(N):
            if v[i] == 0:
                B = v[:]
                B[i] = 1
                C = a[:]
                C.append(arr[i])
                find(B, d+1, C)

N = int(input())
arr = list(map(int,input().split()))
ans = []
visited = [0] * N
max = 0
find(visited, 0, ans)
print(max)