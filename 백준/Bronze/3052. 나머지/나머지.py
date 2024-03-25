check = []

for _ in range(10):
    num = int(input())
    check.append(num % 42)

ans = set(check)
print(len(ans))