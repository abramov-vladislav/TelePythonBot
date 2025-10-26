import telebot

from bot.utils.helpers import log_user_action


def register_handlers(bot: telebot.TeleBot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        log_user_action(message.from_user.id, 'command_start')
        bot.reply(message, 'Привет, это Telegram бот!')
