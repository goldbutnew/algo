# 8개의 이동 방향 정의: 상, 하, 좌, 우, 대각선 상하좌우
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def search(grid, word, x, y, dir, index):
    if index == len(word):
        return 1
    nx, ny = (x + dx[dir]) % n, (y + dy[dir]) % m
    if grid[nx][ny] != word[index]:
        return 0
    return search(grid, word, nx, ny, dir, index+1)

def find_word(grid, word):
    cnt = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] == word[0]: # 시작 문자와 일치할 때만 탐색 시작
                for dir in range(8): # 모든 방향에 대해 탐색
                    cnt += search(grid, word, x, y, dir, 1)
    return cnt

n, m, k = map(int, input().split())
grid = [input().strip() for _ in range(n)]
words = [input().strip() for _ in range(k)]

# 각 단어에 대해 탐색하여 결과 출력
for word in words:
    print(find_word(grid, word))

