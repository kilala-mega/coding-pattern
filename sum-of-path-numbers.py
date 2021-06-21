class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeSum(root: TreeNode) -> int:
    def search(node: TreeNode, current_sum) -> int:
        if not node:
            return 0
        current_sum = current_sum*10 + node.val
        if not node.left and not node.right:
            # it's a leaf node
            return current_sum
        return search(node.left, current_sum) + search(node.right, current_sum)
    return search(root, 0)

def test():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(treeSum(root))

test()
