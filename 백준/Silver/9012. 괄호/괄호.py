t = int(input())

for _ in range(t):
    vps_test = input()
    stack = []
    stack_bottom = []
    for ps in vps_test:
        if ps == "(":
            stack.append(ps)
        else:
            if stack:
                stack.pop()
            else:
                stack_bottom.append(ps)
    if stack or len(stack_bottom) != 0:
        print("NO")
    else:
        print("YES")