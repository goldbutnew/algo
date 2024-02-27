import heapq

n = int(input())
m = int(input())

# 1번 노드부터 시작하므로 하나 더 추가
info = [[] for _ in range(n+1)]

visited = [False] * (n+1)
expense = [float('inf')] * (n+1)

# 출발점의 도시 번호 / 도착점의 도시 번호 / 버스 비용
for _ in range(m):
    u, v, w = map(int, input().split())
    info[u].append((v, w))

# 출발 도시 / 도착 도시
start, end = map(int, input().split())

# 최소 비용 찾기
def dijkstra(start):
    heap = [(0, start)]
    expense[start] = 0  # 시작 노드 초기화

    while heap:
        cost, now = heapq.heappop(heap)

        if visited[now]:
            continue

        visited[now] = True

        for next_node, next_cost in info[now]:
            if expense[next_node] > cost + next_cost:
                expense[next_node] = cost + next_cost
                heapq.heappush(heap, (expense[next_node], next_node))

# 다익스트라 알고리즘 수행
dijkstra(start)
ans = expense[end]

print(ans)
