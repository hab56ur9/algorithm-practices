#2294.py
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
weight = []
for _ in range(n):
    weight.append(int(input()))

weight.sort(reverse=True)
