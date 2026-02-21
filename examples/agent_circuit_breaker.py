import functools
import time

class CostCircuitBreaker:
    """
    A simple circuit breaker to halt execution if simulated cost exceeds a threshold.
    """
    def __init__(self, max_cost: float):
        self.max_cost = max_cost
        self.current_cost = 0.0

    def check(self, cost_increment: float):
        self.current_cost += cost_increment
        if self.current_cost > self.max_cost:
            raise CostLimitExceededException(f"Circuit Breaker Tripped! Cost {self.current_cost} > Limit {self.max_cost}")

class CostLimitExceededException(Exception):
    pass

# Simulated Decorator for Agent Steps
def monitor_cost(breaker: CostCircuitBreaker, estimated_cost_per_call: float = 0.05):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[CircuitBreaker] Checking budget before executing {func.__name__}...")
            breaker.check(estimated_cost_per_call)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example Usage
if __name__ == "__main__":
    budget = CostCircuitBreaker(max_cost=0.12)
    
    @monitor_cost(budget, estimated_cost_per_call=0.05)
    def agent_step(step_id):
        print(f"Agent executing step {step_id}...")
        time.sleep(0.1)

    try:
        for i in range(5):
            agent_step(i)
    except CostLimitExceededException as e:
        print(f"\n[!] ALERT: {e}")
