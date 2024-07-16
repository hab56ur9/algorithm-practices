#11725.py
#
# n-1개의 Edge를 가지므로 tree구조를 만족함. 

def dfs(graph,start):
    visited=[False]*len(graph)
    stack = [start]
    parents = [0]*len(graph)
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v]=True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    parents[neighbor] = v
                    stack.append(neighbor)
    for i in range(2,n+1):
        print(parents[i])
import sys
input = sys.stdin.readline
n = int(input()) # 2<= N <= 100,000
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    v,w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)
dfs(graph,1)
