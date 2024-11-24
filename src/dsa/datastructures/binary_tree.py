from typing import Optional, Any


class BinaryTreeNode:
    """Represents a node in a binary tree.

    Each node contains a value and references to its left and right child nodes.

    Attributes:
        val (Any): The value stored in the node. Can be of any data type.
        left (Optional[BinaryTreeNode]): Reference to the left child node.
        right (Optional[BinaryTreeNode]): Reference to the right child node.
    """

    def __init__(
        self,
        val: Any = None,
        left: Optional["BinaryTreeNode"] = None,
        right: Optional["BinaryTreeNode"] = None,
    ):
        """Initializes a BinaryTreeNode.

        Args:
            val (Any, optional): The value to be stored in the node. Defaults to None.
            left (Optional[BinaryTreeNode], optional): The left child node. Defaults to None.
            right (Optional[BinaryTreeNode], optional): The right child node. Defaults to None.
        """
        self.val = val
        self.left: BinaryTreeNode = left
        self.right: BinaryTreeNode = right


class BinaryTree:
    """Represents a binary tree.

    This class provides the basic structure for a binary tree, including methods
    to retrieve children of a node and perform in-order traversal.

    Attributes:
        root (Optional[BinaryTreeNode]): The root node of the binary tree.
    """

    def __init__(self, root=None):
        """Initializes a BinaryTree.

        Args:
            root (Optional[BinaryTreeNode], optional): The root node of the tree. Defaults to None.
        """
        self.root = root

    def get_children(self, node: BinaryTreeNode) -> list[BinaryTreeNode]:
        """
        Retrieves the children of a given node.

        Args:
            node (BinaryTreeNode): The node whose children are to be retrieved.

        Returns:
            list[BinaryTreeNode]: A list containing the left and right children of the node (if they exist).
        """
        return [child for child in (node.left, node.right) if child]

    def insert(self, val):
        """
        Inserts a value into the binary tree.

        Caution:
            This method is not implemented for the generic BinaryTree class.
            Subclasses such as BinarySearchTree should provide specific implementations.

        Args:
            val (Any): The value to be inserted into the tree.

        Raises:
            NotImplementedError: Always, since this is a placeholder method.
        """
        raise NotImplementedError("Insert is not defined for a generic BinaryTree")

    def traverse_inorder(self, node: BinaryTreeNode = None):
        """Performs an in-order traversal of the tree.

        In-order traversal visits nodes in the following order:
        1. Left subtree
        2. Current node
        3. Right subtree

        Args:
            node (Optional[BinaryTreeNode], optional): The starting node for the traversal.
            Defaults to the root of the tree.

        Yields:
            Any: The value of each node in the tree during the traversal.

        Example:
            >>> tree = BinaryTree(BinaryTreeNode(1))
            >>> tree.root.left = BinaryTreeNode(2)
            >>> tree.root.right = BinaryTreeNode(3)
            >>> list(tree.traverse_inorder())
            [2, 1, 3]
        """
        node = node or self.root
        if node:
            yield from self.traverse_inorder(node.left)
            yield node.val
            yield from self.traverse_inorder(node.right)
