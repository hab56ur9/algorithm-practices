#10000이하의 소수를 모두 출력하는 코드 
#제곱근, eratos배열, 짝수제외, 시작점 제곱부터 
num = 10000
cnt = 0 
def logic3(n):
    global cnt
    cnt+=1
    eratos = [True]*(n+1)
    eratos[0]=eratos[1]=False
    root = int(n**0.5)+1  
    for i in range(4,n+1,2): # 짝수는 모두 False처리 
        cnt+=1
        eratos[i] = False
    for i in range(3,root,2): # 홀수만 검색 , 맥스범위가 루트 
        cnt+=2
        if eratos[i]:
            for j in range(i*i,n+1,i): # 10이내의 범위는 소수판별이 쉬우므로 제곱부터 시작 
                cnt+=1
                eratos[j] = False
    return eratos
list = logic3(num)
print([2]+[x for x in range(3,num+1,2) if list[x]], '실행 횟수',cnt) # 홀수만 검색 