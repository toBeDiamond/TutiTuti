import sys
sys.stdin = open(".\input\input_1024.txt", "r")

# 1부터 n 까지의 합을 구해주는 함수
def range_sum(n):
    if n <= 1:
        return 1
    # 재귀함수
    return n + range_sum(n-1)

# N은 합의 수 L은 최소 숫자의 수
N, L = map(int, input().split())

# L-1 까지 합을 더함
r_sum = range_sum(L-1)

# 결과를 True로 초기화
result = True

#result True일 때 까지 반복
while result:
    # L이 100을 넘거나 N에서 L-1까지 합이 음수라면
    if L > 100 or N-r_sum < 0:
        result = False
    # N에서 L-1합을 뺀 값이 L과 나누었을 때 나머지가 0이라면
    elif (( N - r_sum) % L) == 0:
        break
    L += 1
    r_sum = range_sum(L-1)

# result 값이 True라면
if result:
    #num 값을 구한다.
    num = (N-r_sum) // L
    for i in range(L):
        #num을 L개 까지 1씩 더하면서 출력한다.
        print(num + i, end=' ')
else:
    print(-1)