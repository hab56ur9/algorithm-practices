#2110.py
N,C = map(int,input().split())
arr =[]
for _ in range(N):
    arr.append(int(input()))
arr.sort()

start  = 1 # 최소거리
end = arr[-1] - arr[0] # 최대거리

while start <= end:
    mid = ( start+end ) // 2
    value = arr[0]
    cnt = 1

    for i in range(1, len(arr)):
        if arr[i] >= value + mid:
            cnt +=1 
            value = arr[i]
    
    if cnt >= C:
        result = mid
        start = mid +1
    else:
        end = mid - 1

print(result)