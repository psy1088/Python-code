# 서로소 집합 알고리즘
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


v, e = map(int, input().split())  # v= 노드개수, e= 간선개수
parent = [0] * (v+1)  # 노드의 개수만큼 부모테이블 초기화

# 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# cycle이 없을 시, union 연산 수행
cycle = False
for i in range(e):
    a, b = map(int, input().split())

    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

print(parent)

print("각 원소가 속한 집합: ", end='')
for i in range(v, 0, -1):
    print(find_parent(parent, i), end=' ')

print()

print("부모 테이블:", end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

if cycle:
    print("\n사이클 발생!!")
else:
    print("\n사이클 발생 안함!!")
