import sys

sys.stdin = open(".\input\input_2103.txt", "r")


# 리스트를 정렬해주는 함수 merge_sort
def merge_sort(c_arr, index):  # 병합 정렬 리스트 c_arr과 기준 인덱스 index를 입력 받는다.

    # 리스트의 길이가 2 이하면 바로 반환 한다.
    if len(c_arr) < 2:
        return c_arr

    # 리스트의 중간 위치를 나타내는 mid
    mid = len(c_arr) // 2

    # mid를 기준으로 위, 아래로 나눠서 각자 다시 정렬 해준다.
    low_arr = merge_sort(c_arr[:mid], index)
    high_arr = merge_sort(c_arr[mid:], index)

    merged_arr = []  # 정렬된 low, high를 합병할 리스트

    l = h = 0  # low, high 리스트 인덱스

    # 인덱스가 각 배열의 길이 보다 작을 때 까지 반복
    while l < len(low_arr) and h < len(high_arr):
        # low의 값이 high보다 작다면
        if low_arr[l][index] < high_arr[h][index]:

            # low_arr[l]를 merged_arr에 먼저 넣는다.
            merged_arr.append(low_arr[l])

            # index l 1 증가
            l += 1

        # high가 low보다 작다면
        else:
            merged_arr.append(high_arr[h])
            h += 1

    ''' 넣고 남은 값들을 merged_arr 뒤에 더한다.
    [ 1, 2, 3, 6], [4, 5, 7, 8]  ->  [ ], [7, 8]
    while 후 남은 [7, 8]을 더해준다.
    '''
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr  # 정렬된 리스트를 반환


# 도형 변의 길이를 더해주는 함수 merge_count
def merge_count(list, index):  # 리스트와 기준 인덱스를 받는다.
    #길이의 합 length
    length = 0

    # 선은 점 2개가 필요 하기에 2씩 증가 한다.
    for i in range(0, len(list), 2):
        # 2 점의 차를 합 한다.
        length += abs(list[i + 1][index] - list[i][index])
    return length


T = int(input())  # 점의 수를 입력받음
dot_axis = []  # 점을 저장할 리스트
result = 0  # 변의 길이

for i in range(T):  # 점의 xy좌표를 받아 리스트로 저장 한다.
    xy = list(map(int, input().split()))
    dot_axis.append(xy)


# 이것을 생각 못해서 3시간 뻘짓을 했다!!
# 점들을  x좌표 기준으로 한번 정렬한다.
x_axis = merge_sort(dot_axis, 0)

# 점들을 y좌표 기준으로 다시 정렬한다.
x_axis = merge_sort(x_axis, 1)

# 위와 반대
y_axis = merge_sort(dot_axis, 1)
y_axis = merge_sort(y_axis, 0)

# 점 사이의 거리를 result에 더해준다.
result += merge_count(x_axis, 0)
result += merge_count(y_axis, 1)

print(result)