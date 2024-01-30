import sys
import heapq

n = int(input())

heap=[]

for _ in range(n):
    x = int(sys.stdin.readline())

    # x가 0이 아니라면 배열에 x라는 값 추가
    if x != 0:
        heapq.heappush(heap, (abs(x), x))

    # x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력
    elif x == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
