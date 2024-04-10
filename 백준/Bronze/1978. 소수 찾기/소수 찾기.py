n = int(input())

arr = list(map(int, input().split()))

# print(arr)

cnt = 0

for i in range(n):
    for k in range(2, arr[i]):
        if arr[i] % k == 0:
            break
        if k == arr[i]-1 and arr[i] % k != 0:
            cnt += 1
    if arr[i] == 2:
        cnt += 1

print(cnt)
