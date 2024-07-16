#18352.py
import heapq
def dijkstra(graph, start):
    length = len(graph)
    distances = {node:float('inf') for node in range(length+1)}
    pq = [(0,start)]
    distances[start] = 0
    # cnt = -1
    # result = set()
    while pq :
        # print(pq)
        weight,node = heapq.heappop(pq)

        if weight > distances[node]:
            continue
        # if weight == K:
        #     result.add(node)
        #     cnt+=1
        for n_node in graph[node]:
            distance = weight + 1
            if distance < distances[n_node]:
                distances[n_node] = distance
                heapq.heappush(pq,(distance,n_node))
    
    
    # if cnt == -1 :
    #     print(-1)
    # else :
    # result = sorted(list(result))
    cnt = 0
    for x in distances:
        if distances[x] == K:
            print(x)
            cnt+=1
    if cnt==0:
        print(-1)
    # [print(x) for x in distances.values() if]
    return 

import sys
input = sys.stdin.readline
N, M, K, X = map(int,input().split())
graph=[[] for _ in range(N+1)] # 도시의 개수만큼 인접리스트 표현

for _ in range(M): # 도로의 개수 만큼 반복 
    v,w = map(int,input().split())
    graph[v].append(w)
dijkstra(graph,X)

