"""Implementation of Token Bucket rate limiting algorithm."""
import time


class TokenBucket:
    def __init__(self, capacity: int, rate: int):
        """

        Args:
            capacity: Maximum number of tokens the bucket can hold at a time.
            rate: Rate (token per second) at which tokens are added.
        """
        self._capacity = capacity
        self._rate = rate
        self._tokens = capacity
        self._last_checked = time.time()

    def _add_tokens(self) -> None:
        """Adds token to bucket based on how much time elapsed after last check."""
        elapsed = time.time() - self._last_checked
        self._tokens = min(int(elapsed * self._rate) + self._tokens, self._capacity)
        self._last_checked = time.time()

    def allow_request(self, tokens_needed: int = 1) -> bool:
        """  Check if request can be allowed.

        Args:
            tokens_needed: Number of tokens required for operation.

        Returns:

        """
        self._add_tokens()
        if self._tokens >= tokens_needed:
            self._tokens -= tokens_needed
            return True
        return False

if __name__ == '__main__':
    rl = TokenBucket(5, 2) # Bucket with capacity 5 tokens, rate of 2 tokens/sec
    for i in range(20):
        if rl.allow_request():
            print(f"Packet {i} forwarded")
        else:
            print(f"Packet {i} dropped")
        time.sleep(0.2)




