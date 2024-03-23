N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

total = N*M

for w in range(N-2):
    for b in range(w+1, N-1):

        count = 0

        for ww in range(w+1):
            for k in range(M):
                if arr[ww][k] != 'W':
                    count += 1

        for bb in range(w+1, b+1):
            for m in range(M):
                if arr[bb][m] != 'B':
                    count += 1
        for rr in range(b+1, N):
            for m in range(M):
                if arr[rr][m] != 'R':
                    count += 1
        if total >= count:
            total = count

print(total)