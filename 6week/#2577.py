#2577.py
A = int(input())
B = int(input())
C = int(input())
cnt = [0]*10

temp = A*B*C

while temp > 0 :
    n = temp % 10
    cnt[n] +=1
    temp = temp//10
for i in range(10):
    print(cnt[i])
