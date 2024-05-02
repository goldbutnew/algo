paper = [[0] * 1001 for _ in range(1001)]

N = int(input())

for k in range(1, N+1):
    x1, y1, x2, y2 = list(map(int, input().split()))

    for i in range(x1, x1+x2):
        for j in range(y1, y1+y2):
            paper[i][j] = k

ans = [0] * (N+1)

for i in range(len(paper)):
    for j in range(len(paper)):
        for k in range(1, N+1):
            if paper[i][j] == k:
                ans[paper[i][j]] += 1

for i in range(1, N+1):
    print(ans[i])