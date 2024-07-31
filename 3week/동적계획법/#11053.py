#11053.py
#
# LCS
import sys
input = sys.stdin.readline
N = int(input())
data = list(map(int,input().split()))

prev = [0]*(N+1)
crnt = [0]*(N+1)
temp = sorted(list(set(data)))
max_data = 0
for i in range(N):
    for j in range(len(temp)):
        if data[i] == temp[j]:
            crnt[j+1] = prev[j]+1
            if max_data < crnt[j+1]:
                max_data = crnt[j+1]
        else:
            crnt[j+1] = max(prev[j+1], crnt[j])
    prev,crnt =crnt,[0]*(N+1)
print(max_data)
