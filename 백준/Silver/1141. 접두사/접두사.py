n = int(input())
words = sorted([input() for _ in range(n)])

ans = 0

for i in range(n):
    current_word = words[i]
    is_prefix_x = False
    for j in range(i+1, n):
        if current_word == words[j][0:len(current_word)]:
            is_prefix_x = True
    if not is_prefix_x:
        ans += 1

print(ans)
