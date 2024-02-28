T = int(input())

for _ in range(T):
    quiz = input()
    ans = 0
    t = 0
    for q in quiz:
        if q == "O":
            t += 1
            ans += t
        elif q == "X":
            t = 0
    print(ans)