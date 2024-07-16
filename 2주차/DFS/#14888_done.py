#14888.py
########################
#
# DONE
# 
##################

import sys
input = sys.stdin.readline
N = int(input()) # 2 <= N <= 11

data = [int(x) for x in input().split()]
calculer = list(map(int,input().split()))
# calculer[0]+=1
cal_sum = calculer[0]+calculer[1]+calculer[2]+calculer[3]
# 0: 덧셈  , 1: 뺄셈, 2:곱셈, 3: 나눗셈  
import copy
def dfs(cal,m_depth,data): ## cal: 연산자 개수 저장하는 배열 m_depth: 최대 깊이, data:계산할 숫자 저장할 배열 
    graph = [[0,1,2,3]]*4 # 자기 자신을 가르키는 노드또한 포함 
    result = []
    stack = [(cal,0,0,data[0])] # visited, pos , depth, val 
    while stack:
        temp = stack.pop()
        visited,pos,depth,val = temp 
        # print(temp)
        if depth == m_depth:
            result+=[val]
            continue 
        
        for n in graph[pos]:
            # if cal[n] - visited[n]: ## 계산을 실행 
            if visited[n]:
                temp_visited = copy.deepcopy(visited)
                temp_visited[n]-=1
                temp = calculate(val,data[depth+1],n) # 0번째 초기화를 포함하므로 m_depth는 N와 같아야함
                stack.append((temp_visited,n,depth+1,temp))
    return result

def calculate(left,right,calculer):
    if calculer == 0:
        return left+right
    elif calculer == 1:
        return left-right
    elif calculer == 2:
        return left*right
    elif calculer == 3:
        # left 음수일 때 예외 추가 
        if left<0:
            return -(-left//right)
        return left//right

data = dfs(calculer,cal_sum,data)
print(max(data))
print(min(data))
        