### DFS
# graph = 그래프의 간선들을 저장한 리스트
# v = 시작 정점
# visited = 정점의 방문 여부를 저장한 리스트
def DFS(graph, v, visited):
    visited[v] = True
    print(v,end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)
            
            
            
### BFS            
from collections import deque    
        
def BFS(graph, start, visited):
    q = deque([start])
    visited[start] = True
    
    while q:
        v = q.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
