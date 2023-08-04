import sys
sys.stdin = open(".\input\input_1388.txt", "r")

# 세로 크기 n 과 가로 크기 m를 입력 받는다.
n, m = map(int, input().split())

# 타일 모양을 입력 받는다.
tile = [list(input()) for _ in range(n)]

# 반환값 return 0으로 초기화
result = 0

# 2중 for 문을 이용 하여 타일을 확인
for row in range(n):
    for col in range(m):
        # 현재 타일 위치를 now 지정
        now = tile[row][col]

        #  '-'  현재 타일이 전 타일이랑 같은지 비교한다.
        if now == '-':

            # (row 기준) 현재 타일이 전 타일이랑 다른지 확인한다.
            # col==0을 먼저 배치 하여 [col-1]이 [-1]인덱스로 인식되는 것을 막는다.
            if col == 0 or now != tile[row][col - 1 ] :
                # 타일이 다르다면 result에 1을 더 해준다.
                result += 1
        # '|' 타일 일 때 (col)을 기준으로 위와 똑같이 진행한다.
        else:
            if row == 0 or now != tile[row - 1 ][col] :
                result += 1

print(result)