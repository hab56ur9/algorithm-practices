#2637.py

#############################################
# 단순 dfs는 시간초과 

def topologi_v1(graph,N): # failure
    cnt = [0]*(N+1)
    stack = [(1,N)]
    while stack:
        # print(stack)
        weight,node = stack.pop()
        # 단방향 노드이고 다른 경로에서도 방문하기 떄문에 visited가 필요 없다.
        for c_weight,c_node in graph[node]:
            temp = weight * c_weight
            cnt[c_node]+=temp
            stack.append((temp,c_node))
    for i in range(1,N+1): # 1부터 N까지 출력 
        if not graph[i]:
            print(f'{i} {cnt[i]}')
############################################
from collections import deque
def topologi(graph,in_degree,N):
    cnt = [0]*(N+1)
    cnt[N] = 1 # 완제품 초기값 
    queue = deque([N])

    while queue:
        node = queue.popleft()
        for weight, c_node in graph[node]:
            cnt[c_node]+=cnt[node]*weight
            in_degree[c_node]-=1
            if in_degree[c_node] == 0 :
                queue.append(c_node)

    for i in range(1,N+1): # 1부터 N까지 출력 
        if not graph[i]:
            print(f'{i} {cnt[i]}')
#############################################
#
# input 
import sys
input = sys.stdin.readline
N = int(input()) #  1부터 N-1까지는 기본부품이나 중간부품 N=완제품 번호
M = int(input()) #  M개의 줄 

### 위상 정렬 핵심 in-dgree
in_degree = [0]*(N+1)
#초기세팅
graph = [[] for _ in range(N+1)] # 0은 사용하지 않는 인덱스 0~N까지 범위설정
for _ in range(M):
    # x,y,z = 중간부품이나 완제품 x를 만드는데 중간부품 혹은 기본부품 y가 k개필요하다.
    x,y,z = map(int,input().split())
    graph[x].append((z,y)) # z는 가중치, y는 노드
    in_degree[y]+=1 # 진입 차수 기록 

#중간 부품을 고르는 로직이 필요  
# 일단 부품별 필요 개수를 모두 구한후에 그래프에 arc 없는 노드가 기본부품이므로 
topologi(graph,in_degree,N)    

