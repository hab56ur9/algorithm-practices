#2178.py

from collections import deque
def bfs(matrix, n, m):
    length = n*m
    visited = [[False]*m for _ in range(n)]
    queue = deque([(0,0,0)])
    visited[0][0] = True
    while queue:
        v,w,weight = queue.popleft()
        dirc = wasd(v,w)
        
        if v == n-1 and w == m-1:
            print(weight)
            return 
        for i,j in dirc:
            if i>=0 and i<n and j>=0 and j<m and matrix[i][j] == '1' :
                if not visited[i][j]:
                    visited[i][j] = True
                    queue.append((i,j,weight+1))

def wasd(i,j):
    return [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]
import sys    
input = sys.stdin.readline
N,M = map(int,input().split())
matrix = [ input().strip() for _ in range(N)]
bfs(matrix,N,M)