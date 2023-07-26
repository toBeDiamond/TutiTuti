import sys
sys.stdin = open(".\input\input_1011.txt", "r")

for T in range(int(input())):
    x, y = map(int, input().split()) # 0 <= x < y < 2^31
    distance = (y - x)
    sqrt = round(distance ** 0.5)

    if (distance - sqrt ** 2) > 0:
        print(2 * sqrt)
        continue
    print(2 * sqrt - 1)

