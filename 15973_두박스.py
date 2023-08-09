fx1, fy1, fx2, fy2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

if fx2 < bx1 or fx1 > bx2 or fy2 < by1 or fy1 > by2:
    ans = 'NULL'
elif fx1 == bx2 or fx2 == bx1:
    if fy1 == by2 or fy2 == by1:
        ans = 'POINT'
    else:
        ans = 'LINE'
elif fy1 == by2 or fy2 == by1:
    ans = 'LINE'
else:
    ans = 'FACE'

print(ans)