import time
import pytest
from unittest.mock import ANY
from src.dsa.algorithms.rate_limiter.token_bucket import TokenBucket
from src.dsa.algorithms.rate_limiter.fixed_window import FixedWindow

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

    def test_token_state(self):
        """Test that state is correctly returned."""
        bucket = TokenBucket(2, 1)
        assert bucket.get_state() == {'capacity': 2, 'rate': 1, 'tokens': 2, 'last checked': ANY}
        bucket.allow_request()
        assert bucket.get_state() == {'capacity': 2, 'rate': 1, 'tokens': 1, 'last checked': ANY}, "State should reflect that tokens has reduced by 1 after consuming 1 token"

    def test_token_rate_limit(self):
        """Test that Token bucket rate limiter returns the correct rate limit."""
        bucket = TokenBucket(3, 4)
        assert bucket.get_rate_limit() == (3, 1), "Should return the rate at which tokens get refilled."

class TestFixedWindow:

    def test_fixed_window(self):
        window = FixedWindow(2, 2)
        window.allow_request()
        assert window.allow_request(), "Should allow two requests"
        assert not window.allow_request(), "Should not allow third request"
        time.sleep(2)
        assert window.allow_request(), "Should allow requests after initial window has passed"

    def test_window_state(self):
        window = FixedWindow(4, 2)
        window.allow_request()
        window.allow_request()
        window.allow_request()
        window.allow_request()
        assert window.get_state() == {'capacity': 4, 'window size': 2, 'counter': 4, 'window start': ANY}
        time.sleep(2)
        window.allow_request()
        assert window.get_state() == {'capacity': 4, 'window size': 2, 'counter': 1, 'window start': ANY}, "Counter resets after window has passed"

    @pytest.mark.xfail(raises=ValueError)
    @pytest.mark.parametrize("params", [(-2, 4), (5, -2)])
    def test_valid_params(self, params):
        window = FixedWindow(*params)
