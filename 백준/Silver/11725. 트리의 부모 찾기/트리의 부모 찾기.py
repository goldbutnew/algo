n = int(input())

# 그래프 생성
tree = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 방문 체크
visited = [0] * (n + 1)

def dfs(tree, root):
    stack = [root]
    while stack:
        top = stack.pop()
        for adj in tree[top]:
            if visited[adj] == 0:  # 방문한 적이 없다면
                visited[adj] = top  # 해당 노드를 부모 노드로 저장
                stack.append(adj)
    return visited


# 트리의 루트는 언제나 1
dfs(tree, 1)

for x in range(2, n + 1):
    print(visited[x])  # 각 인덱스(노드)에 저장된 부모 노드 가져오기