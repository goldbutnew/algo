import heapq
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    chapter = int(sys.stdin.readline())
    size = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(size)
    min_cost = 0
    while True:
        try:
            a, b = heapq.heappop(size), heapq.heappop(size)
            min_cost += (a + b)
            heapq.heappush(size, (a+b))
        except IndexError:
            break
    print(min_cost)