year = int(input())
print(1 if year%4 == 0 and (year % 400 == 0 or year %100 != 0) else 0 )