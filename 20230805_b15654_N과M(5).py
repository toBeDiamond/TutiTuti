''' 테스트 케이스
4 2
9 8 7 1
출력 결과
1 7
1 8
1 9
7 1
7 8
7 9
8 1
8 7
8 9
9 1
9 7
9 8
'''

import sys;

sys.stdin = open("./15654_N과M(5).py", encoding='utf-8')  # 코드가 들어있는 파일을 연다.
_ = input()  # 파일 첫줄이 ''' 이기 때문에 한줄 입력 받는다.


def n_to_m(nums, a):
    # 반환할 리스트 ans
    ans = []

    if a < m:  # 현재 길이가 목표 길이 보다 작으면

        for i in nums:  # 순열이 들어있는 nums를 순환

            for j in arr:  # 자연수가 들어있는 arr을 순환

                if j not in i:  # 순열 i에 자연수 j가 없다면

                    # i를 복사
                    tmp = i[:]

                    # tmp에 j를 넣어준다.
                    tmp.append(j)

                    # ans에 tmp를 넣어준다.
                    ans.append(tmp)

        # n_to_m() 함수에 값이 추가된 리스트 ans와 현재길이에+1를 하여 넣어준다.
        nums = n_to_m(ans, a + 1)
    # 길이가 k인 순열이 들어있는 리스트 nums를 반환
    return nums


n, m = map(int, input().split())  # 자연수의 수 N과 수열의 길이 M
arr = list(map(int, input().split()))  # 자연수를 입력 받는다.
arr.sort()  # 정렬 .. 나중에 머지정렬로 다시 구현하자.

for i in arr:  # 자연수 arr 순회
    first_num = [[i]]  # 길이가 1인 순열을 넣어준다.

    re_tmp = n_to_m(first_num, 1)  # 함수에 진행 리스트와 현재 길이를 인자로 넣어준다.

    for i in re_tmp:  # 길이가 k인 순열이 들어있는 re_tmp를 순환
        print(*i)  # 순열을 출력한다.