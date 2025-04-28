from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

def test_level_order_traversal():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Test Case 1 - Normal tree:", level_order_traversal(root))
    
    empty_tree = None
    print("Test Case 2 - Empty tree:", level_order_traversal(empty_tree))
    
    single_node = TreeNode(1)
    print("Test Case 3 - Single node:", level_order_traversal(single_node))
    
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    print("Test Case 4 - Left-skewed tree:", level_order_traversal(left_skewed))
    
    right_skewed = TreeNode(1)
    right_skewed.right = TreeNode(2)
    right_skewed.right.right = TreeNode(3)
    right_skewed.right.right.right = TreeNode(4)
    print("Test Case 5 - Right-skewed tree:", level_order_traversal(right_skewed))

if __name__ == "__main__":
    test_level_order_traversal()
