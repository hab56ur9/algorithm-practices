#1931.py
#
# time out // bit 플래그는 입력이 조금더 적을때 사용하자.
#
# import heapq
# import sys
# input = sys.stdin.readline
# N = int(input()) # 1<= N <= 100,000
# meeting = []
# for _ in range(N):
#     s,e = map(int,input().split())
#     time = 0
#     for i in range(s,e):
#         time += (1<<i)
#     heapq.heappush(meeting,(e-s,time,s,e))

# reserved = (1<<32)
# cnt = 0
# while meeting:
#     weight,time,s,e = heapq.heappop(meeting)
#     if reserved & time == 0 :
#         reserved = reserved | time
#         cnt+=1
#     else:
#        continue
# print(cnt)

import sys
input = sys.stdin.readline
N = int(input())
A=[]
for _ in range(N):
    s,e = map(int,input().split())
    A.append((s,e))

A.sort(key = lambda x :(x[1],x[0]))
count =0
end_time =0
for start,end in A:
    if start>=end_time:
        end_time=end
        count+=1
print(count)

