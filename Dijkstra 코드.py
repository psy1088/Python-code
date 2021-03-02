#########################
# 간단한 다익스트라 알고리즘 #
# 시간복잡도 :  O(V^2)    #
#########################
# import sys
#
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, m = map(int, input().split())  # n=노드 개수, m= 간선 개수
# start = int(input())
# graph = [[] for i in range(n + 1)]  # n+1까지 해서 1부터 시작하게끔해 숫자에 맞는 인덱스에 바로 접근할 수 있도록!
# visited = [False] * (n + 1)
# distance = [INF] * (n + 1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())  # a -> b 로 가는 비용이 c
#     graph[a].append((b, c))
#
#
# def get_smallest_node():  # 방문하지 않은 노드 중에서 최단 거리의 노드 번호 반환
#     min_value = INF
#     index = 0
#     for i in range(1, n+1):
#         # 방문하지 않은 최솟값이라면
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#
#     return index
#
#
# def dijkstra(start):
#     distance[start] = 0  # 시작 노드 초기화
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#
#     for i in range(n-1):  # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
#         now = get_smallest_node()  # 현재 최단거리가 가장 짧은 노드를 꺼내서, 방문 처리
#         visited[now] = True
#
#         for j in graph[now]:  # 현재 노드와 연결된 다른 노드 확인
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:  # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 갱신해줌
#                 distance[j[0]] = cost
#
#
# dijkstra(start)
# for i in range(1, n+1):  # 최단 거리 출력
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])


#########################
# 개선된 다익스트라 알고리즘 #
# 시간복잡도 :  O(ElogV)  #
#########################
# 우선순위 큐를 사용함으로써 기존이 다익스트라 코드에서 get_smallest_node함수와, visited 리스트가 필요없어짐!!!
import sys
import heapq

input = sys.stdin.readline()
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:  # 갱신할 필요가 없다면 무시~
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])














