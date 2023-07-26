import sys
import re

sys.stdin = open(".\input\input_1013.txt", "r")

STAR_VEGA_ELECTRIC_WAVE = '(100+1+ | 01)+'

results = []

for _ in range(int(input())):
    sign = input()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(sign)
    if m:
        results.append("YES")
    else:
        results.append("NO")

for result in results:
    sys.stdout.write(str(result) + '\n')