#21606.py

def dfs(graph,start):
    stack = [start]
    n = len(graph)
    visited  = [False]*n
    cnt=0
    while stack:
        # print(stack)
        v = stack.pop()
        if not visited[v]:
            visited[v]= True
            if pos[v-1] == "1" and v != start : # 중간에 실내를 만날시에 돌아가기 
                cnt+=1
                continue
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    return cnt

import sys
inpurt = sys.stdin.readline
N = int(input())
pos = input() # 1은 실내, 0은 실외
graph = [[] for _ in range(N+1)] # 0번 인덱스는 사용하지 않음
for _ in range(N-1):
    v,w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)
cnt = 0 
for i in range(1,N+1):
    if pos[i-1] == "1":
        cnt+=dfs(graph,i)
print(cnt)

