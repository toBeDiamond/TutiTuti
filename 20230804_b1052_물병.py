'''
5
1000000 5
3 1
13 2
15 3
3 4

정답 :
15808
1
3
1
0
'''
import sys; sys.stdin=open('./1052_물병.py', encoding='utf-8')
_ = input()

T = int(input())
for t in range(1, T+1):
    N, K = map(int,input().split())
    buy = 0
    dept = 1
    while N > K:
        sum_bottle = N // 2
        rest_bottle = N % 2
        tmp = 0
        tmp_b = sum_bottle
        while tmp_b > 1:
            if tmp_b % 2:
                tmp_b - 1
                tmp += 1
                tmp_b //= 2
        if tmp_b + tmp + rest_bottle <= K:
            break
        if rest_bottle != 0:
            buy += 2**(dept) - 2**(dept-1)
            sum_bottle += 1
        N = sum_bottle
        dept += 1
    print(buy)