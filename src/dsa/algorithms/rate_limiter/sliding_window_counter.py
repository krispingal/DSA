"""Implement a Sliding window counter rate limiter"""

import random
import time
from collections import defaultdict

from src.dsa.algorithms.rate_limiter.rate_limit_abc import RateLimiter


class SlidingWindowCounter(RateLimiter):

    def __init__(self, capacity: int, window_size: int, bucket_size):
        if capacity <= 0 or window_size <= 0 or bucket_size <= 0:
            raise ValueError(
                f"Capacity {capacity}, window size {window_size} and bucket size {bucket_size} must be positive integers"
            )
        if window_size % bucket_size != 0:
            raise ValueError("Window size must be divisible by bucket size")
        self._capacity = capacity
        self._window_size = window_size
        self._bucket_size = bucket_size
        self._buckets = defaultdict(int)
        self._last_checked = time.monotonic()

    def _current_bucket(self) -> int:
        """Determine the current bucket based on the current time."""
        return int(time.monotonic() // self._bucket_size)

    def _clean_old_buckets(self):
        """Clean up buckets that are outside the sliding window."""
        current_bucket = self._current_bucket()
        oldest_bucket = current_bucket - (self._window_size // self._bucket_size)

        buckets_to_remove = [
            bucket for bucket in self._buckets if bucket < oldest_bucket
        ]
        for bucket in buckets_to_remove:
            del self._buckets[bucket]

    def allow_request(self) -> bool:
        """
        Check if request can be allowed.

        Returns:
            bool: True if request should be allowed else False.

        """
        self._clean_old_buckets()
        total_requests = sum(self._buckets.values())
        if total_requests < self._capacity:
            current_bucket = self._current_bucket()
            self._buckets[current_bucket] += 1
            return True
        return False

    def get_state(self) -> dict:
        """ "Return the current state of the rate limiter."""
        return {
            "capacity": self._capacity,
            "window_size": self._window_size,
            "bucket_size": self._bucket_size,
            "buckets": dict(self._buckets),
        }

    def get_rate_limit(self) -> tuple:
        """Returns the rate limit configuration."""
        return self._capacity, self._window_size


if __name__ == "__main__":
    rl = SlidingWindowCounter(
        5, 6, 3
    )  # Sliding window with capacity of 6 requests in the span of 5 secs, and each bucket of 1 sec
    for i in range(20):
        if rl.allow_request():
            print(f"Packet {i} forwarded")
        else:
            print(f"Packet {i} dropped")
        time.sleep(random.random() + 0.6)
