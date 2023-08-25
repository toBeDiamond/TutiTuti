'''
3 4 5
3 2
2 2
3 1
2 3
1 1
'''
# 터치 X
import sys; sys.stdin=open('./Test.py', encoding='utf-8'); _=input()
sys.setrecursionlimit(10000) # 재귀 한도 늘려주기
def find_ss(arr, r, c, count):
    # 쓰레기 크기 += 1
    count += 1
    
    # 측정한 쓰레기는 0으로 바꿔주기 > 중복 방지
    arr[r][c] = 0
    
    # 4방향 탐색
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        # 쓰레기 옆 좌표가 복도 범위 안에 있다면?
        if 0<= r+dx[i] < N and 0 <= c+dy[i] < M:
            
            # 옆 좌표에 쓰레기가 있다면?
            if arr[r+dx[i]][c+dy[i]] == 1:
                
								# 옆 좌표를 기준으로 다시 쓰레기를 찾아 기존 count와 더한다.
                count = find_ss(arr, r+dx[i], c+dy[i], count)
      
    # 찾은 쓰레기 크기 반환
    return count

# 복도 가로길이, 세로길이, 쓰레기 개수 받기
N, M, K = map(int,input().split())

# 쓰레기 없는 복도 배열
arr = [[0]*M for _ in range(N)]

# 쓰레기 채워주기
for i in range(K):
    a, b = map(int,input().split())
    arr[a-1][b-1] = 1

# 가장 큰 쓰레기 크기 max
max = 0
# 쓰레기 복도 순환
for i in range(N):
    for j in range(M):
        # 쓰레기를 발견하면?
        if arr[i][j] == 1:
            # 쓰레기 크기 측정
            aa = find_ss(arr, i, j, 0)

            if aa > max:
                max = aa

print(max)