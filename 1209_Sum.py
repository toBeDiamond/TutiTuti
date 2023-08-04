import sys; sys.stdin=open('./input/input_1209.txt')

for _ in range(10):

    # TestCase Num
    t = int(input())

    arr = [list(map(int,input().split())) for _ in range(100)]

    # 가장 큰 합 max
    max = 0

    # 왼쪽에서 오른쪽으로 내려가는 대각선의 합
    tmp_lx = 0
    # 오른쪽에서 왼쪽으로 내려가는 대각선의 합
    tmp_rx = 0

    # 배열은 100 * 100 크기 row크기만큼 반복
    for i in range(100):
        # for문이 0~99까지 1씩 증가 > tmp_lx 인덱스에 i를 넣어준다.
        tmp_lx += arr[i][i]

        # tmp_rx는 col이 99부터 1씩 줄어드는 인덱스를 가지므로 99-i를 col로 사용한다.
        tmp_rx += arr[i][99 - i]

        # row의 합 tmp_row
        tmp_row = 0
        # col의 합 tmp_col
        tmp_col = 0

        # col 크기만큼 반복
        for j in range(100):
            #tmp_row 에  i, j 를 더해줌
            tmp_row += arr[i][j]

            #tmp_col에 j, i를 넣어줌
            tmp_col += arr[j][i]

        # 구한 값들을 max랑 비교
        if tmp_row > max:
            max = tmp_row
        if tmp_col > max:
            max = tmp_col
    if tmp_lx > max:
        max = tmp_lx
    if tmp_rx > max:
        max = tmp_rx

    print(f'#{t} {max}')