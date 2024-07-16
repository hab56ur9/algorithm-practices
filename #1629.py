#1629.py
# 문제
# 자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

# 출력
# 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

# -> 나머지는 숫자마다 다를 뿐 반복된다. 나머지 값들을 저장 똑같은 나머지값이 출력될때까지.
# -> 이후 len(list)%k으로 해당 리스트를 나누어 적절한 나머지 출력 
import sys
input = sys.stdin.readline
n, k, p = map(int,input().split())
k = 10
data = [] 

mul = 1 
start = 0
if n < p :
    start = 1
for i in range(k):
    mul*=n
    temp = mul%p
    if data[start] == temp:
        break
    data.append(temp)
   