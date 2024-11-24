from collections import defaultdict


def foo(self):
    UF = {}

    def find(x):
        if UF[x] != x:
            UF[x] = find(UF[x])
        return UF[x]

    def union(x, y):
        UF.setdefault(x, x)
        UF.setdefault(y, y)
        UF[find(y)] = find(x)
