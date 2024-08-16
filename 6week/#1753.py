#1753.py
import sys
input = sys.stdin.readline
V,E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w,v)) # 가중치 w인 v목적지

import heapq
pq = [(0,K)] # start setting
distances = [float('inf')] * (V+1)
distances[K] = 0
while pq:
    cur_distance , node = heapq.heappop(pq)
    if distances[node] < cur_distance:
        continue
    for weight,neibor in graph[node]:
        distance = weight + cur_distance
        if distances[neibor] > distance:
            distances[neibor] = distance
            heapq.heappush(pq,(distance,neibor))

for i in range(1,V+1):
    if distances[i] == float('inf'):
        print('INF')
        continue
    print(distances[i])