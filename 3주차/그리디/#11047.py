

import sys
input = sys.stdin.readline
N , K = map(int,input().split()) # 1<= N <= 10 , 1<=k <= 100,000,000
coins = []
for _ in range(N):
    coins.append(int(input()))

data = K
cnt = 0
for coin in sorted(coins,reverse= True):
    temp = data // coin 
    if temp == 0 :
        continue
    cnt += temp
    temp = temp*coin
    data = data % temp
    if data == 0:
        break
print(cnt)
    
