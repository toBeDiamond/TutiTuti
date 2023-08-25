from collections import deque


def bfs(start, target):
    # 선입 선출 하기 위해서 queue 만들고 본인 미리 넣어주기
    queue = deque([start])

    # visited를 깊은 복사 했다 원본 회손 방지
    visited_l = deque([visited[:]])

    # queue가 있으면 반복
    while queue:
        # 현재 시작 관계 수
        a = queue.popleft()
        # 현재 까지 방문했던 리스트 
        c = visited_l.popleft()
        # 방문 했던 관계 수 더하기
        b = sum(c)

        # 현재 관계와 연결된 관계가 있는지 확인
        for w in range(1, n + 1):
            # 관계가 연결되 있다면
            if adj[a][w] == 1 and c[w] == 0:
                # 그 관계가 목표인지 확인 맞으면 리턴
                if target == w:
                    return b
                else:
                    # 아니라면 queue에 넣어준다.
                    queue.append(w)
                    d = c[:]
                    d[w] = 1
                    visited_l.append(d)




# 사람 수와 관계의 수를 입력받는다.
n, r = map(int, input().split())

# 관계 배열을 만든다.
adj = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# 관계를 입력받아 넣는다. ( 양방향 )
for i in range(r):
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1

# 가장 케빈 베이컨 수가 적은 값
ans = 777
# 해당되는 사람 번호
man = 0

# 사람 수 만큼 반복
for i in range(1, n + 1):
    # 총 케빈 베이컨 합
    tmp = 0

    # 찾아야 하는 사람 반복
    for j in range(1, n + 1):
        # visited 함수
        visited = [0] * (n + 1)
        # 찾아야 하는 사람이 본인이 아니라면?
        if i != j:
            # 본인은 미리 체크하기
            visited[i] = 1

            # 그 사람과의 케빈베이컨 수 찾기
            find = bfs(i, j)
            # 총 합에 더 해주기
            tmp += find

        # tmp가 가장 케빈베이컨 합이 적다면 바꿔주기
    if ans > tmp:
        ans = tmp
        man = i
print(man)