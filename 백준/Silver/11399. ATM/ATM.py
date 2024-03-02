n = int(input())
arr = list(map(int, input().split()))

arr.sort()  # 그리디 알고리즘을 위해 입력 배열을 정렬

ans = 0
for i in range(n):
    ans += arr[i] * (n - i)

print(ans)
