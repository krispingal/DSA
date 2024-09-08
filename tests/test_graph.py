import pytest
from dsa.algorithms.dijkstras import Solution


class TestDijkstra:
    def test_cost(self):
        edge_list = [
            ('A', 'B', 5),
            ('A', 'C', 10),
            ('B', 'D', 7),
            ('C', 'D', 3),
            ('D', 'E', 4),
            ('C', 'E', 2)
        ]
        sol = Solution()
        assert sol.dijkstra(edge_list, 4, "A") == {'A': 0, 'B': 5, 'C': 10, 'D': 12, 'E': 12}

