#4344.py
import math
T = int(input())
for _ in range(T):
    data = list(map(int,input().split()))
    N = data[0]
    avg = (sum(data)-data[0])/N
    cnt = 0
    for i in range(1,len(data)):
        if data[i] <= avg:
            cnt+=1
    print(f"{round(((1-cnt/N)*100),3)}%")