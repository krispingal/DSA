"""Implementation of a skip list datastructure."""

import random

MAX_LEVEL = 16
PROBABILITY = 0.5


class SkipListNode:
    def __init__(self, value: int, level: int):
        self.value = value
        self.forward = [None] * (level + 1)


class SkipList:
    def __init__(self, max_level=MAX_LEVEL, probability=PROBABILITY):
        """SkipList constructor

        Parameters
        ----------
        max_level: maximum level the skiplist
        probability: Probability factor for the level decision.

        """
        self.head = SkipListNode(None, max_level)
        self.cur_level = 0
        self.max_level = max_level
        self.probability = probability

    def insert(self, val: int) -> None:
        """Inserts a value into the skip list."""
        update = [None] * (
            self.max_level + 1
        )  # Used to track all nodes whose next would be new val
        current = self.head

        # Traverse and mark each node which should be updated
        for level in range(self.cur_level, -1, -1):
            while current.forward[level] and current.forward[level].value < val:
                current = current.forward[level]
            update[level] = current

        # Assign a level to the new value
        new_level = self._random_level()

        if new_level > self.cur_level:
            for i in range(self.cur_level + 1, new_level + 1):
                update[i] = self.head  # Propagate head nodes to higher levels
            self.cur_level = new_level
        new_node = SkipListNode(val, new_level)

        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def delete(self, target: int) -> bool:
        """Delete target from skip list.

        Parameters
        ----------
        target: value to be deleted

        Returns
        -------
        """
        update = [None] * (
            self.max_level + 1
        )  # Used to track all nodes whose next should be updated.
        current = self.head

        for level in range(self.cur_level + 1, -1, -1):
            while current.forward[level] and current.forward[level].value < target:
                current = current.forward[level]
            update[level] = current

        current = current.forward[0]
        # Value is not found
        if not current or current.value != target:
            return False
        # From the bottom up update the links until current is not a forward
        for i in range(self.cur_level + 1):
            if update[i].forward[i] != current:
                break
            update[i].forward[i] = current.forward[i]

        # Clean up any left over levels that are empty
        while self.cur_level > 0 and self.head.forward[self.cur_level] is None:
            self.cur_level -= 1
        return True

    def search(self, target: int) -> bool:
        """Search whether target is a member of skip list.

        Returns
        -------
        bool
            True if target exists, False otherwise.

        """
        current = self.head
        # Search each level till the next has esxceeded target. Once exceeded go down to lower level.
        for level in range(self.cur_level, -1, -1):
            while current.forward[level] and current.forward[level].value < target:
                current = current.forward[level]
        current = current.forward[0]

        return current and current.value == target

    def _random_level(self) -> int:
        level = 0
        while random.random() < self.probability and level < self.max_level:
            level += 1
        return level
