num = int(input())

cnt = 0 
def is_prime(n):
    global cnt 
    cnt+=2
    if n <= 1:
        cnt+=1
        return False
    for i in range(2, int(n**(1/2))+1):
        cnt+=2
        if n % i == 0:
            return False,cnt
    return True
print([2]+[x for x in range(3,num+1,2) if is_prime(x)] , '실행 횟수',cnt)

# 에라토스 테네스의 체 개선판 
# 1. 인덱스 맥스 범위 n의 제곱근
# 2. 2,3은 소수이고 이둘의 배수를 처리하면 대부분의 수가 처리된다. 
# 3. 2과정을 거치면 소수일 가능성이 높은 홀수와, 홀수의 제곱만 남게된다.
# 4. 따라서 홀수의 제곱으로 인덱싱 시에 성능 향상 비약적 일것
# 5. 10이내의 범위는 예측이 쉽고, 제곱수를 시작첨자로 잡아도 문제가 없다.

cnt = 0 
def logic3(n):
    global cnt
    cnt+=1
    Eratos = [True]*(n+1)
    Eratos[0]=Eratos[1]=False
    root = int(n**0.5)+1  
    for i in range(4,n+1,2): # 짝수는 모두 False처리 
        cnt+=1
        Eratos[i] = False
    for i in range(3,root,2): # 홀수만 검색 , 맥스범위가 루트 
        cnt+=2
        if Eratos[i]:
            for j in range(i*i,n+1,i): # 10이내의 범위는 소수판별이 쉬우므로 제곱부터 시작 
                cnt+=1
                Eratos[j] = False
    return Eratos
list = logic3(num)
print([2]+[x for x in range(3,num+1,2) if list[x]], '실행 횟수',cnt) # 홀수만 검색 


