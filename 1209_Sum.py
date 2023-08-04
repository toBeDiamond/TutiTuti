import sys; sys.stdin=open('./input/input_1209.txt')

for _ in range(10):
    t = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    max = 0
    tmp_lx = 0
    tmp_rx = 0
    for i in range(100):
        tmp_lx += arr[i][i]
        tmp_rx += arr[i][99 - i]
        tmp_row = 0
        tmp_col = 0
        for j in range(100):
            tmp_row += arr[i][j]
            tmp_col += arr[j][i]
        if tmp_row > max:
            max = tmp_row
        if tmp_col > max:
            max = tmp_col
    if tmp_lx > max:
        max = tmp_lx
    if tmp_rx > max:
        max = tmp_rx
    print(f'#{t} {max}')