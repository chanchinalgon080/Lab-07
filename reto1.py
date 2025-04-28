class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_height(root):
    
    if root is None:
        return -1
    
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return max(left_height, right_height) + 1

def test_tree_height():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print("Test Case 1 - Normal tree height:", tree_height(root))  
    
    empty_tree = None
    print("Test Case 2 - Empty tree height:", tree_height(empty_tree))  
    
    single_node = TreeNode(1)
    print("Test Case 3 - Single node tree height:", tree_height(single_node))  
    
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    print("Test Case 4 - Left-skewed tree height:", tree_height(left_skewed)) 
    
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    print("Test Case 5 - Perfect binary tree height:", tree_height(perfect))  

if __name__ == "__main__":
    test_tree_height()