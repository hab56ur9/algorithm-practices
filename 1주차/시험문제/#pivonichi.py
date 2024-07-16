#pivonichi.py

def fibonacci(num = None):
    if num <= 0 :
        return  0
    elif num == 1:
        return 1 
    else:
        return fibonacci(num-1)+fibonacci(num-2)

for i in range(10):
    print(fibonacci(i))
    
def fibonacci2(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

for i in range(10):
    print(fibonacci2(i))