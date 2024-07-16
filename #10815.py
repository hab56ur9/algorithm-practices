#10815.py
import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
data.sort()

def bs(arr, n):
    pl = 0
    pr = len(arr)-1
    
    while pl <= pr:
        pc = (pl+pr)//2
        if arr[pc] == n :
            return 1
        elif arr[pc]>n:
            pr = pc -1
        else:
            pl = pc +1
    return 0
n = int(input())
print(" ".join([ str(bs(data,int(x))) for x in input().split()]))
