a, b, v = map(int, input().split())

def find_day():
    if a >= v:
        return 1
    else:
        days = (v - b) / (a - b)
        return math.ceil(days)

import math
ans = find_day()

print(ans)
