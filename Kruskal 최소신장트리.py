# Kruskal 최소신장 트리 알고리즘
# 간선 입력 받기 -> 오름차순으로 정렬해 -> 간선 하나씩 확인하면서 싸이클이 있으면 패스하고, 싸이클 없으면 union
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)  # 부모테이블
edges = []  # 간선을 담을 테이블
result = 0

# 부모테이블에서 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 간선, 비용 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()  # cost 값에 대하여 오름차순 정렬

# 간선을 하나씩 확인
for cost, a, b in edges:
    # 부모가 같지 않으면 싸이클이 생기지 않으므로 union해줌
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
