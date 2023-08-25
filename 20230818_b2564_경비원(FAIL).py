c, r = map(int,input().split()) # 가로 세로 길이
N = int(input()) # 가게 개수


store_loc = []

# 1 북쪽, 2 남쪽, 3 서쪽, 4 동쪽에 / Left or Up
for t in range(N+1):
    # 식당 좌표
    ewsn, loc = map(int, input().split())
    # 가게의 좌표와 경비원의 위치를 받는다.
    store_loc.append((ewsn, loc))

# 경비원과 가게 사이의 거리의 총 합
ans = 0

# 경비원의 위치는 아까 받은 리스트의 맨 끝 값이다.
guard = store_loc[-1]

# 가게의 수 만큼 반복
for i in range(N):
		
		# 현재 가게와 경비원 사이의 거리
    tmp = 0

		# 가게 정보 가지고 오기
    store = store_loc[i]

		# 경비원의 위치가 (북) 또는 (남) 이라면
    if guard[0] == 1 or guard[0] == 2:

				# 가게가 (북) 또는 (남)에 위치 한다면
        if store[0] == 1 or store[0]==2:

						# 경비원과 가게가 같은 거리에 있지 않다면
            if store[0] != guard[0]:

								# 왼쪽으로 가는길이 오른쪽으로 가는 길보다 작다면
                if guard[1] + store[1] < c - guard[1] + c - store[1]:

										# 오른쪽으로 가는 길의 거리를 더해준다.
                    tmp += r + guard[1] + store[1]

								# 왼쪽으로 가는 길이 더 짧다면
                else:

										# 왼쪽으로 가는 길을 더해준다.
                    tmp += r + c - guard[1] + c - store[1]

						# 같은 거리에 위치한다면
            else:
								 
								#가게와 경비원의 위치를 뺀 값의 절대값을 더해준다.
                tmp += abs(guard[1] - store[1])

				# 가게의 위치가 (동) (서) 쪽 이라면
        else:
						# 가게가 (서)쪽에 위치한다면.
            if store[0] == 3:
								# 경비원아 북쪽이라면
                if guard[0] == 1:
										# (거리는 경비원과 경계 사이 거리) + (가게와 경계 사이 거리)
                    tmp += guard[1] + store[1]

								# 가게가 남쪽이라면
                else:
										# (경비원과 경계 사이의 거리) - (세로 길이 - 가게와 경계 사이의 거리)
                    tmp += guard[1] + r-store[1]

						# 가게가 (동)쪽에 위치한다면.
            else:
								# 경비원이 (북)쪽에 위치한다면
                if guard[0] == 1:

										# ( 가로 - 경계와 경비원 사이 거리) + (경계와 가게 사이의 거리)
                    tmp += c-guard[1] + store[1]

								# 경비원이 남쪽에 위치한다면
                else:
										
										# (가로 - 경계와 경비원 사이 거리) + (세로 - 경계와 가게 사이 거리)
                    tmp += c-guard[1] + r - store[1]

		# 경비원이 (동) (서) 에 위치 한다면.
    else: # guard = 3 or 4

				# 가게가 (북) (남) 쪽에 있다면.
        if store[0] == 1 or store[0] == 2:

						# 가게가 (북)쪽에 있을 때
            if store[0] == 1:

								# 경비원이 (서) 쪽 이라면
                if guard[0] == 3:
										# (경계와 경비원 사이 거리) + (가로 - 경계와 가게 사이 거리)
                    tmp += guard[1] + c-store[1]

								# 경비원이 (동) 쪽 이라면
                else:
										# (경계와 경비원 사이 거리) + (경계와 가게 사이 거리)
                    tmp += guard[1] + store[1]

						# 가게가 (남)쪽에 있을 때
            else: # store == 2

								# 경비원의 위치가 (서)쪽 이라면
                if guard[0] == 3:
										# (가로 - 경계와 경비원 사이 거리) + (경계와 가게 사이 거리)
                    tmp += r - guard[1] + store[1]

								# 경비원이 (동)쪽에 있다면
                else:
										# (가로 - 경계와 경비원 사이 거리) + (세로 - 경계와 가게 사이 거리)
                    tmp += r- guard[1] + c - store[1]

				# 가게가 (동) (서) 쪽 이라면
        else: # store = 3, 4
						# 가게와 경비원이 같은 거리에 있지 않다면
            if store[0] != guard[0]:
								# 왼쪽, 오른쪽 길 길이를 비교 왼쪽이 더 짧다면
                if guard[1] + store[1] < r - guard[1] + r - store[1]:
									
										# (가로길이) + (경계와 경비원 사이 거리) + (경계와 가게 사이 거리)
                    tmp += c + guard[1] + store[1]

								# 반대면 반대로 길이를 구해서 더해준다.
                else:
                    tmp += c + r - guard[1] + r - store[1]

						# 같은 거리에 있다면
            else:

								# 각 거리를 뺴주고 절대값을 한다.
                tmp += abs(guard[1] - store[1])
		# 구한 거리를 총 합에 더해준다.
    ans += tmp
# 총합 출력
print(ans)