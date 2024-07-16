#5639.py
########################################
# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.left =None
#         self.right = None
    
# def makeTree(node:Node,key:int):
#     if node is None:
#         return Node(key)
#     else:
#         if node.key > key : 
#             node.left = makeTree(node.left,key)
#         else : 
#             node.right = makeTree(node.right,key)
#     return node

# def postOrder(node):
#     if node:
#         postOrder(node.left)
#         postOrder(node.right)
#         print(node.key)
# import sys
# # 전체 입력을 받아와서 줄 단위로 나눈다.
# input = sys.stdin.read
# sys.setrecursionlimit(10**6)
# data = list(map(int,input().split()))
# root = None
# for key in data :
#     root = makeTree(root,key)

# postOrder(root)
###################################
#
# 이 문제는 Recursion Error을 재귀로 푼다면 맞이할 것
# 스택으로 해결해야함

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
def insert(node:Node,key):
    if node is None:
        return Node(key)
    state = 0
    while node:
        if key == node.key:
            state = 1
            break
        elif key > node.key:
            if node.key is None:
                node.right = Node(key)
                break
            else:
                node = node.right
        else :
            if node.key is None:
                node.left = Node(key)
                break
            else :
                node = node.left 

import sys
input = sys.stdin.read
data = list(map(int,input().split()))
root = None
for key in data:
    root = insert(root,key)

