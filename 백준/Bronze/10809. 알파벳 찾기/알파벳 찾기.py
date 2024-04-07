text = input()
check = "abcdefghijklmnopqrstuvwxyz"
ans = [0] * 26

for i in range(len(ans)):
    if check[i] in text:
        idx = text.index(check[i])
        ans[i] = idx
    else:
        ans[i] = -1

print(*ans)