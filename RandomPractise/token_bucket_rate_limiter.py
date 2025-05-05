"""
**API Rate Limiter:**
    Design and implement a rate limiter for an API. Choose an algorithm (like token bucket, leaky bucket, or fixed window counter) and explain your choice.
API Rate Limiter Design
The Token Bucket is a flexible rate limiting algorithm that allows for bursts of requests up to a configured maximum, smoothing out the rate of incoming requests while maintaining a specified rate over time.

The Token Bucket algorithm works like this:
-------------------------------------------

*   A bucket can hold a certain number of tokens and is refilled with new tokens at a constant rate.
*   When a request comes in, the rate limiter checks if there are enough tokens in the bucket.
*   If there are enough tokens, the request is allowed, and the appropriate number of tokens are removed from the bucket.
*   If there are not enough tokens, the request is denied.
*   The token refill happens at a regular interval which maintains the average allowed rate of requests.

Considerations for the Token Bucket Rate Limiter:
------------------------------------------------
*   Burst Capacity: The bucket size determines the burst capacity. This allows the system to handle spikes in traffic without immediately rejecting excess requests.
    --------------
*   Rate Limiting: The refill rate of the bucket dictates the sustained rate of requests that the system can handle.
    --------------
*   Flexibility: By adjusting the bucket size and refill rate, the rate limiter can be configured for different scenarios.
    ------------
*   Fairness: Requests are allowed based on availability of tokens, which prevents a single source from dominating the API usage if the bucket is shared.
    ---------
"""

import time
import threading

class TokenBucket:
    """
        tokens: The total capacity of the bucket.
        fill_rate: Rate at which the bucket will be refilled (tokens per second).
    """
    def __init__(self, tokens, fill_rate) -> None:
        self.capacity = tokens
        self._tokens = tokens
        self.fill_rate = fill_rate
        self.lock = threading.Lock()
        self.timestamp = time.monotonic()
    
    def allow_request(self, tokens_requested=1):
        """
        tokens_requested: Number of tokens requested per incoming API call.
        Returns True if the request is allowed, False otherwise.
        """
        with self.lock:
            # First calculate the number of tokens to be added, sicne last request
            now = time.monotonic()
            time_elapsed = now - self.timestamp
            add_tokens = time_elapsed * self.fill_rate

            # Update the number of tokens
            self._tokens = min(self.capacity, self._tokens + add_tokens)

            # If enough tokens are available, allow the request
            if self._tokens >= tokens_requested:
                self._tokens -= tokens_requested
                return True
            return False


# Example Usage  with Bucket size 10 tokens, refill 1 token per second

rate_limiter = TokenBucket(tokens=1, fill_rate=1)

def send_request():
    if rate_limiter.allow_request():
        print("Allowed. send request now")
        return True
    else:
        print("Not Allowed, Rejected")
        return False

if __name__ == "__main__":
    success_count = 0
    for _ in range(15):
        if send_request():
            success_count += 1
            print("Hello", success_count)
            time.sleep(0.1) # Simulate a request every 100 milliseconds
    print(f"{success_count} number of requests out of 15 got filled")

    time.sleep(10)

    success_count_wait = 0
    for _ in range(15):
        if send_request():
            success_count_wait += 1
            # print("Hello", success_count_wait)
            time.sleep(0.1) # Simulate a request every 100 milliseconds
    print(f"After Sleeping for 10 seconds, {success_count_wait} number of requests out of 15 got filled")
