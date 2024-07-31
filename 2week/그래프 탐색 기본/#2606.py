#2606.py

from collections import deque
def bfs(graph,start):
    visited = [False]*len(graph)
    queue = deque([start])
    cnt = 0
    visited[start] = True
    while queue:
        v = queue.popleft()
        cnt+=1
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor]= True
                queue.append(neighbor)
    print(cnt-1)

import sys
input = sys.stdin.readline
cnt_vertice = int(input())
cnt_edge = int(input())
graph=[[] for _ in range(cnt_vertice+1)]
for _ in range(cnt_edge):
    v,w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)
bfs(graph,1)
    