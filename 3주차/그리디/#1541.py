#1541.py
# - 나오고 다음 - 까지 묶는다면 무조건 최소값을 가질 것. 땅땅 
# - 가 한번이라도 등장시 다음 부호들은 모두 -로 교체
import sys
input = sys.stdin.readline

S = input()
length = len(S)
data = [] 
cal = ['+']

prev = 0
pointer = 0 
while pointer < length: # 입력을 적절히 핸들링, 
    temp = S[pointer]
    if temp == '-' or temp == '+':
        data.append(int(S[prev:pointer]))
        prev = pointer+1
        cal.append(temp)
    pointer+=1
data.append(int(S[prev:pointer])) # 마지막 인덱스를 추가 

state = 0 # - 가 한개라도 존재시에 뒤에 부호를 전부 -로 교체
for i in range(len(cal)):
    if cal[i] == '-':
        state = 1
    elif state == 1:
        cal[i] = '-'

result =0
pointer = 0
while pointer < len(cal):
    if cal[pointer] == "+":
        result +=data[pointer]
    elif cal[pointer] == '-':
        result -= data[pointer]

    pointer+=1
print(result)

############################################################