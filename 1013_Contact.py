
import re
import sys
sys.stdin = open(".\input\input_1013.txt", "r")

results = []

for _ in range(int(input())):
    sign = input()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(sign)
    if m: results.append("YES")
    else: results.append("NO")

for result in results:
    print(result)