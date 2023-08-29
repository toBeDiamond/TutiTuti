T = int(input())
for t in range(1,T+1):
    binary = list(input()) # 2진법 숫자
    trit = list(input()) # 3진법 숫자

    binary_arr = [] # 한 글자 다른 모든 2진법을 담아준다.
    trit_arr = [] # 한 글자 다른 모든 3진법을 담아준다.

    # 2진법 숫자 순환
    for i in range(len(binary)):
        tmp = binary[:] # 깊은복사
        # 0이라면 1로 바꿔준다
        if binary[i] == '0':
            tmp[i] = '1'
        # 1이라면 0으로 바꿔준다.
        else:
            tmp[i] = '0'
        # 2진법 리스트에 담아준다.
        binary_arr.append(''.join(tmp))

    # 3진법 숫자 변환
    for i in range(len(trit)):
        tmp = trit[:] # 깊은복사

        for _ in range(2): # 3진법이니까 숫자 2개씩 구해준다.

            # 자리수가 1일 떄, (1+1)%3 = 2 and (2+1)%3 = 0
            tmp[i] = str((int(tmp[i]) + 1 )% 3)
            trit_arr.append(''.join(tmp)) # 리스트에 담기

    ans=''
    for i in binary_arr: # 2진법 순환
        if not ans: # 출력값이 아직 못찾았으면
            for j in trit_arr: # 3진법 순환
                if int(i,2) == int(j, 3): # 2진법숫자 = 3진법숫자 일 때
                    ans = int(i, 2) # 출력값 넣어주기
                    break   # break
        else:   # 출력값을 찾았으면 break
            break

    print(f'#{t}', ans)