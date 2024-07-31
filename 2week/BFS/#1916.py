#1916.py
#DONE
import heapq 
def dijkstra(graph,start):
    distances = [float('inf')]*len(graph)
    distances[start] = 0
    pq = [(0,start)]
    while pq:
        distance, v = heapq.heappop(pq)
        if distance > distances[v]:
            continue
        for weight,neighbor in graph[v]:
            c_distance = distance+weight
            if c_distance < distances[neighbor]:
                distances[neighbor] = c_distance
                heapq.heappush(pq,(c_distance,neighbor))
    return distances
##############################
# input 
import sys
input = sys.stdin.readline
N = int(input()) # 도시의 개수 
M = int(input()) # 버스의 개수
graph = [[] for _ in range(N+1)] # 0은 인덱스로 사용 x

for _ in range(M): # 인접리스트 생성 
    v,w,weight = map(int,input().split())
    graph[v].append((weight,w))
start , end = map(int,input().split())

result = dijkstra(graph,start)
print(result[end])
############################################################



