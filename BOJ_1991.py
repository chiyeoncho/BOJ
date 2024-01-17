import sys
input = sys.stdin.readline
N = int(input())

def preorder_traversal(start): # 전위 순회
    if start not in tree:
        return
    print(tree[start],end = '')
    preorder_traversal(start * 2)
    preorder_traversal(start * 2 + 1)

def inorder_traversal(start): # 중위 순회
    if start not in tree:
        return
    inorder_traversal(start * 2)
    print(tree[start],end = '')
    inorder_traversal(start * 2 + 1)

def postorder_traversal(start): # 후위 순회
    if start not in tree:
        return
    postorder_traversal(start * 2)
    postorder_traversal(start * 2 + 1)
    print(tree[start],end = '')


tree = dict()
tree[1] = 'A'
dic = dict()
dic['A'] = 1

for _ in range(N):
    parent,left,right = input().rstrip().split()
    if left != '.':
        dic[left] = dic[parent] * 2
        tree[dic[left]] = left
    if right != '.':
        dic[right] = dic[parent] * 2 + 1
        tree[dic[right]] = right

start = 1
preorder_traversal(start)
print()
inorder_traversal(start)
print()
postorder_traversal(start)
