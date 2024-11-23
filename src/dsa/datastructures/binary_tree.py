class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: BinaryTreeNode = left
        self.right: BinaryTreeNode = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def get_children(self, node: BinaryTreeNode) -> list[BinaryTreeNode]:
        return [child for child in (node.left, node.right) if child]

    def insert(self, val):
        raise NotImplementedError("Insert is not defined for a generic BinaryTree")

    def traverse_inorder(self, node: BinaryTreeNode = None):
        """Perform in-order traversal"""
        node = node or self.root
        if node:
            yield from self.traverse_inorder(node.left)
            yield node.val
            yield from self.traverse_inorder(node.right)
