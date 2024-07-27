# #9249.py
# 
# import sys
# input = sys.stdin.readline
# A = input().strip()
# B = input().strip()

# DP = [[0]*(len(B)+1) for _ in range(len(A)+1)]
# max = 0
# x,y = 0,0
# for i in range(1,len(A)+1):
#     for j in range(1,len(B)+1):
#         if A[i-1] == B[j-1]:
#             DP[i][j] = DP[i-1][j-1]+1
#             if max < DP[i][j]:
#                 max = DP[i][j]
#                 x,y = i,j
# print(DP[x][y])
# for i in range(max,0,-1):
#     print(A[y-i-1],end='')

################################################
#
# 이 문제는 일반적인 2차원 LCS배열 방식으로는 메모리 초과가 발생함.
# max_length와 pos값만 유지할 수 있다면 부분해가 최적해와 같으므로  
# 배열을 하나씩 생성하는 greedy 방식이 유효함. 
#
################################################
#
# 이 문제는 N^2으로는 시간초과남.
import sys
A = input()
B = input()
prev = [0]*(len(B)+1)
current = [0]*(len(B)+1)

max = 0 # 최대 길이
pos = 0 # 최장 문자열 포인터
for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1] :
            current[j] = prev[j-1]+1
            if max < current[j]:
                max = current[j]
                pos = i
        else:
            current[j] = 0
    prev,current = current, prev
print(max)

if max > 0:
    # for i in range(max):
    #     print(A[pos-max+i],end='')
    print(A[pos-max:pos])
        
