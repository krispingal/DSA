from random import randrange


def random_shuffle(A: list) -> list:
    """Shuffle the list

    Args:
        A: list of values that needs to be shuffled.

    """
    for i in range(len(A) - 1, 0, -1):
        r = randrange(i+1)
        A[i], A[r] = A[r], A[i]
    return A
