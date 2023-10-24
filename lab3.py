import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_depth(root):
    if root.left is None:
        return 0

    queue = [(root.left, 1)]
    left_depth = 0

    while queue:
        node, depth = queue.pop(0)
        left_depth = max(left_depth, depth)
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return left_depth

def right_depth(root):
    if root.right is None:
        return 0

    queue = [(root.right, 1)]
    right_depth = 0

    while queue:
        node, depth = queue.pop(0)
        right_depth = max(right_depth, depth)
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return right_depth

def is_balanced():
    if abs(left_depth(root) - right_depth(root)) <= 1:
        return True
    else:
        return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
root.right.right.right.left = TreeNode(9)

print(is_balanced())
