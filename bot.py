from telegram import Bot

class SecurityBot:
    def __init__(self, token):
        self.bot = Bot(token)

    def send_alert(self, message):
        self.bot.send_message(chat_id='your_chat_id', text=message)
