class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_leaf_nodes(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)

# Función de pruebas
def test_count_leaves():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert count_leaf_nodes(root) == 3, "Test Case 1 Failed"

    # Test Case 2: Empty tree
    empty_tree = None
    assert count_leaf_nodes(empty_tree) == 0, "Test Case 2 Failed"

    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    assert count_leaf_nodes(single_node) == 1, "Test Case 3 Failed"

    # Test Case 4: No leaf nodes at first level
    no_leaves_at_first = TreeNode(1)
    no_leaves_at_first.left = TreeNode(2)
    no_leaves_at_first.right = TreeNode(3)
    assert count_leaf_nodes(no_leaves_at_first) == 2, "Test Case 4 Failed"

    # Test Case 5: All nodes are leaves except root
    all_leaves = TreeNode(1)
    all_leaves.left = TreeNode(2)
    all_leaves.right = TreeNode(3)
    all_leaves.left.left = TreeNode(4)
    all_leaves.left.right = TreeNode(5)
    all_leaves.right.left = TreeNode(6)
    all_leaves.right.right = TreeNode(7)
    assert count_leaf_nodes(all_leaves) == 4, "Test Case 5 Failed"

    print("All test cases passed!")
test_count_leaves()
    