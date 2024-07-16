#1300.py

import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
data= []
for i in range(1,n+1):
    for j in range(1,n+1):
        data.append(i*j)
data.sort()
print(data)
print(data[k])