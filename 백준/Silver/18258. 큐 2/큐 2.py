import sys
from collections import deque
n = int(input())
q = deque([])

for i in range(1, n+1):
    my_command = sys.stdin.readline().split()
    # print(my_command)

    if my_command[0] == "push":
        q.append(my_command[1])
        # print(q)

    elif my_command[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())

    elif my_command[0] == "size":
        print(len(q))

    elif my_command[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif my_command[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif my_command[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
