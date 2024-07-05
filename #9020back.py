#9020back.py
#
# 골드바흐의 추측

# 문제
# 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

# 출력
# 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

# 제한
# 4 ≤ n ≤ 10,000
# 예제 입력 1 
# 3
# 8
# 10
# 16
# 예제 출력 1 
# 3 5
# 5 5
# 5 11



# 논리 1 
# 1. 주어진 수보다 작은 소수를 리스트에 오름차순으로 저장 
# 2. 리스트 앞과 뒤의 값을 순차적으로 비교 -->> 틀린 논리, 차이가 가장적은 값 출력이므로 가운데 부터 비교가 옳다 .
# -> 에라토스테네스 배열, 투포인터 

def logic1():
    num = int(input())
    Eratos = [True] * (num+1)
    Eratos[0] = Eratos[1] = False
    for i in range(2,int(num**0.5)+1):
        if Eratos[i]:
            for j in range(i+i,num+1,i):
                Eratos[j] = False
    list = [x for x in range(num+1) if Eratos[x]] # 1 번 
    front = 0
    rear = len(list)-1
    while front <= rear:
        if list[front]+list[rear] == num :
            print(list[front],list[rear])
            break
        elif list[front]+list[rear] > num : # 합이 주어진 수보다 클경우 rear를 앞으로 이동 
            rear-=1
        elif list[front]+list[rear] < num : # 합이 주어진 수보다 작은경우 front 뒤로 이동 
            front +=1

# --> 가장 차이가 큰 소수두개가 출력되므로 오답 , 로직 오류이므로 논리단계부터 다시 



########################################################################################

# 논리2
# 1. 주어진 수 범위의 소수들을 모두 구하여 오름차순 정렬하여 리스트에 저장 ( Eratos 배열 생성)
# 2. 주어진 수가 짝수임에 주목,반으로 나누어 가장 근접한 소수 2개를 찾는다.
# 3. 소수 두개의 합이 주어진수와 같으면 해결, 아닐시에 2번 부터 다시 

# 투포인터 
# 1. 가운데 기준으로 front,rear 같게 초기화
# 2. front 소수여부 확인
# 3. rear 소수여부 확인 
# 4. front == rear 확인 
# 4-1 front rear각각 다음 소수까지 이동 

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

cnt = int(input())
for i in range(cnt):
    num = int(input())
    front = rear = num//2                
    Eratos = logic3(num)
    while front > 1 and rear < num+1:
        state =0
        if Eratos[front]:
            state +=1
        else:
            front-=1
        if Eratos[rear]:
            state +=1
        else: 
            rear +=1

        if state == 2: ## 너무어렵게 풀었다, 어차피 합이 같아야 하니 둘이 동시에 움직이는것이 효과적일 것 
            sum = front + rear 
            if sum == num :
                print(front, rear)
                break
            elif sum < num:
                rear +=1
            elif sum > num :
                front -=1

########################################################################################
# 
#
# 위랑 같은 논리, but 합이 항상 같아야 한다는점을 이용, front와 rear를 동시에 움직인다.
#

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

cnt = int(input())
for i in range(cnt):
    num = int(input())
    Eratos = logic3(num)
    front = rear = num//2
    for _ in range(num//2):
        if Eratos[front] and Eratos[rear] :
            print(front,rear)
            break
        else :
            front -=1
            rear +=1



        


    
    
