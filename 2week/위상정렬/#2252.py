#2252-.py
def dfs(v,graph,visited,stack:list): # 여기
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor,graph,visited,stack)
    stack.append(v)

def topologi(graph):#dfs 사용하여 구현
    length = len(graph)
    visited = [False] * length  # visited 배열을 모든 dfs에 공유 사용하기위해 topologi배열에서 선언하는 것이중요
    stack = [] 
    # 얻을 자료 순서에 따라 queue or stack으로 구별 ex) 리프노드가 맨뒤로 -> 스택 , 리프노드가 맨앞으로 -> 큐 
    # 또한 dfs를 재귀방식, stack 방식을 사용하는 여부에 따라 순서가 또 바뀌니 주의.
    for node in range(1,length):
        if not visited[node]:
            dfs(node,graph,visited,stack)
    while stack:
        print(stack.pop(),end=' ')
    

####################################
# input 
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph=[[] for _ in range(N+1)] # 1 번째 인덱스부터 시작 
for _ in range(M):
    v,w = map(int,input().split())
    graph[v].append(w)
topologi(graph)
