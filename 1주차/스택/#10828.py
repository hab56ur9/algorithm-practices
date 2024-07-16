import sys
input = sys.stdin.readline

head = -1 
def push(x):
    global head
    stack.append(x)
    head +=1

def pop():
    global head
    if head < 0 :
        print(-1)
    else:
        print(stack[head])
        stack.remove(stack[head])
        # print(stack)
        head-=1

def size():
    print(head+1)

def empty():
    print(1 if head > -1 else 0)

def top():
    if head < 0:
        print(-1)
    else:
        print(stack[head])

stack = []
n = int(input())
for _ in range(n):
    command = input().strip().split()
    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "top":
        top()

################################################################################################################

import sys
input = sys.stdin.readline

def push(x):
    stack.append(x)

def pop():
    if not stack:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    print(1 if not stack else 0)

def top():
    if not stack:
        print(-1)
    else:
        print(stack[-1])

stack = []
n = int(input())
for _ in range(n):
    command = input().strip().split()
    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "top":
        top()
