def find_kth_number(n, k):
    def count_less_equal(x):
        count = 0
        for i in range(1, n + 1):
            count += min(x // i, n)
        return count

    left, right = 1, n * n
    while left < right:
        mid = (left + right) // 2
        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left


n = int(input())
k = int(input())
ans = find_kth_number(n, k)

print(ans)
