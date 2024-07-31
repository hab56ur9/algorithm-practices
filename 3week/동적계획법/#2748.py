#2748.py
# dp bottom up 
# -> use iterater 
N = int(input())
f = [0]*(N+2)
f[0] = 0
f[1] = 1
for i in range(2,N+1):
    f[i] = f[i-1]+f[i-2]
    print(f[i])
print(f[N])
