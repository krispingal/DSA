import time
import pytest
from src.dsa.algorithms.token_bucket import TokenBucket

class TestTokenBucket:
    def test_initial_token_bucket_capacity(self):
        """Test that the token bucket starts with full capacity."""
        bucket = TokenBucket(5, 2)
        assert bucket.allow_request() == True, "Token bucket should allow request with full capacity"

    def test_request_reduction(self):
        bucket = TokenBucket(3, 1)  # Bucket with 3 tokens, refills 1 token/sec
        assert bucket.allow_request() == True, "Request 1 should be allowed"
        assert bucket.allow_request() == True, "Request 2 should be allowed"
        assert bucket.allow_request() == True, "Request 3 should be allowed"
        assert bucket.allow_request() == False, "Request 4 should be denied due to lack of tokens"

    def test_token_refill(self):
        """Test that tokens are refilled correctly after some time."""
        bucket = TokenBucket(2, 1)  # 2 tokens capacity, refills 1 token/sec
        bucket.allow_request()
        bucket.allow_request()  # Consumed 2 tokens, bucket should be empty now
        assert bucket.allow_request() == False, "No tokens should be left after two requests"
        time.sleep(1.1)  # Wait for tokens to be refilled
        assert bucket.allow_request() == True, "Token should be refilled after waiting"
