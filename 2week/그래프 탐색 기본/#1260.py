#1260.py

def dfs(graph,start):
    visited = [False]*len(graph)
    stack=[start]
    result = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            result.append(v)
            visited[v] = True
            for neighbor in reversed(graph[v]):
                if not visited[neighbor]:
                    stack.append(neighbor)
    print(' '.join(map(str,result)))
    
from collections import deque
def bfs(graph,start):
    visited = [False]*len(graph)
    queue = deque([start])
    result = []
    visited[start] = True
    while queue:
        v=queue.popleft()
        result.append(v)
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    print(' '.join(map(str,result)))

import sys 
input = sys.stdin.readline
n,j,k = map(int,input().split())
data = []
graph = [[] for _ in range(n+1)]
for i in range(1,j+1):
    v,w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v) 
for neighbor in graph:
    neighbor.sort()

dfs(graph,k)
bfs(graph,k)




