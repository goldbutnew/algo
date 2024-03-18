n, m = map(int, input().split())

nolisten = set()  # 듣지 못한 사람의 목록을 set으로 변경

cnt = 0
name_lst = []

for _ in range(n):
    a = input()
    nolisten.add(a)

for _ in range(m):
    b = input()
    if b in nolisten:
        cnt += 1
        name_lst.append(b)

print(cnt)
for name in sorted(name_lst):
    print(name)
