"""Implements Depth First Search in a Tree"""

from typing import Callable, Any

from ...datastructures.tree_protocol import TreeProtocol


def dfs(tree: TreeProtocol, node: Any, visit: Callable[[Any], None]) -> None:
    """Performs a depth first search on a Tree recursively.
    Args:
        tree (TreeProtocol): The tree structure to traverse. Must implement the TreeProtocol.
        node (Any): The starting node for the DFS traversal.
        visit (Callable[[Any], None]): A function to apply to each node during traversal.

    Returns:
        None: This function does not return anything. The results depend on the behavior of `visit`.
    """
    if not node:
        return
    visit(node)
    for child in tree.get_children(node):
        dfs(tree, child, visit)
