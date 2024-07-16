#2805.py

# import sys
# input =sys.stdin.readline
# n ,  m = map(int,input().split())
# tree = [int(x) for x in input().split()]
# tree.sort(reverse=True)
# for saw in range(max(tree),0,-1):
#     temp = 0
#     cnt = 0
#     for i in tree:
#         if i > saw:
#             temp+=i
#             cnt +=1
#         else :
#             break
#     val = temp - cnt*saw
#     if val == m :
#         print(saw)
#         break
#     elif val > m:
#         print(-1)

# import sys
# input =sys.stdin.readline
# n ,  m = map(int,input().split())
# tree = [int(x) for x in input().split()]

# low = 0
# high = max(tree)
# pivot = (high+low)//2
# while low<=high :
#     temp = 0
#     for t in tree :
#         val =  t - pivot
#         if val < 0:
#             continue
#         temp+=val
#     next = (temp-m)//len(tree)
#     if next == 0 :
#         next = 1 
#     if temp > m :
#         pivot += next
#     elif temp < m :
#         pivot -= next 
#     else:
#         print(pivot)
#         break

import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
tree = list(map(int, input().split()))

# 이진 탐색을 위한 변수 초기화
low, high = 0, max(tree)

# 이진 탐색 수행
while low <= high:
    mid = (low + high) // 2
    total = 0
    
    # mid 높이로 잘랐을 때 얻는 나무 길이 계산
    for t in tree:
        if t > mid:
            total += t - mid
    
    # 필요한 길이와 비교하여 범위 조정
    if total < m:
        high = mid - 1
    else:
        low = mid + 1

# 정답 출력
print(high)
