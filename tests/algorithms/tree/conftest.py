import pytest

from dsa.datastructures.generalized_tree import TreeNode, GeneralizedTree


@pytest.fixture()
def sample_tree():
    """
    Creates a sample tree for testing.
    Tree structure:
          A
         / \
        B   C
       / \
      D   E
    """
    root = TreeNode("A", [TreeNode("B", [TreeNode("D"), TreeNode("E")]), TreeNode("C")])
    return GeneralizedTree(root)


# Fixture for an empty tree
@pytest.fixture
def empty_tree():
    """Creates an empty tree."""
    return GeneralizedTree(None)


# Fixture for a single-node tree
@pytest.fixture
def single_node_tree():
    """Creates a tree with only a single node."""
    root = TreeNode("A")
    return GeneralizedTree(root)
