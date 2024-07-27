#1946.py


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    data = []
    for _ in range(N):
        v,w = map(int,input().split())
        data.append((v,w))
    data.sort(key= lambda x : (x[0],x[1]))

    cnt = 1
    min_data = data[0][1]
    for x,y in data:
        if y < min_data:
            cnt+=1
            min_data =y
    print(cnt)