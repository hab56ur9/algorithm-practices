#8958.py

N = int(input())
for _ in  range(N):
    quiz = input()
    point = 0
    bonus = 1
    for i in range(len(quiz)):
        if (quiz[i] == 'O'):
            point+=bonus
            bonus+=1
        else:
            bonus = 1
    print(point)
