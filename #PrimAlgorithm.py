#Prim'sAlgorithm.py
import heapq
def prim_lazy(graph, start=0):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, start)]  # (가중치, 정점)
    mst_cost = 0
    mst_edges = []
    cnt = 0 ## MST는 E = V-1를 만족함 
    while cnt < n-1: # MST의 Edge가 V-1개를 만족하면 종료 
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        # MST에 추가
        visited[u] = True
        mst_cost += weight
        mst_edges +=[u]
        cnt +=1 
        # 인접 노드를 모두 추가 
        for weight, v in graph[u]:
            heapq.heappush(min_heap, (weight, v))
    return mst_cost, mst_edges

# 그래프의 인접 리스트 표현 (가중치, 정점) 쌍
graph = [
    [(1, 1), (4, 2), (3, 3)],
    [(1, 0), (2, 2), (3, 3)],
    [(4, 0), (2, 1), (5, 3)],
    [(3, 0), (3, 1), (5, 2)]
]

mst_cost, mst_edges = prim_lazy(graph)
print("Total cost of MST:", mst_cost)
print("Edges in MST:", mst_edges)

######################################################
import heapq
def prim_eager(graph, start=0):
    n = len(graph)
    visited = [False] * n
    min_edge = [(float('inf'), v) for v in range(n)]  # (최소 가중치, 정점)
    min_edge[start] = (0, start)
    min_heap = [(0, start)]  # (가중치, 정점)
    mst_cost = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += weight

        for next_weight, v in graph[u]:
            if not visited[v] and next_weight < min_edge[v][0]:
                min_edge[v] = (next_weight, v)
                heapq.heappush(min_heap, (next_weight, v))
                mst_edges.append((u, v, next_weight))

    return mst_cost, mst_edges

# 그래프의 인접 리스트 표현 (가중치, 정점) 쌍
graph = [
    [(1, 1), (4, 2), (3, 3)],
    [(1, 0), (2, 2), (3, 3)],
    [(4, 0), (2, 1), (5, 3)],
    [(3, 0), (3, 1), (5, 2)]
]

mst_cost, mst_edges = prim_eager(graph)
print("Total cost of MST:", mst_cost)
print("Edges in MST:", mst_edges)