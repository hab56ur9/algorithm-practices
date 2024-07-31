#9663back.py

# N-Queen
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 10 초	128 MB	119020	57264	37098	46.624%
# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.



##################################################
#
# 논리 1 
# 1. 각 행과 열에는 오직 한개의 퀸만 존재해야한다. 
# 2. 대각선또한 한개의 퀸만 존재해야한다 
# 3. 백트래킹 방식으로 
#
# 구현 1
# 1. 행은 배열의 인덱스로 구분하자. 
# 2. 열은 배열의 값으로 구분하자. 
# 3. 대각선의 위치는 공식을 이용하자 | X1-X2 |  = | Y1- Y2 | 
# 4. DFS 방식으로 구현하고, 불가능할시에 해당 가지를 제거하고 복귀하는 백트래킹 
#
#############
#
# keyword DFS, BackTraking
#
################

num = 10
pos = [0]* num
flag_a =[False]*num
flag_b = [False]*(num*2-1)
flag_c = [False]*(num*2-1)
def put():
    for j in range(num):
        # print(f'{pos[j]:2}',end="")
        for i in range(num):
            print('O'if pos[i]==j else "X", end="")
        print()
    print()
        
def set(i):
    for j in range(num):
        if( 
            not flag_a[j]
        and not flag_b[i+j]
        and not flag_c[i-j+7]
        ):
            pos[i] = j 
            if i == num-1 :
                put()
            else:
                flag_a[j]= flag_b[i+j] = flag_c[i-j+num-1]= True
                set(i+1)
                flag_a[j]=flag_b[i+j] = flag_c[i-j+num-1] = False
#set(0)

####################################################################################
#
# 백준 제출용
#
num = int(input())
pos = [0]* num
flag_a =[False]*num
flag_b = [False]*(num*2-1)
flag_c = [False]*(num*2-1)

cnt=0
def set(i):
    global cnt
    for j in range(num):
        if( 
            not flag_a[j]
        and not flag_b[i+j]
        and not flag_c[i-j+num-1]
        ):
            pos[i] = j 
            if i == num-1 :
                cnt+=1
            else:
                flag_a[j]= flag_b[i+j] = flag_c[i-j+num-1]= True
                set(i+1)
                flag_a[j]=flag_b[i+j] = flag_c[i-j+num-1] = False
set(0)
print(cnt)

#############################################################
#
# NQueen 계산이 엄청 오래걸린다.. 최적화 방법 생각해보기 
#
