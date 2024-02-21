import sys
from collections import deque
from itertools import permutations

# 입력 받은 미로의 초기 상태 저장
maze = [[list(map(int, input().split(' '))) for _ in range(5)] for _ in range(5)]

# 회전된 블록의 상태 저장을 위한 3차원 배열 초기화
empty = [[[0] * 5 for _ in range(5)] for _ in range(5)]

# 최단 경로의 길이를 저장하는 변수 초기화
# sys.maxisize: 현재 시스템에서 표현 가능한 정수형의 최대값
ans = sys.maxsize

# 미로를 이동하는 6가지 방향에 대한 델타 설정
# 상하좌우앞뒤
dz = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dx = [1, -1, 0, 0, 0, 0]

# 판을 회전시키기
def rotate(empty):
    tmp = [[0] * 5 for _ in range(5)]
    for i in range(len(empty)):
        for j in range(len(empty[0])):
            tmp[j][4 - i] = empty[i][j]
    return tmp

# 최단 경로를 찾기 위한 bfs
def bfs(empty):
    global ans
    q = deque()
    # 각 위치에 도달하는데 걸린 이동 횟수를 저장하는 3차원 배열 초기화
    dist = [[[0, 0, 0, 0, 0] for _ in range(5)] for _ in range(5)]
    # 시작 위치를 큐에 추가
    q.append((0, 0, 0))

    while q:
        x, y, z = q.popleft()
        # 목표 위치에 도달한 경우
        if (x, y, z) == (4, 4, 4):
            # 현재까지의 최단 경로 업데이트
            ans = min(ans, dist[4][4][4])

            # 5x5x5 크기의 미로에서 갈 수 있는 가장 짧은 경로는 12
            # 최단 경로가 12인 경우 출력 후 종료
            if ans == 12:
                print(ans)
                exit()
            return

        # 6가지 방향에 대해 이동
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            # 범위를 벗어나거나 이미 방문한 위치인 경우 무시
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and empty[nx][ny][nz] != 0 and  dist[nx][ny][nz] == 0:
                q.append((nx, ny, nz))
                dist[nx][ny][nz] = dist[x][y][z] + 1
            else:
                continue

# 미로 탈출 체크하는 dfs
def dfs(d):
    global empty
    # 5개의 블록을 모두 처리한 경우
    if d == 5:
        # 목표 위치인 (4, 4, 4)에 블록이 존재하는 경우에만 bfs 호출
        if empty[4][4][4]:
            bfs(empty)
        return

    # 4번 회전하면서 블록을 배치
    for i in range(4):
        # 블록의 첫 번째 위치가 비어있는 경우에만 dfs 호출
        if empty[0][0][0]:
            dfs(d + 1)
        # 블록 회전
        empty[d] = rotate(empty[d])


# 가능한 모든 블록의 배치에 대해 최단 경로를 찾는 함수
def solve():
    # 가능한 블록의 배치 순열에 대해 반복
    for d in permutations([0, 1, 2, 3, 4]):
        for i in range(5):
            empty[d[i]] = maze[i]
        # 블록을 회전시키고 최단 경로를 찾는 dfs 호출
        dfs(0)

# 최단 경로를 찾기 위한 함수 호출
solve()

# 결과 출력
if ans == sys.maxsize:
    ans = -1

print(ans)