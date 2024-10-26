from itertools import permutations
n = int(input())
arr = list(map(int,input().split()))

max_val = 0
for perm in permutations(arr):
    cur_val = 0
    for i in range(n-1):
        cur_val += abs(perm[i]-perm[i+1])
    if cur_val > max_val:
        max_val = cur_val
print(max_val)