N = input()
if len(N) > 2 and N[0] == '0':
    if N[1] == 'x' :
        print(int(N,16))
    else:
        print(int(N,8))
else:
    print(int(N))