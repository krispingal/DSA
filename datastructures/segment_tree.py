class SegmentTree:
    def __init__(self, A: list[int]):
        self.n = len(A)
        self.tree = [0] * 2 * self.n
        self.build_tree(A)

    def build_tree(self, A: list[int]) -> None:
        for i in range(self.n):
            self.tree[i + self.n] = A[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, pos: int, value: int) -> None:
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]

    def query(self, l: int, r: int) -> int:
        res = 0
        l, r = self.n + l, self.n + r + 1
        while l < r:
            if l % 2:
                res += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res


if __name__ == '__main__':
    segmentTree = SegmentTree(range(100))
    assert segmentTree.query(0, 99) == 4950
    segmentTree.update(0, 100)
    segmentTree.update(9, 100)
    assert segmentTree.query(0, 15) == 311
