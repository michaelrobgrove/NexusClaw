from typing import Callable, Dict, Any

class BaseChannel:
    def __init__(self):
        self.message_handler: Callable[[Dict[str, Any]], None] = lambda x: None

    def set_message_handler(self, handler: Callable[[Dict[str, Any]], None]):
        self.message_handler = handler

    def receive_message(self, message: Dict[str, Any]):
        # Simulate receiving a message and passing it to the handler
        self.message_handler(message)

class TelegramChannel(BaseChannel):
    def __init__(self, bot_token: str):
        super().__init__()
        self.bot_token = bot_token

    def start_polling(self):
        # Placeholder for starting Telegram polling
        pass

    def send_message(self, chat_id: str, text: str):
        # Placeholder for sending a message via Telegram API
        print(f"Sending message to {chat_id}: {text}")

# Example usage:
# telegram = TelegramChannel(bot_token='YOUR_BOT_TOKEN')
# telegram.set_message_handler(your_message_handler_function)
# telegram.start_polling()
