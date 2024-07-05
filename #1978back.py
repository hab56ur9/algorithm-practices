#1978back.py
# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.
num = int(input())
data = [int(x) for x in input().split(" ")]

def logic1(n):
    # 방법 1 -> 일반적으로 수 n에 대해 소수인지 알려면 1부터 n-1까지의 수로 모두 나눠보는 것이 일반적 .
    cnt = 0 
    for n in data: # 시간복잡도 N
        if n < 2 : # 1일경우 그냥 패스 
            continue
        temp = 0
        for i in range(2,n): 
            # 시간복잡도 N , 1과 자기 자신을 제외한 범위내 탐색 
            if n%i == 0:
                temp+=1
        if temp == 0:
            cnt +=1
    print(cnt)
    # 총 시간복잡도 N*N -> N^2 

# 어떤 소수도 제곱근보다 큰 수로 나눠지지 않는다는 규칙이 있다.
def logic2(n):
    cnt = 0 
    for n in data: 
    # 시간 복잡도 -> N  
        if n < 2 :
            continue
        temp = 0
        for i in range(2,int(n**(1/2)+1)): 
            if temp>1:
                break
            # 1과 자신의 제곱근 까지의 범위내 탐색 
            # 시간복잡도 -> log(n) 범위가 n 전체에서 1부터 제곱근까지의 범위로 변경되었기 때문.
            if n%i == 0 :
                temp+=1
        if temp == 0:
            cnt +=1
    print(cnt) 
# 총 시간 복잡도 N * log(N) -> Nlog(N)

# ++ 개선안 -> 단일 로직으로 처리하니 1일때의 예외와 약수를 구했을때 바로 반복문을 빠져나오는 예외등 불필요한 오버헤드 존재
# -> 함수로 개선 
def isPrime(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0 :
            return False
    return True
def logic0():
    cnt = 0
    for n in data :
        if isPrime(n):
            cnt+=1
    print(cnt)
#총 시간 복잡도 N * log(N) -> Nlog(N)

## log(N)은 현재 제곱근까지의 범위를 탐색한다. 아직도 많게는 절반가까이 탐색중 





## -> 에라토스테네스의 체 : 소수들의 배수를 이용한 판별,
#
#  논리 flow
#  
#  1. 데이터 중 max 값을 찾아 max값까지의 소수를 구하는 에라토스테네스 배열 생성 
#  2. 주어진 값을 배열 인덱스에 넣어 소수여부 반환 
#  

# num = int(input())
# data = [int(x) for x in input().split(" ")]
def logic1(n):
    max = 0
    for n in data : # 최댓값 검색 
        if max < n :
            max = n 
    Eratos = [True]*(max+1) #최댓값까지의 소수를 저장할 리스트
    Eratos[0] = False
    Eratos[1] = False
    root = int(max**(1/2)+1)
    for i in range(2,root):
        if Eratos[i] == True:
            for j in range(i+i,max+1,i):
                Eratos[j] = False
    cnt = 0 
    for n in data : # 에라토스 배열에서 소수여부 조회 
        if Eratos[n] :
            cnt+=1

    print(cnt)

## 파이선에 맞게 최적화 

# num = int(input())
# data = [int(x) for x in input().split(" ")]
def logic2(n):
    max_val = 0
    max_val = max(data)
    Eratos = [True]*(max_val+1) #최댓값까지의 소수를 저장할 리스트
    Eratos[0] = Eratos[1] = False

    root = int(max_val**0.5)+1
    for i in range(2,root):
        if Eratos[i]:
            for temp in range(i+i,max_val+1,i):
                Eratos[temp] = False

    print(sum(1 for n in data if Eratos[n]))

# 에라토스 테네스의 체 개선판 
# 1. 인덱스 맥스 범위 n의 제곱근
# 2. 2,3은 소수이고 이둘의 배수를 처리하면 대부분의 수가 처리된다. 
# 3. 2과정을 거치면 소수일 가능성이 높은 홀수와, 홀수의 제곱만 남게된다.
# 4. 따라서 홀수의 제곱으로 인덱싱 시에 성능 향상 비약적 일것
# 5. 10이내의 범위는 예측이 쉽고, 제곱수를 시작첨자로 잡아도 문제가 없다.

def logic3(n):
    Eratos = [True]*(n+1)
    Eratos[0]=Eratos[1]=False
    root = int(n**0.5)+1   
    for i in range(4,n+1,2): # 짝수는 모두 False처리 
        Eratos[i] = False
    for i in range(3,root,2): # 홀수만 검색 , 맥스범위가 루트 
        if Eratos[i]:
            for j in range(i*i,n+1,i): # 10이내의 범위는 소수판별이 쉬우므로 제곱부터 시작 
                Eratos[j] = False
    return Eratos

max_value = max(data)
Eratos = logic3(max_value)
cnt = 0 
for item in data :
    if Eratos[item] : 
        cnt+=1

