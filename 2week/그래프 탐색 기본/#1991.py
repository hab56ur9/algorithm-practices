#1991.py
class Node: 
    def __init__(self,left,right):
        self.left = left
        self.right = right 
    
def preorder(node):
    if node=='.':
        return 
    print(node,end='')
    preorder(tree[node].left)
    preorder(tree[node].right)

def inorder(node):
    if node == '.':
        return 
    inorder(tree[node].left)
    print(node,end='')
    inorder(tree[node].right)

def postorder(node):
    if node == '.':
        return 
    postorder(tree[node].left)
    postorder(tree[node].right)
    print(node,end='')

import sys
input = sys.stdin.readline
N = int(input())
tree = {}
for _ in range(N):
    root, left, right = input().split()
    tree[root] = Node(left, right)
print(tree)
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()