"""
    Implementation of dijkstras algorithm to find the
    shortest path from a source node to all other nodes.
"""
import math
import heapq
from collections import defaultdict
from typing import Generic, TypeVar

T = TypeVar('T')


class Solution(Generic[T]):
    def dijkstra(self, edge_list: list[tuple[T, T, int]], s: T) -> int:
        """Performs Dijkstra's algorithm to find shortest path from source.

            Args:
                edge_list (list[tuple[T, T, int]]: Edge list in the form [(A, B, 1), (A, C, 3)] => Node 1 has edges to node 2 and node 3 with cost
                s (T): Source node

            Returns:
                dist (int): An array of size n, containing the shortest distance from source node.
        """
        seen = set()
        dist = defaultdict(lambda: math.inf)
        dist[s] = 0
        pq = [(0, s)]
        g = self.get_adjacency_list(edge_list)
        while pq:
            minValue, node = heapq.heappop(pq)
            seen.add(node)
            for dest, cost in g[node].items():
                if dest in seen: continue
                newCost = minValue + cost
                if newCost < dist[dest]:
                    heapq.heappush(pq, (newCost, dest))
                    dist[dest] = newCost
        return dist

    def get_adjacency_list(self, edge_list: list[tuple[T, T, int]]) -> dict[T, dict[T, int]]:
        g = defaultdict(dict)
        for u, v, c in edge_list:
            g[u][v] = c
            g[v][u] = c
        return g

