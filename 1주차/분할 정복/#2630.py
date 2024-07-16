#2630.py after 
def solve(matrix, n):
    white = 0
    blue = 0
    def cut(x:int,y:int,size:int):
        nonlocal blue,white
        current = matrix[x][y]
        same = True
        for i in range(x,x+size):
            for j in range(y,y+size):
                if current != matrix[i][j]:
                    same = False
                    break
            if not same :
                break
        if same:
            if current==1:
                blue+=1
            else:
                white+=1
        else :
            _size = size//2 
            cut(x,y,_size) 
            cut(x,y+_size,_size)
            cut(x+_size,y,_size)
            cut(x+_size,y+_size,_size)
    cut(0,0,N)
    return white,blue    

import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
white , blue = solve(matrix,N)
print(white)
print(blue)