"""Disjoint Sets Union data structure implementation."""


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        r = x
        while r != self.parent[r]:
            r = self.parent[r]
        while x != r:
            x, self.parent[x] = self.parent[x], r
        return r
    
    def union(self, x: int, y: int) -> None:
        rX, rY = self.find(x), self.find(y)
        if rX == rY: return
        if self.rank[rX] >= self.rank[rY]:
            self.parent[rY] = rX
            self.rank[rX] += 1 if self.rank[rX] == self.rank[rY] else 0
        else:
            self.parent[rX] = rY

