import telebot

from bot.config import config
from bot.handlers.handlers import register_handlers


def create_bot():
    bot = telebot.TeleBot(config.BOT_TOKEN)
    register_handlers(bot)
    return bot
