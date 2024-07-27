#2098.py

# def solve(s,e):
#     if s+1 == e  :
#         return M[s][e] if M[s][e] !=0 else 0 
#     result = 0
#     for i in range(N):
#         if M[s][i] != 0 :
#             for j in range(N):
#                 if M[j][e] != 0:
#                     result += M[s][i] + solve(i,j) + M[j][e]
#     print(result)
#     return result

import sys
input = sys.stdin.readline
N = int(input())
M = [list(map(int,input().split())) for _ in range(N)]

d = [[0]*(1<<16) for _ in range(N)]

def tsp(c,v):
    if v == (1<<N) -1 :
        return float('inf') if M[c][0] == 0 else M[c][0]
    if d[c][v]:
        return d[c][v]
    min_val = float('inf')

    for i in range(N):
        if v&(1<<i) == 0 and M[c][i] != 0:
            min_val = min(min_val,tsp(i,(v|(1<<i)))+M[c][i])
    d[c][v] = min_val
    return d[c][v]

print(tsp(0,1))