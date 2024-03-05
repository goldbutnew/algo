import heapq

def dijk(s, e, N, adj_l):
    vstd = [float('inf')] * (N+1)
    hq = [(0, s)]
    vstd[s] = 0
    while hq:
        val, idx = heapq.heappop(hq)
        if vstd[idx] < val:
            continue

        for v, i in adj_l[idx]:
            if vstd[i] > val+v:
                vstd[i] = val+v
                heapq.heappush(hq, (val+v, i))

    return vstd[e]

def find_shortest_path(N, edges, v1, v2):
    adj_l = [[] for _ in range(N+1)]

    for a, b, c in edges:
        adj_l[a].append((c, b))
        adj_l[b].append((c, a))

    onetwo = dijk(1, v1, N, adj_l) + dijk(v1, v2, N, adj_l) + dijk(v2, N, N, adj_l)
    twoone = dijk(1, v2, N, adj_l) + dijk(v2, v1, N, adj_l) + dijk(v1, N, N, adj_l)

    # >= 로 해야함
    if onetwo >= float('inf') and twoone >= float('inf'):
        return -1
    else:
        return min(onetwo, twoone)

# 입력 받기
N, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
v1, v2 = map(int, input().split())

# 결과 출력
res = find_shortest_path(N, edges, v1, v2)
print(res)
