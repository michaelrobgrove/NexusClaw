import json
import os
from typing import List, Dict, Any

class EventBus:
    def __init__(self, filepath: str):
        self.filepath = filepath
        # Ensure the file exists
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                pass

    def emit(self, event: Dict[str, Any]) -> None:
        """Append an event to the JSONL event log."""
        with open(self.filepath, 'a') as f:
            f.write(json.dumps(event) + '\n')

    def replay(self) -> List[Dict[str, Any]]:
        """Read all events from the JSONL event log."""
        events = []
        with open(self.filepath, 'r') as f:
            for line in f:
                if line.strip():
                    events.append(json.loads(line))
        return events

# Example usage:
# bus = EventBus('data/events.jsonl')
# bus.emit({'id': 'evt_001', 'type': 'message.received', 'payload': {'text': 'Hello'}})
# all_events = bus.replay()
