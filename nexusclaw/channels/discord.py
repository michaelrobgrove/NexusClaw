from typing import Callable, Dict, Any

class BaseChannel:
    def __init__(self):
        self.message_handler: Callable[[Dict[str, Any]], None] = lambda x: None

    def set_message_handler(self, handler: Callable[[Dict[str, Any]], None]):
        self.message_handler = handler

    def receive_message(self, message: Dict[str, Any]):
        # Simulate receiving a message and passing it to the handler
        self.message_handler(message)

class DiscordChannel(BaseChannel):
    def __init__(self, bot_token: str, guild_id: str):
        super().__init__()
        self.bot_token = bot_token
        self.guild_id = guild_id

    def start_listening(self):
        # Placeholder for starting Discord event listening
        pass

    def send_message(self, channel_id: str, text: str):
        # Placeholder for sending a message via Discord API
        print(f"Sending message to channel {channel_id}: {text}")

# Example usage:
# discord = DiscordChannel(bot_token='YOUR_BOT_TOKEN', guild_id='YOUR_GUILD_ID')
# discord.set_message_handler(your_message_handler_function)
# discord.start_listening()
