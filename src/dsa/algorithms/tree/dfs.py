"""Implements Depth First Search in a Tree"""

from typing import Callable, Any

from ...datastructures.tree_protocol import TreeProtocol


def dfs(tree: TreeProtocol, node: Any, visit: Callable[[Any], None]) -> None:
    """Performs a depth-first search (DFS) on a tree.

    Args:
        tree (TreeProtocol): The tree structure to traverse. Must implement
            the `TreeProtocol` interface, which provides the `get_children`
            method to retrieve child nodes.
        node (Any): The starting node for the DFS traversal.
        visit (Callable[[Any], None]): A function applied to each node during
            the traversal. The function takes a single argument (the node).

    Returns:
        None: This function does not return anything. The results depend on the behavior of `visit`.

    References:
        - `Depth-First Search on Wikipedia <https://en.wikipedia.org/wiki/Depth-first_search>`_

    Notes:
        - **Performance**:
            - Time Complexity: O(V + E), where `V` is the number of vertices
              (nodes) and `E` is the number of edges (connections).
            - Space Complexity: O(V) for the recursion stack.
        - If the tree contains cycles or invalid nodes, ensure appropriate
          safeguards to prevent infinite recursion.
    """
    if not node:
        return
    visit(node)
    for child in tree.get_children(node):
        dfs(tree, child, visit)
