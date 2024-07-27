#1890.py

def solve(x,y):
    if x >= N or y >= N :
        return 0
    if D[x][y]:
        return D[x][y]
    n = matrix[x][y]
    if n == 0:
        return 0
    D[x][y] = solve(x+n,y) + solve(x,y+n)
    return D[x][y]

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
D = [[0]*N for _ in range(N)]
D[N-1][N-1] = 1

print(solve(0,0))

