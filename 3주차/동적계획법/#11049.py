#11049.py


def solve(s,e):
    result = float('inf')
    if D[s][e] != -1:
        return D[s][e]
    elif s == e:
        return 0 
    elif s+1 == e:
        return M[s][0]*M[s][1]*M[e][1]
    for i in range(s,e):
        result = min(result,M[s][0]*M[i][1]*M[e][1] + solve(s,i) + solve(i+1,e))
    D[s][e] = result    
    return result

import sys
input = sys.stdin.readline

N = int(input())
D = [[-1]*(N+1) for _ in range(N+1)]
M = [['a','b']]
for _ in range(N):
    x,y = map(int,input().split())
    M.append([x,y])
print(solve(1,N))