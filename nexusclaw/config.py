import toml
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = {}

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        with open(self.config_path, 'r') as f:
            raw_config = toml.load(f)
        self.config = self._apply_defaults(raw_config)
        return self.config

    def _apply_defaults(self, raw_config: Dict[str, Any]) -> Dict[str, Any]:
        # Define default config values here
        defaults = {
            'llm_provider': 'ollama',
            'llm_base_url': 'http://localhost:11434',
            'llm_model_fast': 'phi3',
            'llm_model_standard': 'mistral',
            'llm_model_power': None,
            'ha_url': None,
            'ha_token': None,
            'telegram_bot_token': None,
            'discord_bot_token': None,
            'discord_guild_id': None,
            'cf_tunnel_token': None,
            'tailscale_auth_key': None,
            'low_end_mode': False,
            'context_soft_limit_tokens': 4000,
            'circuit_breaker_threshold': 3,
            'circuit_breaker_cooldown_seconds': 900,
            'executor_timeout_seconds': 5
        }
        # Merge raw config with defaults, ignoring unknown keys
        merged = {}
        for key, default_value in defaults.items():
            merged[key] = raw_config.get(key, default_value)
        return merged

# Example usage:
# loader = ConfigLoader('/path/to/config.toml')
# config = loader.load()
# print(config)
