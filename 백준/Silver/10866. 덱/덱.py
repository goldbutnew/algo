import sys
from collections import deque

N = int(input())

t_lst = []
deck = deque(t_lst)

for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    if "push_front" in cmd:
        deck.appendleft(cmd[11:])
    elif "push_back" in cmd:
        deck.append(cmd[10:])
    elif cmd == "pop_front":
        if len(deck) != 0:
            print(deck.popleft())
        else:
            print(-1)
    elif cmd == "pop_back":
        if len(deck) != 0:
            print(deck.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(deck))
    elif cmd == "empty":
        if len(deck) != 0:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if len(deck) != 0:
            print(deck[0])
        else:
            print(-1)
    elif cmd == "back":
        if len(deck) != 0:
            print(deck[-1])
        else:
            print(-1)