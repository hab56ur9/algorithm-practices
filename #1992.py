#1992.py
def compress(x, y, size):
    # 현재 영역이 모두 같은 숫자인지 확인
    current = matrix[x][y]
    all_same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != current:
                all_same = False
                break
        if not all_same:
            break

    # 모두 같은 숫자라면 그 숫자를 출력
    if all_same:
        return current
    else:
        # 그렇지 않으면 4개의 부분으로 나누어 재귀 호출
        half_size = size // 2
        top_left = compress(x, y, half_size)
        top_right = compress(x, y + half_size, half_size)
        bottom_left = compress(x + half_size, y, half_size)
        bottom_right = compress(x + half_size, y + half_size, half_size)
        return f"({top_left}{top_right}{bottom_left}{bottom_right})"

# 입력 처리
N = int(input())
matrix = [input().strip() for _ in range(N)]

# 결과 출력
result = compress(0, 0, N)
print(result)