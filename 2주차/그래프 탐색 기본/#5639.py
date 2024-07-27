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
import sys
input = sys.stdin.read

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    new_node = Node(key)
    parent = None
    current = root

    while current:
        parent = current
        if key < current.val:
            current = current.left
        else:
            current = current.right

    if parent is None:
        return new_node
    elif key < parent.val:
        parent.left = new_node
    else:
        parent.right = new_node

    return root

def postorder_traversal(root):
    if root is None:
        return []

    stack = []
    postorder = []
    last_visited = None
    current = root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek_node = stack[-1]
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                postorder.append(peek_node.val)
                last_visited = stack.pop()

    return postorder

def solve():
    data = input().strip().split()
    preorder = list(map(int, data))

    root = None
    for key in preorder:
        root = insert(root, key)

    postorder = postorder_traversal(root)
    for value in postorder:
        print(value)

if __name__ == "__main__":
    solve()

