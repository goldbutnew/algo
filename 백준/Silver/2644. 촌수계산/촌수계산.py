n = int(input())
a, b = map(int, input().split())
m = int(input())
relation = [list(map(int, input().split())) for _ in range(m)]

# 각 노드의 부모를 저장하는 리스트
parents = [0] * (n + 1)

for x, y in relation:
    parents[y] = x

# 방문한 노드를 체크하는 리스트
visited = [[0, 0] for _ in range(n + 1)]

def dfs(node, depth):
    # 이미 방문한 노드이면 무시
    if visited[node][0]:
        return -1
    # 목표 노드에 도달하면 깊이 반환
    if node == b:
        return depth
    visited[node][0] = 1
    # 부모 노드로 이동하여 재귀적으로 호출
    parent = parents[node]
    if parent:
        result = dfs(parent, depth + 1)
        if result != -1:
            return result
    # 자식 노드로 이동하여 재귀적으로 호출
    for x, y in relation:
        if x == node:
            result = dfs(y, depth + 1)
            if result != -1:
                return result
    return -1

print(dfs(a, 0))