
import re
import sys
sys.stdin = open(".\input\input_1013.txt", "r")

STAR_VEGA_ELECTRIC_WAVE = '(100+1+ | 01)+'

a = [ '10', '0', '1' ] # '100+1+' 규칙은 10, 0+, 1+ 3개의 검증과정을 거쳐야한다.
b = '01'

for T in range(int(input())):
    rule_1001 = False # 100+1+ 규칙을 진행여부 표시

    success = True # 문자열이 규칙에 따르는지 표시

    pattern = input() # 입력받는 문자패턴 > 100110101 : True

    count = 0  # + 앞의 숫자 갯수를 카운트해주는 변수

    tmp = '' # 진행중인 문자 저장

    progress = 0 # 검증과정의 위치를 표시하는 progress

    for i in range(len(pattern)):
        tmp += pattern[i] #tmp에 현재 위치 문자 더하기

        if tmp == a[progress] or tmp == b : #tmp 가 현재 과정의 규칙과 일치??
            if tmp == b: # 01 과 일치
                tmp =''
                continue

            if progress == 0: # 과정이 0이라면 ? b:01은 걸러졌음
                progress += 1 # 다음 과정 진행
                tmp = ''
                rule_1001 = True  # 100+1+ 규칙진행중
                continue

            if a[progress] == tmp: # 과정의 값과 tmp가 일치하면 갯수 +1
                count += 1
                tmp = ''
                continue

        if rule_1001: # tmp가 규칙과 일치 안하고, rule1001 진행중 이면
            if count > 0: # 갯수가 1 이상인가?
                if progress == 1: # 과정 0+ 진행중
                    progress += 1
                    count = 1 # 이미 불일치 문자 1이 나왔기에 >> 1을 더해줌
                    tmp = ''
                    continue
                elif progress == 2: # 과정 1+ 진행중
                    progress -= 2 # 검증 과정을 처음으로 초기화
                    count = 0
                    rule_1001 = False # 100+1+ 검증과정 종료

                    # 문자열이 끝까지 갔거나. 다음 문자가 tmp랑 같을 때
                    # ex> 10011001 문제를 해결할려고 만든 조건문
                    # > 10011 001 로 인식하고 00은 규칙에 없어서 NO라고 출력됨
                    if i+1 == len(pattern) or pattern[i+1] == tmp:
                        if pattern[i-1] == pattern[i-2] :
                            progress += 1
                            tmp = ''
                            rule_1001 = True # 10은 이미 진행되었기에 100+1+규칙 진행중

            else: # 갯수가 0개라면
                success = False
                break
        if len(tmp) >= 2: # tmp가 2글자 이상이라면
            success = False
            break
    # 문자열이 규칙에 맞다면 and 과정이 중간에 끝나지 않았다면 > 10010 방지
    if success and len(tmp) == 0 and progress != 1 :
        print('YES')
    else :
        print('NO')