#3055.py
import heapq
def dijkstra(visited,distances,pq,end):
    n,k = end # unpack goal
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    while pq:
        # print(pq)
        weight,r,c,who = heapq.heappop(pq)
        if weight > distances[r][c]:
            continue
        if r==n and c == k and who == 1:
            return(weight//2)
        
        for dr,dc in directions:
            mr, mc = r+dr, c+dc
            if 0<=mr<R and 0<=mc<C : # 유효한 방향에만 탐색 
                if who == -1 and n==mr and k == mc: #물은 비버굴에는 못들어감 
                    continue

                temp = visited[mr][mc]
                if temp == 0: # 만약 아무도 방문하지 않은 길이라면 
                    visited[mr][mc] = who # 1 이면 고슴도치 -1 이면 물 
                    distance = weight+2
                    if distance < distances[mr][mc]: # 최소거리 업데이트 
                        distances[mr][mc] = distance
                        heapq.heappush(pq,(distance,mr,mc,who))

                elif temp == 1 and who == -1 : # 고슴도치가 이미 지나간 길일경우 
                    visited[mr][mc] = who
                    distances[mr][mc] = weight+2
                    heapq.heappush(pq,(weight+2,mr,mc,who))
    return 'KAKTUS'

################
# input
import sys
input = sys.stdin.readline
R,C = map(int,input().split())
mapData = [input().strip() for _ in range(R)]
visited = [[0] * C for _ in range(R)]
distances = [[float('inf')]*C for _ in range(R)]
pq =[]
for i in range(R):
    for j in range(C):
        temp = mapData[i][j]
        if temp =='D':
            end = (i,j) #아무것도 지나가지 않은 길은 0 그대로 
        elif temp == 'S':
            heapq.heappush(pq,(0,i,j,1))# 가중치 == 거리 0 부터 시작 
            # start = (0,i,j,1) # 가중치 == 거리 0 부터 시작 
            visited[i][j] = 1 # 고슴도치가 지나가는길은 1
            distances[i][j] = 0
        elif temp == '*':
            heapq.heappush(pq, (-1,i,j,-1))
            # water = (-1,i,j,-1) # 가중치가 -1부터 시작하여 우선순위큐에서 먼저 한사이클 실행
            visited[i][j] = -1 # 물이 지나가는 길은 -1 
            distances[i][j] = 0
        elif temp == 'X':
            visited[i][j] = 2
print(dijkstra(visited,distances,pq,end))