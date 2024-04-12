import sys

def is_palindrome(start, end):
    return dp[start][end]

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

# dp[i][j]는 수열의 i번째부터 j번째까지가 팰린드롬인지 여부를 저장
dp = [[False] * (N+1) for _ in range(N+1)]

# 길이가 1인 부분 수열은 항상 팰린드롬
for i in range(1, N+1):
    dp[i][i] = True

# 길이가 2인 부분 수열이 팰린드롬인지 확인
for i in range(1, N):
    if sequence[i-1] == sequence[i]:
        dp[i][i+1] = True

# 길이가 3 이상인 부분 수열이 팰린드롬인지 확인
for length in range(3, N+1):
    for start in range(1, N-length+2):
        end = start + length - 1
        if sequence[start-1] == sequence[end-1] and dp[start+1][end-1]:
            dp[start][end] = True

# 각 질문에 대한 답 출력
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    if is_palindrome(S, E):
        print(1)
    else:
        print(0)

