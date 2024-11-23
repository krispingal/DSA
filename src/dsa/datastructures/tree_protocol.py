"""Specifies Tree protocol"""

from typing import Protocol, List, Any


class TreeProtocol(Protocol):
    def get_children(self, node: Any) -> List[Any]:
        """Returns a list of children of a given node."""
        pass
