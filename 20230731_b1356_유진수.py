import sys

sys.stdin = open(".\input\input_1356.txt", "r")

def check(num):
    # 2글자 미만이면 False 반환
    if len(num) < 2:
        return False

    # 2글자 이상 for문을 이용하여 모든 나누는 자리를 확인한다.
    for i in range(1, len(num)):

        # 나눈 자리의 곱을 나타내는 함수 multiplication()
        sum_front = multiplication(num[:i])
        sum_back = multiplication(num[i:])

        # front와 back이 똑같다면
        if sum_front == sum_back:
            return True
    return False


def multiplication(nums):
    # 곱하기전에 m을 1로 초기화
    m = 1
    # (문자)숫자를 하나씩 순환 각 자릿수를 확인한다.
    for num in nums:
        # num을 int로 바꿔서 m에 곱해준다.
        m *= int(num)
    return m


# 숫자를 문자열로 입력받는다.
target = input()  # ex: '1236'

# check() 함수에 숫자(문자)를 넣어 앞뒤의 곱이 같은지 확인
if check(target):
    print('YES')
else:
    print('NO')