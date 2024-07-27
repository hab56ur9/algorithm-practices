#2253.py
# import sys
# input = sys.stdin.readline
# N,M = map(int,input().split())
# DP = [float('inf')]*(N+1)
# for _ in range(M):
    
#     DP[int(input())] = -1 #가지 못하는 곳은 inf로 예외처리 

# import heapq
# def solve2():
#     pq = [(2,1,1)] # 2번돌에 속도 1로 도착. 1회 점프
#     while pq:
#         print(pq)
#         pos,cnt,vel = heapq.heappop(pq)
#         if vel == 0:
#             continue
#         elif pos > N:
#             continue
#         elif DP[pos] == -1:
#             continue
#         elif cnt < DP[pos] :
#             DP[pos] = cnt    
#             heapq.heappush(pq,(pos+vel+1,cnt+1,vel+1))
#             heapq.heappush(pq,(pos+vel,cnt+1,vel))
#             heapq.heappush(pq,(pos+vel-1,cnt+1,vel-1))
        
#     return DP[N] if DP[N] != float('inf') else -1
# print(solve2())
# import sys
# input = sys.stdin.readline
# N,M = map(int,input().split())

# cant_visit = [0]*(N+1)
# for _ in range(M):
#     cant_visit[int(input())] = 1

# DP = [[float('inf')]*(N+1) for _ in range(N+1)]

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
stones = [False] * (n + 1)

for _ in range(m):
    stones[int(input())] = True

dp = [[float('inf')] * (int((2 * n) ** 0.5) + 2) for _ in range(n + 1)]
dp[1][0] = 0

for i in range(2, n + 1):
    if stones[i]:
        continue
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

result = min(dp[n])
if result == float('inf'):
    print(-1)
else:
    print(result)