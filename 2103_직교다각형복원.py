import sys
sys.stdin = open(".\input\input_2103.txt", "r")




dot_point = [] # 점들을 담을 리스트
dot_point11 = [1,2,1,2]
for T in range(int(input())): # 점 개수 T를 받아 반복문 실행
    dot_point.append(list(map(int,input().split()))) # 점의 좌표를 리스트에 추가한다.
print(dot_point)
for i in range(len(dot_point)): #점 x좌표 기준 정렬
    for j in range(len(dot_point) - i - 1):
        if dot_point[j][0] > dot_point[j+1][0]:
            dot_point[j], dot_point[j+1] = dot_point[j+1], dot_point[j]

print(dot_point)

