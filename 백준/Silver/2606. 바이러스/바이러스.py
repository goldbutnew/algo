v = int(input()) # 0~6
w = int(input())
matrix = [[] for i in range(v+1)]

visited = [False] * (v+1)

# 양방향 연결
for i in range(w):
    a, b = map(int, input().split())
    matrix[a] += [b]
    matrix[b] += [a]

def dfs(start_v):
    visited[start_v] = True
    for i in matrix[start_v]:
        if not visited[i]:
            dfs(i)

dfs(1)

ans = visited.count(True) - 1

print(ans)