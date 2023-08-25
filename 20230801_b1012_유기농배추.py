import sys

# 재귀함수 깊이를 늘려줌 백준은 1000까지 허용되서 더 늘렸다.
sys.setrecursionlimit(10000)


def check(r, c):
    # arr 2차원 리스트 호출
    global arr

    # 현재위치 배추를 2으로 바꿔준다. -> 중복방지
    arr[r][c] = 2
    # 배추기준 상하좌우 좌표
    x = [0, 0, -1, 1]
    y = [1, -1, 0, 0]
    # 4방향 순환
    for i in range(4):
        # 바뀐 좌표가 2차원 리스트 범위를 벗어나면 넘어간다.
        if r - x[i] < 0 or r - x[i] >= n or c - y[i] < 0 or c - y[i] >= m:
            continue
        # 배추를 찾으면 찾은 배추좌표를 check()함수에 넣어준다. (재귀)
        if arr[r - x[i]][c - y[i]] == 1:
            check(r - x[i], c - y[i])


T = int(input())
for t in range(T):

    # 가로길이=m , 세로길이=n , 배추의수=k
    m, n, k = map(int, input().split())

    # 가로 * 세로 2차원 리스트 생성
    # [[0] * m ] * n 을 해버리면 얉은복사가 되서 값이 다 바뀜
    arr = [[0 for j in range(int(m))] for i in range(n)]

    # 배추 위치를 받아 1로 바꿔준다.
    for i in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1

    # 총 벌레의 수를 0으로 초기화
    bug = 0

    # 2차원 리스트를 순환
    for i in range(n):
        for j in range(m):
            # 배추를 찾으면
            if arr[i][j] == 1:
                # check()함수에 배추 위치를 넣어준다.
                check(i, j)
                bug += 1
    print(bug)