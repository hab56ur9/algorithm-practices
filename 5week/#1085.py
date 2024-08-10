#1085.py
import sys
input = sys.stdin.readline
x,y,w,h = map(int,input().split())

up = h-y
down = y
left = x
right = w-x
print(min(up,down,left,right))