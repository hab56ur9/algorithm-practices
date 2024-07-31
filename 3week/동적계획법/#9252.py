#9252.py
# LCS , Longest Common Subseqeance

import sys
input = sys.stdin.readline
A = input().strip() # 개행제거
B = input().strip() # 개행제거
DP = [[0]*(len(B)+1) for _ in range(len(A)+1)]

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            DP[i][j] = DP[i-1][j-1]+1
        else:
            DP[i][j] = max(DP[i-1][j],DP[i][j-1])

# print(DP)
print(DP[len(A)][len(B)])
result = []

def getText(row,col):
    if row == 0 or col == 0:
        return
    elif A[row-1]==B[col-1]:
        result.append(A[row-1])
        getText(row-1,col-1)
    else : 
        if DP[row-1][col] > DP[row][col-1]:
            getText(row-1,col)
        else:
            getText(row,col-1)

getText(len(A),len(B))
for i in range(len(result)-1,-1,-1):
    print(result[i],end='')