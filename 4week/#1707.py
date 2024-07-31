#1707.py

def dfs():
    visited = [0]*(V+1)
    for i in range(1,V+1):
        stack = [(i,1)]
        while stack:
            pos,state = stack.pop()
            
            if visited[pos] == 0 :
                visited[pos] = state
                for neighbor in graph[pos]:
                    if neighbor == pos:
                        return 'NO'
                    elif visited[neighbor] == 0:
                        temp = 2 if state == 1 else 1
                        stack.append((neighbor,temp))
                    elif visited[neighbor] == state:
                        return 'NO'
    return 'YES' 

import sys
input = sys.stdin.readline
K = int(input())
for _ in range(K):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        v,w = map(int,input().split())
        graph[v].append(w)
        graph[w].append(v)
    print(dfs())