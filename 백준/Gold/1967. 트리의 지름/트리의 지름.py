from collections import defaultdict

def find_farthest_node(graph, start):
    visited = set()
    stack = [(start, 0)]
    farthest_node = start
    max_distance = 0

    while stack:
        node, distance = stack.pop()
        if distance > max_distance:
            max_distance = distance
            farthest_node = node
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                stack.append((neighbor, distance + weight))

    return farthest_node, max_distance

def tree_diameter(n, edges):
    # 그래프 생성
    graph = defaultdict(list)
    for parent, child, weight in edges:
        graph[parent].append((child, weight))
        graph[child].append((parent, weight))

    # 임의의 노드에서 가장 먼 노드를 찾기
    start_node, _ = find_farthest_node(graph, 1)

    # 그 노드에서 가장 먼 노드를 찾기
    end_node, diameter = find_farthest_node(graph, start_node)

    return diameter

n = int(input())

# 간선에 대한 정보
# 부모 노드 번호 / 자식 노드 / 간선의 가중치
edges = [list(map(int, input().split())) for _ in range(n-1)]

print(tree_diameter(n, edges))