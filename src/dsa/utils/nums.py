from pathlib import Path
import pickle
import random

random.seed(5)
RANDOM_NUMS_FILENAME = 'data/random_nums.pickle'
SORTED_NUMS_FILENAME = 'data/sorted_nums.pickle'


def generate_random_nums(n: int, lo: int, hi: int):
    """
    Returns a list of random nums.
    """
    res = []
    for _ in range(n):
        res.append(random.randrange(lo, hi))
    return res


def write_nums(nums: list[int], filename):
    with open(filename, 'wb') as f:
        pickle.dump(nums, f, pickle.HIGHEST_PROTOCOL)


def read_nums(filename) -> list[int]:
    with open(filename, 'rb') as f:
        nums = pickle.load(f)
        return nums


def get_random_nums() -> list[int]:
    base_path = Path(__file__).parent
    file_path = (base_path / RANDOM_NUMS_FILENAME).resolve()
    try:
        nums = read_nums(file_path)
    except OSError:
        nums = generate_random_nums(1_000, 0, 10_000)
        write_nums(nums, file_path)
    return nums


def get_sorted_nums() -> list[int]:
    base_path = Path(__file__).parent
    file_path = (base_path / SORTED_NUMS_FILENAME).resolve()
    try:
        nums = read_nums(file_path)
    except OSError:
        nums = generate_random_nums(1_000, 0, 10_000)
        nums.sort()
        write_nums(nums, file_path)
    return nums


if __name__ == '__main__':
    x = get_sorted_nums()
    print(x[:10])

