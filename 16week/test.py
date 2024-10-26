def dfs(graph,start):
    stack = [start]
    visited = [False]*len(graph)
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in graph[node]:
                stack.append(neighbor)

from collections import deque
def bfs(graph,start):
    visited = [False]*len(graph)
    visited[start] = True
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    
