import random
from typing import TypeVar, Optional

T = TypeVar("T")


class Sampler[T]:
    """Reservoir sampling implementation that maintains a single sample."""

    def __init__(self):
        self._num_seen: int = 0
        self._cur: Optional[T] = None

    def sample(self, value: T) -> None:
        """
        Process a new value, potentially updating the current sample.

        Args:
            value: The new value to potentially sample
        """
        self._num_seen += 1
        if random.randint(1, self._num_seen) == 1:
            self._cur = value
            print(f"Updated value to {value}")

    @property
    def value(self) -> T:
        if self._num_seen == 0:
            raise ValueError("No items have been sampled yet")
        return self._cur


if __name__ == "__main__":
    sampler = Sampler[str]()
    movies = [
        "Seven Samurai",
        "Rashomon",
        "Yojimbo",
        "Ran",
        "The Hidden Fortress",
        "Red Beard",
        "Sanjuro",
        "Ran",
    ]
    for movie in movies:
        sampler.sample(movie)

    print(sampler.value)
