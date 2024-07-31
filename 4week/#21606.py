#21606
# 이전 주차에 못풀었던 문제들 다시 풀이
# 여전히 1자 트리 해결 못하고있음..
import sys
N = int(input())
isInside = [0]+list(map(int,input().strip()))
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    v,w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)


cnt = 0
for k in range(1,N+1):
    if isInside[k] != 1: # 시작점이 실내가 아닐 경우 continue
        continue
    visited = [False]*(N+1) # 여기서 시간초과 되었을 가능성 높음
    visited[k] = True
    stack = [] # 시작노드는 탐색하지 않고 바로 인접노드를 모두 넣어줌.
    for neighbor in graph[k]:
        stack.append(neighbor)
    
    while stack:
        node = stack.pop()
        visited[node] = True
        if isInside[node]: # 중간에 만나는 곳이 실내이면 cnt++이후 continue
            cnt+=1
            continue
        for neighbor in graph[node]:
            if not visited[neighbor]:
                stack.append(neighbor)
print(cnt)


            

