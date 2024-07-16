#11724.py
#

from collections import deque
def bfs(graph,start,visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)] # 1 부터 인덱싱
for _ in range(m):
    v,w = map(int,input().split()) 
    graph[v].append(w)
    graph[w].append(v)

visited = [False]*len(graph)
cnt=0
for i in range(1,len(visited)):
    if not visited[i]:
        bfs(graph,i,visited)
        cnt+=1
print(cnt)