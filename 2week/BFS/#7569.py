#7569.py
#

#DONE

# 1인 노드를 모두 모은다음 우선순위큐로 한번에 탐색하는 방식 필요
#
############################################################
# from collections import deque
# def bfs(matrix,visited,start):
#     directions = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
#     i,j,k = start
#     visited[i][j][k] = True
#     queue = deque([(0,(i,j,k))])
#     max_weight = 0
#     while queue:
#         print(queue)
#         weight,pos = queue.popleft()
#         if weight > max_weight :
#             max_weight=weight
#         x,y,z = pos
#         for dx,dy,dz in directions:
#             mx,my,mz = x+dx,y+dy,z+dz
#             if 0<=mx<H and 0<=my<M and 0<=mz<N and not visited[mx][my][mz]:
#                 if matrix[mx][my][mz] =='0':
#                     visited[mx][my][mz] = True
#                     queue.append((weight+1,(mx,my,mz)))
#                     matrix[mx][my][mz]='1'
#     print(matrix,max_weight)
#     return visited

# # 1은 익은 토마토, 0은 익지 않은 토마토, -1은 빈공간 
# import sys
# import copy
# input = sys.stdin.readline
# N,M,H = map(int,input().split())
# matrix = [[input().split() for _ in range(M)] for _ in range(H)]

# visited = [[[False]*N]*M]*H
# for i in range(H):
#     for j in range(M):
#         for k in range(N):
#             if not visited[i][j][k] and matrix[i][j][k] == '1':
#                 visited = bfs(matrix,visited,(i,j,k))
                ## 익지않은 토마토 카운트 할 로직 필요 
############################################################

#
# dijk stra 에서 1인 노드를 모두 출발노드로 설정하여 풀이 
# 3차원 노드를 1차원으로 바꿔서 풀지말자.... 유효 노드 계산에만 한 세월이다.
# import heapq 
# def dijkstra(matrix,distances,start):
#     pq = start 
#     while pq:
#         weight,node = heapq.heappop(pq)
#         if weight > distances[node]:
#             continue
#         dirc = direction(node) # 유효한 방향만 받기 
#         for new_node in dirc:
#             if matrix[new_node] == '0': # 유효 방향이 안익은 토마토라면
#                 matrix[new_node] ='1' # 익은 토마토로 변경하고 
#                 distance = weight + 1 # 날짜를 하루 추가 
#                 if distance < distances[new_node]:
#                     distances[new_node] = distance
#                     heapq.heappush(pq,(distance,new_node))

#     # 모든 계산이 완료된후에도 0이 있으면 익지않는 토마토가 존재한다는 뜻.
#     for node in matrix:
#         if node =='0':
#             return -1
#     return max(distances)

# def direction(node):  # 상하좌우앞뒤 중 유효한 노드만 반환
#     delta = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]
#     wasd = []
#     x = node // (M * H)
#     y = (node % (M * H)) // H
#     z = node % H
#     for dz, dy, dx in delta:
#         nz, ny, nx = z + dz, y + dy, x + dx
#         if 0 <= nz < H and 0 <= ny < M and 0 <= nx < N:
#             new_node = nx * (M * H) + ny * H + nz
#             wasd.append(new_node)
#     print(f"Original node: ({z}, {y}, {x})")
#     print(f"Valid moves: {wasd}")
#     return wasd
 
# import sys
# input = sys.stdin.readline
# N,M,H = map(int,input().split())
# input = sys.stdin.read
# matrix = [int(x) for x in input().split() ]
# print(matrix)
# distances = [float('inf')]*N*M*H
# start=[]
# for node in matrix:
#     if node == '1':
#         distances[node] = 0 # 거리 배열 초기화 
#         start.append((0,node)) # 출발 노드 모두 더하기
#     elif node =='-1': #가로막힌 벽이면 weight 을 -1로 변경
#         distances[node] = 0


# print(dijkstra(matrix,distances,start))

import heapq 
def dijkstra(matrix,distances,start,cnt):
    direction = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
    
    pq = start 
    max_weight = 0 
    while pq:
        # print(pq)
        weight,node = heapq.heappop(pq)
        z,y,x = node
        if weight > distances[z][y][x]:
            continue
        if max_weight < weight:
            max_weight = weight
        for dz,dy,dx in direction:
            mz,my,mx = z+dz,y+dy,x+dx
            if 0<=mz<H and 0<=my<M and 0<=mx<N and matrix[mz][my][mx] == 0:
                cnt-=1
                matrix[mz][my][mx] ='1' # 익은 토마토로 변경하고 
                distance = weight + 1 # 날짜를 하루 추가 
                if distance < distances[mz][my][mx]:
                    distances[mz][my][mx] = distance
                    heapq.heappush(pq,(distance,(mz,my,mx)))
    # print(cnt)
    if cnt == 0: # 0이 모두 사라졌다면 
        return max_weight
    return -1 # 0이 남아있다면 

 
import sys
input = sys.stdin.readline
N,M,H = map(int,input().split())
matrix = [[[int(x) for x in input().split()] for _ in range(M)] for _ in range(H)]
distances = [[[float('inf')]*N for _ in range(M)] for _ in range(H)]
start=[]
cnt = 0
for z in range(H):
    for y in range(M):
        for x in range(N):
            temp = matrix[z][y][x]
            if  temp == 1:
                distances[z][y][x] = 0 
                start.append((0,(z,y,x)))
            elif temp == -1:
                distances[z][y][x] =-1
            elif temp == 0:
                cnt+=1
print(dijkstra(matrix,distances,start,cnt))
