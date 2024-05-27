n, m = map(int, input().split())

soldiers = [list(input()) for _ in range(m)]

# 방문한 위치를 표시하기 위한 배열
visited = [[False] * n for _ in range(m)]

def dfs(x, y, team):
    # 범위를 벗어나면 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    # 이미 방문한 위치이거나 팀이 다르면 종료
    if visited[y][x] or soldiers[y][x] != team:
        return 0
    # 현재 위치 방문 표시
    visited[y][x] = True
    count = 1
    # 상하좌우 방향에 대해 재귀적으로 탐색
    count += dfs(x+1, y, team)
    count += dfs(x-1, y, team)
    count += dfs(x, y+1, team)
    count += dfs(x, y-1, team)
    return count

# 흰색 병사의 위력 계산
white_power = 0
for i in range(n):
    for j in range(m):
        if soldiers[j][i] == 'W' and not visited[j][i]:
            white_power += dfs(i, j, 'W') ** 2

# 적국 병사의 위력 계산
black_power = 0
visited = [[False] * n for _ in range(m)]  # 방문 배열 초기화
for i in range(n):
    for j in range(m):
        if soldiers[j][i] == 'B' and not visited[j][i]:
            black_power += dfs(i, j, 'B') ** 2

print(white_power, black_power)
