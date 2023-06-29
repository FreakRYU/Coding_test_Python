from collections import deque
import sys

# TreeNode 정의
class Node(object):
    def __init__(self, left = None, right = None, value = 0):
        self.value = value
        self.left = left
        self.right = right

# TreeNode의 객체를 참조하는 root 정의
class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.memo = {}

    # 3개씩 입력받아 트리를 구성함
    def input_to_tree(self, center, left, right):
        # (.)값은 None으로 처리
        left = left if left != '.' else None
        right = right if right != '.' else None
        if center in self.memo:
            self.memo[center].left = Node(value = left)
            self.memo[left] = self.memo[center].left
            self.memo[center].right = Node(value = right)
            self.memo[right] = self.memo[center].right
        
        else:
            self.root = cur_node = Node(value = center)
            cur_node.left = Node(value = left)
            cur_node.right = Node(value = right)
            self.memo[center] = cur_node
            self.memo[left] = cur_node.left
            self.memo[right] = cur_node.right

visited1 = []
visited2 = []
visited3 = []

# 전위 순회
def dfs_1(root):
    if root is None:
        return
    if root.value is not None:
        visited1.append(root.value)
    dfs_1(root.left)
    dfs_1(root.right)

# 중위 순회
def dfs_2(root):
    if root is None:
        return
    dfs_2(root.left)
    if root.value is not None:
        visited2.append(root.value)
    dfs_2(root.right)

# 후위 순회
def dfs_3(root):
    if root is None:
        return
    dfs_3(root.left)
    dfs_3(root.right)
    if root.value is not None:
        visited3.append(root.value)

# 예제 입력 받기
n = int(sys.stdin.readline())
bt = BinaryTree()
for _ in range(n):
    n, l, r = sys.stdin.readline().split()
    bt.input_to_tree(center = n, left = l, right = r)

# 출력하기
dfs_1(bt.root)
dfs_2(bt.root)
dfs_3(bt.root)

string1 = ''.join(visited1)
string2 = ''.join(visited2)
string3 = ''.join(visited3)

print(string1)
print(string2)
print(string3)