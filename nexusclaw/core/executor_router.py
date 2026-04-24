from typing import Dict, Any

class ExecutorRouter:
    def __init__(self):
        self.routing_table = {}

    def register_executor(self, action: str, executor_class):
        self.routing_table[action] = executor_class

    def route(self, intent: Dict[str, Any]):
        action = intent.get('action')
        executor_class = self.routing_table.get(action)
        if not executor_class:
            raise ValueError(f"No executor registered for action: {action}")
        return executor_class()

# Example usage:
# router = ExecutorRouter()
# router.register_executor('lights.control', HomeExecutor)
# executor = router.route(intent)
# result = executor.execute(intent['parameters'])
