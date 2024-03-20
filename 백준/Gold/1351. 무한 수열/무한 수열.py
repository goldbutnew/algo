def solve(n, p, q):
    dp = {0: 1}  # dp[i]는 A[i]의 값을 나타냄

    def calculate_dp(i):
        if i in dp:
            return dp[i]
        dp[i] = calculate_dp(i // p) + calculate_dp(i // q)
        return dp[i]

    return calculate_dp(n)

n, p, q = map(int, input().split())
result = solve(n, p, q)
print(result)

