class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        
        if left_height == -1 or right_height == -1:
            return -1  # Propagate failure
        if abs(left_height - right_height) > 1:
            return -1  # Tree is unbalanced
        return max(left_height, right_height) + 1
    
    return height(root) != -1

def test_is_balanced():
    # Test Case 1: Balanced tree
    balanced = TreeNode(1)
    balanced.left = TreeNode(2)
    balanced.right = TreeNode(3)
    balanced.left.left = TreeNode(4)
    balanced.left.right = TreeNode(5)
    assert is_balanced(balanced) == True, "Test Case 1 Failed"

    # Test Case 2: Empty tree (trivially balanced)
    empty_tree = None
    assert is_balanced(empty_tree) == True, "Test Case 2 Failed"

    # Test Case 3: Single node tree (trivially balanced)
    single_node = TreeNode(1)
    assert is_balanced(single_node) == True, "Test Case 3 Failed"

    # Test Case 4: Unbalanced tree - left-heavy
    unbalanced_left = TreeNode(1)
    unbalanced_left.left = TreeNode(2)
    unbalanced_left.left.left = TreeNode(3)
    unbalanced_left.left.left.left = TreeNode(4)
    assert is_balanced(unbalanced_left) == False, "Test Case 4 Failed"

    # Test Case 5: Just balanced on the edge case
    edge_balanced = TreeNode(1)
    edge_balanced.left = TreeNode(2)
    edge_balanced.right = TreeNode(3)
    edge_balanced.left.left = TreeNode(4)
    edge_balanced.left.right = TreeNode(5)
    edge_balanced.left.left.left = TreeNode(6)
    assert is_balanced(edge_balanced) == False, "Test Case 5 Failed"
    
    print("All test cases passed!")
test_is_balanced()
