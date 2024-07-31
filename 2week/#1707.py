#1707.py

from collections import deque
def bfs(graph,start,visited,binary):
    visited[start] = True
    queue = deque([start])
   
    binary[start] = 0
    cnt = 0 
    while queue:
        v = queue.popleft()
        cnt = 1 if cnt == 0 else 0
        for neighbor in graph[v]:
            if binary[neighbor] == binary[v]:
                return 0 
            if not visited[neighbor]:
                binary[neighbor] = cnt
                visited[neighbor] = True
                queue.append(neighbor)
    return 1

import sys
input = sys.stdin.readline
K = int(input())
for _ in range(K):
    v,e =map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        v,w = map(int,input().split())
        graph[v].append(w)
        graph[w].append(v)
    n = len(graph)
    visited=[False]*n
    failed = False
    binary = [-1]*len(graph)
    for i in range(1,n):
        if not visited[i]:
            if bfs(graph,i,visited,binary) == 0:
                failed = True
                break
    if failed:
        print('NO')
    else :
        print("YES")

