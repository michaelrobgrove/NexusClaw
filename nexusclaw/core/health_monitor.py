import time
from typing import Dict, Any

class HealthMonitor:
    def __init__(self):
        self.agent_status = {}
        self.channel_status = {}
        self.circuit_breakers = {}
        self.last_errors = []

    def update_agent_status(self, agent_id: str, status: str):
        self.agent_status[agent_id] = status

    def update_channel_status(self, channel_id: str, status: str):
        self.channel_status[channel_id] = status

    def update_circuit_breaker(self, executor_name: str, state: str):
        self.circuit_breakers[executor_name] = state

    def log_error(self, error: Dict[str, Any]):
        timestamp = time.time()
        self.last_errors.append({"timestamp": timestamp, **error})
        # Keep only last 10 errors
        if len(self.last_errors) > 10:
            self.last_errors.pop(0)

    def get_status(self) -> Dict[str, Any]:
        return {
            "agents": self.agent_status,
            "channels": self.channel_status,
            "circuit_breakers": self.circuit_breakers,
            "last_errors": self.last_errors
        }

# Example usage:
# monitor = HealthMonitor()
# monitor.update_agent_status('home-agent', 'running')
# status = monitor.get_status()
# print(status)
