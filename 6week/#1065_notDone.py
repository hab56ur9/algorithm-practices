#1065.py
N = int(input())
cnt = 0
for i in range(1,N+1):
    tmp = i
    
    a = tmp%10
    tmp = tmp//10
    b = tmp%10
        
print(cnt)