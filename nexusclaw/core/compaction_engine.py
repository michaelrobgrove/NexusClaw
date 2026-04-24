class CompactionEngine:
    def __init__(self, soft_token_limit: int = 4000):
        self.soft_token_limit = soft_token_limit

    def should_compact(self, current_token_usage: int) -> bool:
        return current_token_usage >= 0.6 * self.soft_token_limit

    def compact(self, session_history: str) -> str:
        # Placeholder for actual compaction logic using LLM
        # For now, just return a summary string or NO_FLUSH
        if len(session_history) < 100:
            return "NO_FLUSH"
        return "Summary of session decisions, state changes, and blockers."

# Example usage:
# engine = CompactionEngine()
# if engine.should_compact(current_token_usage):
#     summary = engine.compact(session_history)
#     if summary != "NO_FLUSH":
#         # Write summary to memory
#         pass
