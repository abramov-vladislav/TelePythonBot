from bot.bot import create_bot

if __name__ == '__main__':
    bot = create_bot()
    print("Бот запущен...")
    bot.polling(none_stop=True)