#11279.py

import sys
import heapq

input = sys.stdin.read
data = input().split()

N = int(data[0])
commands = list(map(int, data[1:]))

max_heap = []
results = []

for command in commands:
    if command == 0:
        if max_heap:
            results.append(-heapq.heappop(max_heap))
        else:
            results.append(0)
    else:
        heapq.heappush(max_heap, -command)

print("\n".join(map(str, results)))

#############################################

import sys
import heapq
input = sys.stdin.readline
data = int(input())
commands = list(map(int,data[1:]))
max_heap = []
results=[]

for command in commands:
    if command ==0:
        if max_heap:
            results.append(-heapq.heappop(max_heap))
        else:
            results.append(0)
    else:
        heapq.heappush(max_heap,-command)
print('\n'.join(map(str,results)))
