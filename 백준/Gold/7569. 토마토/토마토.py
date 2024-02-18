from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque([])

def bfs():
    # q가 존재하는 동안
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and not box[nx][ny][nz]:
                box[nx][ny][nz] = box[x][y][z] + 1
                q.append([nx, ny, nz])

m, n, h = map(int, input().split())

# 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append([i, j, k])
bfs()

ans = 0

for i in box:
    for j in i:
        if 0 in j:
            print(-1)
            exit(0)
        ans = max(ans, max(j))

print(ans - 1)