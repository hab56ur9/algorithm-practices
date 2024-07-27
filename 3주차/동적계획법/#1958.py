#1958.py
# LCS
# 추가문제
import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()
C = input().strip()

DP = [[0]*(len(B)+1) for _ in range(len(A)+1)]
max = 0
pos = 0
for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            DP[i][j] = DP[i-1][j-1] +1
            if max < DP[i][j]:
                max = DP[i][j]
                pos = i 
fstr = A[pos-max:pos]
DP = [[0]*(len(C)+1) for _ in range(len(fstr)+1)]
max = 0 
for i in range(1,len(fstr)+1):
    print() #todo 마저작성