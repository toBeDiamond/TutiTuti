# 8방향
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

T = int(input())
for t in range(1, T + 1):

    # N = 배열의 한변 크기, M = 놓는 돌의 수
    N, M = map(int, input().split())

    # 오셀로 판 만들기
    arr = [[0] * N for _ in range(N)]

    # 가운데는 무족건 고정 1=흑돌, 2=백돌
    arr[N // 2 - 1][N // 2 - 1] = 2
    arr[N // 2 - 1][N // 2] = 1
    arr[N // 2][N // 2 - 1] = 1
    arr[N // 2][N // 2] = 2

    # 돌 놓는 수 만큼 반복
    for i in range(M):
        # 놓는 돌 위치 종류
        r, c, d = map(int, input().split())

        # 현재 위치에 돌을 놓는다.
        arr[r - 1][c - 1] = d

        # 8방향 탐색
        for j in range(8):

            # 이동 방향이 오셀로 판 안에 있는가?
            if 0 <= r - 1 + dx[j] < N and 0 <= c - 1 + dy[j] < N:

                # doll 변수에 넣는다
                doll = arr[r - 1 + dx[j]][c - 1 + dy[j]]

                # 돌색이 서로 다른가?
                if doll != d and doll != 0:

                    # 범위는 2부터 바로 윗줄에서 첫번 쨰 칸을 확인 했음
                    # m은 돌 놓았던 칸에서 몆칸 다른 모양을 카운트 했는지 알려주기도 한다.
                    m = 2

                    # 무한 반복 
                    while True:
                        # 다음에 있는 돌이 오셀로 판 안에 있는가?
                        if 0 <= r - 1 + dx[j] * m < N and 0 <= c - 1 + dy[j] * m < N:

                            # 돌2 = 다음 돌 
                            doll2 = arr[r - 1 + dx[j] * m][c - 1 + dy[j] * m]

                            # 다음 돌이 놓았던 돌과 다르다면
                            if doll2 != d and doll2 != 0:
                                # 앞 칸 보러 가야지
                                m += 1

                            # 돌이 같다면
                            elif doll2 == d:
                                # 뒤집으러 가야지
                                for k in range(1, m):
                                    arr[r - 1 + dx[j] * k][c - 1 + dy[j] * k] = d
                                break

                            # 돌이 빈 칸이라면 뒤집지 않는다.
                            elif doll2 == 0:
                                break

                        # 다음 위치의 돌이 오셀로 판에 없다면 break
                        else:  # ex > BWWW| 판이 끝나부렸다...
                            break

    # 카운트 하는 B, W 돌
    B = W = 0
    # 오셀로 판 순환
    for i in range(N):
        for j in range(N):
            # 돌이 1=흑돌이라면
            if arr[i][j] == 1:
                # 흑돌 개수 + 1
                B += 1
            # 백돌이라면
            # why elif : 오셀로판이 0일 가능성도 있으므로
            elif arr[i][j] == 2:
                # 백돌 개수 + 1
                W += 1

    # 흑돌, 백돌 출력
    print(f'#{t} {B} {W}')