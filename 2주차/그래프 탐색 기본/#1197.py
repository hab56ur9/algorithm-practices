#1197.py
# 음수 가중치가 존재하므로 플로이드 워셜로 풀어야함 
# 다시 풀기
# gpt코드 복사
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def kruskal(graph, V):
    parent = [i for i in range(V)]
    rank = [0] * V
    mst_weight = 0
    edges = 0

    graph.sort(key=lambda x: x[2])  # 간선을 가중치 기준으로 정렬

    for edge in graph:
        u, v, weight = edge
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_weight += weight
            edges += 1
            if edges == V - 1:
                break

    return mst_weight

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph.append((u - 1, v - 1, w))  # 노드 번호를 0부터 시작하도록 맞춤

print(kruskal(graph, V))