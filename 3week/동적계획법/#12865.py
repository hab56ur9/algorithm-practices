#12865.py

def knapsack(values,weights,k,i=0,lookup=None):
    lookup = {} if lookup is None else lookup
    if (i,k) in lookup:
        return lookup[(i,k)]
    if k<0:
        return float('-inf')
    elif i == len(values):
        return 0
    else:
        lookup[(i,k)] = max(
            values[i]+knapsack(values,weights,k-weights[i],i+1,lookup),
            knapsack(values,weights,k,i+1,lookup)
        )
        print(lookup)
        return lookup[(i,k)]
    
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
values=[]
weights=[]
for i in range(N):
    w,v = map(int,input().split())
    weights.append(w)
    values.append(v)
print(knapsack(values,weights,M))