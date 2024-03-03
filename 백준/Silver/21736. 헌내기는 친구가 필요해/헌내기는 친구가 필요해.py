from collections import deque

def bfs(start_i, start_j):
    queue = deque([(start_i, start_j)])
    visited[start_i][start_j] = True

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            ni, nj = x + dx[k], y + dy[k]

            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and info[ni][nj] != "X":
                queue.append((ni, nj))
                visited[ni][nj] = True

                if info[ni][nj] == "P":
                    global person
                    person += 1

n, m = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

info = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 시작점 찾기
start_i, start_j = 0, 0
for i in range(n):
    for j in range(m):
        if info[i][j] == "I":
            start_i, start_j = i, j

person = 0
bfs(start_i, start_j)

if person == 0:
    print("TT")
else:
    print(person)
