K = int(input())

k_sum = [0]
for _ in range(K):
    k = int(input())
    if k == 0:
        k_sum.pop()
    else:
        k_sum.append(k)

ans = sum(k_sum)

print(ans)