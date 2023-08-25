'''
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
'''
import sys;
from collections import deque;
sys.stdin=open('./7576_토마토.py', encoding='utf-8')
_ = input()

# 상하좌우 방향
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 그래프 가로 세로 크기 n, m
n, m = map(int,input().split())

# 토마토 상자를 가져온다.
arr = [list(map(int,input().split())) for _ in range(m)]

# deque 선언
Q = deque()

# n,m크기의 배열을 0으로 초기화
day = [[0]*n for _ in range(m)]

# 배열 순환
for i in range(m):
    for j in range(n):
				# 익은 토마토 좌표를 Q에 넣는다.
        if arr[i][j] == 1:
            Q.append((i,j))
# Q 길이가 0이 될 때 까지 무한 반복
while Q:
		# 맨 처음 넣은 익은 토마토 좌표를 꺼낸다.
    tmp = Q.popleft()
		# 좌표 기준 4방향 탐색
    for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]
				# 방향에 안 익은 토마토가 있으면
        if 0 <= xx < m and 0 <= yy < n and arr[xx][yy] == 0:
						# 토마토를 익혀준다.
            arr[xx][yy] = 1

						# day배열 안 익은 토마토 좌표에 익은 토마토 좌표 값 +1을 넣어준다.
            day[xx][yy] = day[tmp[0]][tmp[1]] + 1

						# 익어버린 토마토 좌표를 넣는다.
            Q.append((xx, yy))

# 가장 오래 걸린 날짜
max = 0
# 안익은 토마토가 있는지 확인 
flag = True

# day 배열 순환
for i in range(m):
    for j in range(n):
				# 익히는데 오래걸린 토마토가 있으면 날짜 갱신
        if day[i][j] > max:
            max = day[i][j]
				# 안익은 토마토가 있으면 False로 바꾼다
        if arr[i][j] == 0:
            flag = False

# 토마토가 다 익었으면
if flag:# 가장 오래걸린 날짜 출력
    print(max)
else: # 안익은 토마토가 있으면 -1 출력
    print(-1)