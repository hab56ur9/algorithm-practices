#1152.py
string = input()
cnt = 0
if string[0] != ' ':
    cnt +=1
for i in range(len(string)-1):
    if(string[i] == ' ' and string[i+1] != 0):
        cnt+=1

print(cnt)