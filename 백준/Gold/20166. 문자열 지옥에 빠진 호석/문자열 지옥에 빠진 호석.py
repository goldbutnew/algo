def search(grid, word, x, y, dx, dy, index):
    if index == len(word): # 단어의 끝에 도달했다면, 찾음
        return 1
    if x < 0 or x >= N: x %= N
    if y < 0 or y >= M: y %= M
    if grid[x][y] != word[index]: # 현재 위치의 문자가 일치하지 않는다면 실패
        return 0
    # 다음 문자로 이동
    return search(grid, word, x+dx, y+dy, dx, dy, index+1)

def find_word(grid, word):
    count = 0
    for x in range(N):
        for y in range(M):
            for dx in range(-1, 2): # -1, 0, 1
                for dy in range(-1, 2): # -1, 0, 1
                    if dx == 0 and dy == 0:
                        continue # 정지 상태는 제외
                    count += search(grid, word, x, y, dx, dy, 0)
    return count

# 입력 부분
N, M, K = map(int, input().split())
grid = [input().strip() for _ in range(N)]
words = [input().strip() for _ in range(K)]

# 각 단어에 대해 탐색하여 결과 출력
for word in words:
    print(find_word(grid, word))
