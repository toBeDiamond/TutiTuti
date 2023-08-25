import sys
sys.setrecursionlimit(10000)

# 같은 색을 체크 해주는 함수
def change_C(arr, value, r, c):

		# 해당 값을 체크해준다.
    arr[r][c] = 'C'

		# 4방향 탐색
    for i in range(4):

				# i 방향으로 나아간 좌표가 리스트 범위를 벗어나지 않았다면
        if 0<= r+dx[i] < N and 0<= c+dy[i] < N:

						# 색이 서로 같은가?
            if arr[r+dx[i]][c+dy[i]] == value:
								# 나아간 좌표 근처에 같은 색이 있는지 찾아본다.
                change_N(arr, arr[r+dx[i]][c+dy[i]], r+dx[i] ,c+dy[i])
    return arr

# 4방향 
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 리스트 길이 N
N = int(input())
# 오리지널 리스트
origin_arr = [list(input()) for _ in range(N)]

# 리스트 깊은 복사
blined_arr = [i[:] for i in origin_arr]

# 적록색맹 리스트로 바꾸기
for i in range(N):
    for j in range(N):
        if blined_arr[i][j] == 'G':
            blined_arr[i][j] = 'R'

# 정답을 담기위한 ans
ans = []
# original , blined 순서로 진행
for t in [origin_arr, blined_arr]:
		# 영역의 개수
    count = 0

		# 리스트 순환
    for i in range(N):
        for j in range(N):

						# 아직 체크되지 않았다면
            if t[i][j] != 'C':

                # 근처 같은색을 다 체크해 버린다.
                t = change_C(t, t[i][j], i, j)
								
								# 영역 개수 + 1
                count += 1

		# 영역을 다 찾았다면 ans에 더 해준다.
    ans.append(count)

print(*ans)