from src.dsa.datastructures.skip_lists import SkipList


class TestSkipList:

    def test_insert(self):
        skiplist = SkipList()
        skiplist.insert(10)
        assert skiplist.search(10), "Expected element to be inserted into skiplist"

    def test_delete(self):
        skiplist = SkipList()
        skiplist.insert(10)
        assert skiplist.delete(10), "Expected element to be deleted successfully"
        assert not skiplist.search(
            10
        ), "Expected search to fail after element is deleted"

    def test_search_empty_skiplist(self):
        skiplist = SkipList()
        assert not skiplist.delete(5), "Expected delete to fail with empty skiplist"

    def test_probabilistic_leveling(self):
        skiplist = SkipList(max_level=10, probability=0.5)
        num_elements = 1000
        levels = []

        for _ in range(num_elements):
            level = skiplist._random_level()
            levels.append(level)

        actual_avg_level = sum(levels) / num_elements
        print(actual_avg_level)
        # Expected average level based on geometric distribution with p = 0.5
        expected_avg = (1 / (1 - skiplist.probability)) - 1
        assert (
            abs(actual_avg_level - expected_avg) < 1
        ), f"Expected average level ~{expected_avg}, but got {actual_avg_level}"
