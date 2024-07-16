#1182.py
# 백트래킹 
def count_subsequences_with_sum(nums, target_sum):
    def backtrack(index, current_sum):
        nonlocal count
        if index == len(nums):
            if current_sum == target_sum:
                count += 1
            return
        # 현재 원소를 포함하지 않는 경우
        backtrack(index + 1, current_sum)
        # 현재 원소를 포함하는 경우
        backtrack(index + 1, current_sum + nums[index])
    
    count = 0
    backtrack(0, 0)
    
    # 부분수열의 합이 target_sum인 경우
    # 공집합을 제외하고 세어야 한다.
    if target_sum == 0:
        count -= 1
    
    return count

# 입력 받기
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))

# 결과 출력
result = count_subsequences_with_sum(nums, s)
print(result)
