#1956.py
# not DOne
import sys
input = sys.stdin.readline
V,E = map(int,input().split())
D = [[float('inf')]*(V+1)for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    D[a][b] = c

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            D[i][j] = min(D[i][j], D[i][k]+D[k][j])
for i in range(V):
    print(D[i])