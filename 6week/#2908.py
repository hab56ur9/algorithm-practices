#2908.py
A,B = map(int,input().split())
r_A = 0
r_B = 0

while A > 0:
    r_A *= 10 
    r_A += A%10
    A = A//10
while B > 0:
    r_B *= 10 
    r_B += B%10
    B = B//10

if r_A > r_B :
    print(r_A)
else :
    print(r_B)