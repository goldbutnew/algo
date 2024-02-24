N, K = map(int, input().split())

delete = []
idx = 0
ans = "<"

for i in range(1, N+1):
    delete.append(i)

ans = []

for t in range(N):
    idx += K-1
    if idx >= len(delete):  # 한바퀴를 돌면, 나머지부터 다시 시작
        idx = idx % len(delete)


    ans.append(str(delete.pop(idx)))
    real_ans = ", ".join(ans)

print(f"<{real_ans}>")
