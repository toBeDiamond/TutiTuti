def peak(arr, max2):
		# 현재 높이
    now = arr[max2[0]][max2[1]]

		# 현재 좌표를 0으로 바꾼다. 방문체크
    arr[max2[0]][max2[1]] = 0

		# 8방향 탐색
    for i in range(8):
				# if문을 깔끔하게 보기 위하여 dx dy 생성
        dx = max2[0]+dr[i]
        dy = max2[1]+dc[i]
				
				# dx dy가 배열 범위 안에 있다면
        if 0<= dx< N and 0<= dy < M:
						# dx dy 좌표 값이 지금 위치 높이보다 낮거나 같다면?
            if 0< arr[dx][dy] <= now :
								# 위치 이동
                peak(arr, (dx,dy))

# 8방향
dr = [-1,-1,-1,0,1,1,1,0]
dc = [-1,0,1,1,1,0,-1,-1]


N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

# 배열의 총합 
# -> for i in arr을 하면서 나온 i를 sum(i)하면 1차원 리스트가 되는데 그것을 sum 했다.
total_arr = sum(sum(i) for i in arr)
# 총합이 0이 될 때 까지 반복
while total_arr != 0:
		# 가장 큰 높이의 좌표 max1
    max1 = (0, 0)
    for i in range(N):
        for j in range(M):
            if arr[i][j] > arr[max1[0]][max1[1]]:
                max1 = (i, j)
		# max1좌표를 기준으로 봉우리를 탐색한다.
    peak(arr, max1)
		# 봉우리 +1
    ans += 1
		# 바뀐 배열의 총합을 구한다.
    total_arr = sum(sum(i) for i in arr)

print(ans)