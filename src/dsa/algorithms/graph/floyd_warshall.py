"""Implements the Floyd-Warshall algorithm."""
import math
from collections import defaultdict
from typing import Generic, TypeVar

T = TypeVar('T')


class Solution:
    def floyd_warshall(self, edge_list: list[tuple[T, T, int]]):
        g = self.get_adjacency_list(edge_list=edge_list)
        dist = defaultdict(lambda: math.inf)
        for u in g:
            for v in g[u]:
                dist[(u, v)] = g[u][v]
        for u in g:
            dist[(u, u)] = 0
        for w in g:
            for u in g:
                for v in g:
                    dist[(u, v)] = min(dist[(u, v)], dist[(u, w)] + dist[(w, v)])
        return dist

    def get_adjacency_list(self, edge_list: list[tuple[T, T, int]]) -> dict[T, dict[T, int]]:
        g = defaultdict(dict)
        for u, v, c in edge_list:
            g[u][v] = c
            g[v][u] = c
        return g
