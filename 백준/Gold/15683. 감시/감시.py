# CCTV 타입 별로 가능한 방향 조합
cctv_directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 상하좌우 이동을 위한 배열
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 초기값 설정
ans = float("inf")
N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
cctv_locs = []  # CCTV의 위치 저장
cctv_cnt = 0  # CCTV 개수

# CCTV 위치 파악
for i in range(N):
    for j in range(M):
        if 1 <= room[i][j] <= 5:
            cctv_cnt += 1
            cctv_locs.append([i, j, room[i][j]])  # CCTV의 위치와 타입 저장

# 모든 CCTV의 위치와 가능한 방향 조합에 대해 확인
def dfs(curr_cnt):
    global cctv_cnt, ans
    blind_spot_cnt = 0  # 사각 지대 개수 카운트
    if curr_cnt == cctv_cnt:  # 모든 CCTV를 확인한 경우
        for i in range(N):
            for j in range(M):
                if room[i][j] == 0:  # 사각 지대인 경우 카운트
                    blind_spot_cnt += 1
        ans = min(ans, blind_spot_cnt)
        return
    cctv_x = cctv_locs[curr_cnt][0]  # CCTV의 x좌표
    cctv_y = cctv_locs[curr_cnt][1]  # CCTV의 y좌표
    cctv_type = cctv_locs[curr_cnt][2]  # CCTV의 타입
    for directions in cctv_directions[cctv_type]:  # 해당 CCTV 타입에 대해 가능한 모든 방향 조합 탐색
        reset = []  # 현재 상태를 원상복구하기 위한 좌표 리스트
        for direction in directions:  # 각 방향에 대해 탐색
            x = cctv_x
            y = cctv_y
            while True:
                x += dx[direction]
                y += dy[direction]
                if 0 <= x < N and 0 <= y < M and room[x][y] != 6:  # 벽이 아니고 공간 내에 있을 때
                    reset.append([x, y, room[x][y]])  # 원상복구를 위해 현재 상태 저장
                    room[x][y] = 7  # CCTV가 감시하는 영역으로 표시
                else:
                    break
        dfs(curr_cnt + 1)  # 다음 CCTV 위치 확인
        # 탐색 후에는 원래 상태로 복구하여 다음 탐색에 영향을 주지 않도록 함
        for x, y, type in reset:
            room[x][y] = type

# DFS 실행
dfs(0)
print(ans)
