H, M = map(int, input().split())

change_m = H * 60 + M - 45

if change_m < 0:
    change_m = 60 * 24 + change_m

ans_H = change_m // 60

ans_M = change_m % 60

print(f'{ans_H} {ans_M}')