#1238.py 
# Done !!
# 내 풀이가 정답이다 그래프 방향을 바꿔서 다익스트라 두번
import sys
import heapq
input = sys.stdin.readline
N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
rv_graph = [[] for _ in range(N+1)]

def dijkstra(start, graph):
    D = [float('inf')]*(N+1)
    D[start] = 0
    pq = [(0,start)]
    while pq:
        cur_distance, node = heapq.heappop(pq)
        if cur_distance < D[node]:
            continue
        for neibor, weight in graph[node]:
            distance = weight+cur_distance
            if distance < D[neibor]:
                D[neibor] = distance
                heapq.heappush(pq,(distance,neibor))
    return D

for _ in range(M):
    s,e,t = map(int,input().split())
    graph[s].append((e,t))
    rv_graph[e].append((s,t))

# X로 출발하는 최단거리 
D1 = dijkstra(X,graph)
D2 = dijkstra(X,rv_graph)
max = 0
for i in range(1,N+1):
    temp = D1[i]+D2[i]
    if temp > max :
        max = temp
print(max)


