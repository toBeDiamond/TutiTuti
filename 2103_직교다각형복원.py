import sys
sys.stdin = open(".\input\input_2103.txt", "r")

#
#
# input = sys.stdin.readline
#
# dot_point = [] # 점들을 담을 리스트
# result = 0
#
# T = int(input())
# x_list= [0] * T
# y_list= [0] * T
# y_list=dot_point[:]
# for T in range(T): # 점 개수 T를 받아 반복문 실행
#     dot_point.append(list(map(int,input().split()))) # 점의 좌표를 리스트에 추가한다.
#
#
# x_list=dot_point[:]
# y_list=dot_point[:]
#
# for i in range(len(dot_point)): #점 x좌표 기준 정렬
#     for j in range(len(dot_point) - i - 1):
#         if x_list[j][0] > x_list[j+1][0]:
#             x_list[j], x_list[j+1] = x_list[j+1], x_list[j]
#         if y_list[j][1] > y_list[j+1][1]:
#             y_list[j], y_list[j+1] = y_list[j+1], y_list[j]
#
# for i in range(0,T,2):
#     result += abs(x_list[i][1] - x_list[i+1][1]) + abs(y_list[i][0] - y_list[i + 1][0])
#
# print(result)

#
#
# import sys
# sys.stdin = open(".\input\input_2103.txt", "r")
#
#

T = int(input())
x_dict = {}
y_dict = {}
result = 0

for i in range(T):
    a, b = map(int ,input().split())
    if x_dict.get(a, -1) != -1:
        result += abs(x_dict.pop(a) - b)
    else:
        x_dict[a] = b

    if y_dict.get(b, -1) != -1:
        result += abs(y_dict.pop(b) - a)
    else:
        y_dict[b] = a

print(result)


