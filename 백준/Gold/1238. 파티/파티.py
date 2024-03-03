import heapq

def longest_path(n, m, x, roads):
    graph = [[] for _ in range(n + 1)]

    for road in roads:
        start, end, time = road
        graph[start].append((end, time))

    def dijkstra(start):
        distances = [float('inf')] * (n + 1)
        distances[start] = 0
        heap = [(0, start)]

        while heap:
            current_distance, current_node = heapq.heappop(heap)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

    max_time = 0
    for i in range(1, n + 1):
        if i != x:
            home_to_x = dijkstra(i)[x]
            x_to_home = dijkstra(x)[i]
            total_time = home_to_x + x_to_home
            max_time = max(max_time, total_time)

    return max_time

# 입력 받기
n, m, x = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]

# 결과 출력
res = longest_path(n, m, x, roads)
print(res)
