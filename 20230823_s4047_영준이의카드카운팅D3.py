T = int(input())
for t in range(1, T+1):
    card = input()
    flag = 1

    S = []
    D = []
    H = []
    C = []
    for i in range(len(card)//3):

        shape = card[i*3]
        num1 = card[i*3+1]
        num2 = card[i*3+2]
        num = int(num1+num2)

        if shape == 'S':
            tmp = S
        elif shape == 'D':
            tmp = D
        elif shape == 'H':
            tmp = H
        else:
            tmp = C
        if num in tmp:
            flag = 0
            break
        else:
            tmp.append(num)
    if flag:
        ans = str(13-len(S))+' '+str(13-len(D))+' '+str(13-len(H))+' '+str(13-len(C))

    else:
        ans = 'ERROR'
    print(f'#{t} {ans}')