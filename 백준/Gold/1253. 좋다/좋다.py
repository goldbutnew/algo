import sys
input = sys.stdin.readline

n = int(input())
good = list(map(int, input().split()))
good.sort()

cnt = 0
for i in range(n):
    goal = good[i]
    start = 0
    end = len(good)-1
    while start < end:
        if good[start] + good[end] == goal:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                cnt += 1
                break
        elif good[start] + good[end] > goal:
            end -= 1
        elif good[start] + good[end] < goal:
            start += 1

print(cnt)
