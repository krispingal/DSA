""""Implements a generalized tree"""


class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children else []


class GeneralizedTree:
    def __init__(self, root=None):
        self.root = root

    def get_children(self, node: TreeNode):
        return node.children
