money = {
'50,000 원' : 50_000,
'10,000 원' : 10_000,
'5,000 원' : 5_000,
'1,000 원' : 1_000,
'500 원' : 500,
'100 원' : 100,
'50 원' : 50,
'10 원' : 10,
}

T = int(input())
for t in range(1, T+1):
    N = int(input())

    ans = []
    for i in money.keys():
        ans.append(N//money[i])
        N %= money[i]

    print(f'#{t}')
    print(*ans)