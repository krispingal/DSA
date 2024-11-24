import pytest

from dsa.algorithms.tree.dfs import dfs


@pytest.mark.parametrize(
    "tree_fixture, expected",
    [
        ("sample_tree", ["A", "B", "D", "E", "C"]),  # Full tree traversal
        ("empty_tree", []),  # Empty tree
        ("single_node_tree", ["A"]),  # Single-node tree
    ],
)
def test_dfs_order(tree_fixture, expected, request):
    """
    Test DFS traversal order using different trees.
    """
    tree = request.getfixturevalue(tree_fixture)
    visited = []
    dfs(tree, tree.root, lambda node: visited.append(node.val))
    assert visited == expected


# Test with a custom visit action
def test_dfs_custom_action(sample_tree):
    """
    Test DFS traversal with a custom action applied during visit.
    """
    tree = sample_tree
    result = []

    # Custom visit action to transform node values
    def visit_action(node):
        result.append(node.val.lower())

    dfs(tree, tree.root, visit_action)
    assert result == ["a", "b", "d", "e", "c"]
