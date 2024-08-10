#2253.py
############################################################
# 메모이 제이션은 메모리 초과 ...
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10000)
# N,M = map(int,input().split())
# small_rocks = [False]*(N+1)
# dp = [[-1]*(N+1) for _ in range(N+1)]
# for i in range(M):
#     small_rocks[int(input())] = True

# def f(p,v):
#     if p == N:
#         print(p,v)
#         return 0
#     if p>N or v < 1 or small_rocks[p]:
#         return float('inf') 
   
#     if dp[p][v] != -1:
#         return dp[p][v]
#     dp[p][v] = 1 + min(f(p+v-1,v-1),f(p+v,v),f(p+v+1,v+1))
#     return dp[p][v]

# temp = f(2,1)  
# if temp == float('inf'):
#     print(-1)
# else:
#     print(temp+1)
############################################################

import sys
import heapq
input = sys.stdin.readline
N,M = map(int,input().split())
small_rocks = [False]*(N+1)
for i in range(M):
    small_rocks[int(input())] = True

pq = []
heapq.heappush(pq,(1,2,1)) # cnt , pos, vel
temp = True
while pq:
    cnt,p,v = heapq.heappop(pq)
    if p == N:
        print(cnt)
        temp = False
        break
    if p > N or v < 1:
        continue
    heapq.heappush(pq,(cnt+1,p+v-1,v-1))
    heapq.heappush(pq,(cnt+1,p+v,v))
    heapq.heappush(pq,(cnt+1,p+v+1,v+1))
if temp:
    print(-1)
