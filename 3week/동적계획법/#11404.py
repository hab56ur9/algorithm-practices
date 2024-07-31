#11404.py
#floyd-warshall
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
distances = [[float('inf')]*(N+1) for _ in range(N+1) ] # 1부터 인덱스 사용
for i in range(1,N+1):
    distances[i][i]=0 
for _ in range(M):
    a,b,c = map(int,input().split())
    if distances[a][b]> c:
        distances[a][b] = c

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if distances[i][j] > distances[i][k]+distances[k][j]:
                distances[i][j] = distances[i][k]+distances[k][j]

for i in range(1,N+1):
    for j in range(1,N+1):
        if distances[i][j] == float('inf'):
            print(0,end=' ')
        else:
            print(distances[i][j],end=' ')
    print()