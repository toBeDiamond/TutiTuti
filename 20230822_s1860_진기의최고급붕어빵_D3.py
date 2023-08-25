T = int(input())
for t in range(1, T+1):
    customer_n, cycle_time, lot = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    
    ans = 'Possible'
    for i in range(customer_n):
        # i+1 : 몆번째 손님 , 현재 붕어빵 생산량 = (시간//단위당 생산시간) * 단위당 생산량
        if i + 1 > ( arr[i] // cycle_time) * lot:
            ans = 'Impossible'
    
    print(f'#{t} {ans}')