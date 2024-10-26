#10819.py
# not solved

from itertools import permutations
n = int(input())
arr = list(map(int,input().split()))

max_value = 0
for perm in permutations(arr):
    cur_value = 0
    for i in range(n-1):
        cur_value += abs(perm[i]-perm[i+1])

    if cur_value > max_value :
        max_value = cur_value
print(max_value)
