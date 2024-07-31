#2579.py
def solve(pos,cnt):
    if pos > N: #계단이 최대범위 초과시에 무조건 작은값이 되도록 
        return 0
    # if D[pos]: #현재 값이 존재하면 반환 
    #     return D[pos]
    print(cnt)
    if cnt == 2:
        return stair[pos] + solve(pos+2,0)
    D[pos] = stair[pos] + max(solve(pos+2,cnt),solve(pos+1,cnt+1))
    return D[pos]

## input
N = int(input())
stair = [0]
for _ in range(N):
    stair.append(int(input()))
D = [0]*(N+1) # 0부터 인덱스 시작, 
print(solve(0,0))
