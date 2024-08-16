# 10000 보다 작은 자연수 주목 미리 배열은 선언해보자 
# 등장 횟수를 카운팅하자. 
cnt = [0]*10001
N = int(input())
for _ in range(1,N+1):
    cnt[int(input())]+=1
for i in range(1,10001):
    if cnt[i]:
        for _ in range(cnt[i]):
            print(i)