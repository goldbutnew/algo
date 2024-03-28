n = int(input())
ant_home = {}

# 트리 구조로 저장
for _ in range(n):
    t = list(input().split())
    k = int(t[0])
    path = t[1:]
    now_level = ant_home
    for food in path:
        # 현재 레벨에 해당 먹이가 없으면 새로운 딕셔너리를 추가
        if food not in now_level:
            now_level[food] = {}
        # 현재 레벨 해당 먹이가 위치하는 다음 레벨로 이동
        now_level = now_level[food]

# print(ant_home)

# 트리를 사전 순으로 출력
def print_ans(home, depth=0):
    for food in sorted(home.keys()):
        print("--" * depth + food)
        print_ans(home[food], depth + 1)

# 개미굴 출력
print_ans(ant_home)

