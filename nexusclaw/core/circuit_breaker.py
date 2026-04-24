import time

class CircuitBreaker:
    def __init__(self, threshold: int = 3, cooldown_seconds: int = 900):
        self.threshold = threshold
        self.cooldown_seconds = cooldown_seconds
        self.failure_count = 0
        self.last_failure_time = 0
        self.circuit_open = False

    def record_failure(self):
        now = time.time()
        if self.circuit_open and now - self.last_failure_time > self.cooldown_seconds:
            # Reset circuit after cooldown
            self.circuit_open = False
            self.failure_count = 0

        self.failure_count += 1
        self.last_failure_time = now

        if self.failure_count >= self.threshold:
            self.circuit_open = True

    def is_open(self) -> bool:
        if self.circuit_open:
            now = time.time()
            if now - self.last_failure_time > self.cooldown_seconds:
                # Reset circuit after cooldown
                self.circuit_open = False
                self.failure_count = 0
                return False
            return True
        return False

    def reset(self):
        self.circuit_open = False
        self.failure_count = 0
        self.last_failure_time = 0

# Example usage:
# cb = CircuitBreaker()
# cb.record_failure()
# if cb.is_open():
#     print("Circuit is open, stop retries")
# else:
#     print("Circuit is closed, proceed")
