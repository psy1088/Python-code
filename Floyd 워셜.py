# Floyd 워셜 최단경로 알고리즘
INF = int(1e9)

n = int(input())  # 노드 개수
m = int(input())  # 간선 개수

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):  # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):  # 입력 받기
    a, b, c = map(int, input().split())
    graph[a][b] = c

# Floyd 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY")
        else:
            print(graph[a][b], end=' ')
    print()
