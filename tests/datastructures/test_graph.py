import pytest
from src.dsa.algorithms.graph.dijkstras import Solution as Dijkstra
from src.dsa.algorithms.graph.floyd_warshall import Solution as FloydWarshall


@pytest.fixture
def edge_list():
    edge_list = [
        ('A', 'B', 5),
        ('A', 'C', 10),
        ('B', 'D', 7),
        ('C', 'D', 3),
        ('D', 'E', 4),
        ('C', 'E', 2),
        ('F', 'G', 3)
    ]
    return edge_list

@pytest.fixture
def tiny_edge_list():
    edge_list = [
        ('A', 'B', 5),
        ('A', 'C', 10),
        ('B', 'D', 7),
        ('C', 'D', 3)
    ]
    return edge_list


class TestDijkstra:
    def test_cost(self, edge_list):
        sol = Dijkstra()
        assert sol.dijkstra(edge_list, "A") == {'A': 0, 'B': 5, 'C': 10, 'D': 12, 'E': 12}


class TestFloydWarshall:
    def test_cost(self, tiny_edge_list):
        sol = FloydWarshall()
        assert sol.floyd_warshall(tiny_edge_list) == {
            ('A', 'B'): 5, ('A', 'C'): 10, ('B', 'A'): 5, ('B', 'D'): 7, ('C', 'A'): 10, 
            ('C', 'D'): 3, ('D', 'B'): 7, ('D', 'C'): 3, ('A', 'A'): 0, ('B', 'B'): 0, 
            ('C', 'C'): 0, ('D', 'D'): 0, ('A', 'D'): 12, ('B', 'C'): 10, ('C', 'B'): 10, 
            ('D', 'A'): 12
        }

