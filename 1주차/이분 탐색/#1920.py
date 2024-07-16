#1920.py
import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
data.sort()

def binary_search(arr, n):
    low = 0 
    high = len(data)-1
    while low <= high:
        mid = (low+high)//2
        if data[mid]==n:
            return 1
        if data[mid] < n:
            low = mid+1
        else:
            high = mid-1
    return 0

n = int(input())
find = list(map(int,input().split()))
for i in range(n):
    print(binary_search(data,find[i]))