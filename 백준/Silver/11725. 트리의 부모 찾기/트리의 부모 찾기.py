n = int(input())

# 그래프 생성
tree = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 방문 체크
v = [0] * (n + 1)

def dfs(tree, root):
    stack = [root]
    while stack:
        top = stack.pop()
        for adj in tree[top]:
            # 방문한 적 없는 노드를 v에 부모로 저장
            if v[adj] == 0:
                v[adj] = top
                stack.append(adj)
    return v


# 트리의 루트는 언제나 1
dfs(tree, 1)

# 각 노드에 저장된 부모 노드 가져오기
for p in range(2, n + 1):
    print(v[p])  