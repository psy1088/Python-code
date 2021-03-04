# 위상정렬 Topology Sort
from collections import deque

def topology_sort():
    # 처음 시작시, 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        # now가 진입하는 노드의 진입차수 감소
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:  # 새롭게 진입차수가 0이 된 노드를 큐에 삽입
                q.append(i)


v, e = map(int, input().split())  # v = 노드 수, e = 간선 수
indegree = [0] * (v+1)  # 진입차수 리스트
graph = [[] for _ in range(v+1)]  # 간선 정보를 담는 그래프
result = []  # 수행 결과를 담을 리스트
q = deque()

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # a -> b 로 이동가능
    indegree[b] += 1  # b의 진입차수 1 증가

topology_sort()
for i in result:
    print(i, end=' ')
