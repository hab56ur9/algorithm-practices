#9084.py
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int,input().split()))
    M = int(input())

    f = [0]*(M+1)
    f[0] = 1   
    for coin in coins:
        for j in range(coin,M+1):
            f[j] += f[j-coin]
    print(f[M])




