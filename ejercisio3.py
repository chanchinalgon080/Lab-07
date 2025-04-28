class TreeNode:
    """Basic node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def mirror_tree(node):
    """Mirror a binary tree by swapping left and right children recursively."""
    if node is None:
        return None

    # Swap left and right
    node.left, node.right = node.right, node.left

    # Recursively mirror left and right subtrees
    mirror_tree(node.left)
    mirror_tree(node.right)

    return node

def test_mirror_tree():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    mirror_tree(root)
    assert root.left.value == 3
    assert root.right.value == 2
    assert root.right.left.value == 5
    assert root.right.right.value == 4

    # Test Case 2: Empty tree
    empty_tree = None
    assert mirror_tree(empty_tree) is None

    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    mirrored_single = mirror_tree(single_node)
    assert mirrored_single.value == 1
    assert mirrored_single.left is None
    assert mirrored_single.right is None

    print("All mirror_tree tests passed! ✅")

# Run the tests
test_mirror_tree()
