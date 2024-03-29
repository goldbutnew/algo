h, w = map(int, input().split())
arr = list(map(int, input().split()))

max_block_idx = arr.index(max(arr))
cnt = 0

start = arr[0]
for i in range(1, max_block_idx):
    if arr[i] < start:
        cnt += (start-arr[i])
    elif arr[i] > start:
        start = arr[i]

start = arr[-1]
for i in range(w-2, max_block_idx, -1):
    if arr[i] < start:
        cnt += (start-arr[i])
    elif arr[i] > start:
        start = arr[i]

print(cnt)
