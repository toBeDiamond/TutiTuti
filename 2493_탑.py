
# 타워의 개수
T = int(input())
 
# 타워 받기
list_n = list(map(int,input().split()))

# 타워 높이를 크기순으로 저장한 스택 tmp
tmp = []

# 타워 순환
for i in range(T):

		# 타워 높이가 저장되 있다면?
    while tmp:
				
				# 끝에 있는 타워를 빼준다.
        tv = tmp.pop()
				# 꺼낸 타워 높이가 더 크다면
        if arr[tv] > arr[i]:
						# tv와 현재 타워를 넣어준다.
            tmp.append(tv)
            tmp.append(i)
						# tv타워 위치를 출력해준다.
            print(tv+ 1, end=' ')
            break

		# 타워 높이가 저장 되있지 않다면
    if not tmp:
				# 왼쪽에 큰 타워가 존재하지 않는다는 것이니까 0 출력
        print(0, end=' ')
				# 나 자신을 tmp에 넣어준다.
        tmp.append(i)
