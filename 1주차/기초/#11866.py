#11866.py
from collections import deque
n, k = map(int,input().split())
data = [x for x in range(1,1+n)]
# data = [1,2,3,4,5,6,7]
deq = deque(data)
result = []
for i in range(n):
    for j in range(k-1):
        deq.append(deq.popleft())
    result.append(str(deq.popleft()))

print('<'+', '.join([f'{x}' for x in result])+">")