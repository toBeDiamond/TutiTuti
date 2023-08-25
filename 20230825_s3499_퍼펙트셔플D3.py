T = int(input())
for t in range(1, T+1):
    print(f'#{t}',end=' ')
    N = int(input())
    card_l = list(input().split())


    half = len(card_l) // 2 + len(card_l) % 2
    for i in range(half):
        print(card_l[i], end=' ')
        if i + half < N:
            print(card_l[i+half], end=' ')
    print()