import asyncio
from aiogram import Bot, Dispatcher, types

# --- НАСТРОЙКИ ---
API_TOKEN = '8326400044:AAGHmWeUPi6a0LHTOLFKSepyntyBvX0IKT0'
MY_ID = 123456789  # Узнай свой ID в @userinfobot и вставь сюда

# Ключевые слова
KEYWORDS = ['продам акк', 'продам вк', 'продам тг', 'hbo max', 'продам аккаунт']

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def check_messages(message: types.Message):
    # Проверяем текст сообщения
    text = message.text.lower() if message.text else ""
    
    if any(word in text for word in KEYWORDS):
        # Формируем отчет
        chat_name = message.chat.title or "Личка"
        user = message.from_user.username or message.from_user.id
        
        report = (f"🔍 Нашел объявление!\n"
                  f"📍 Чат: {chat_name}\n"
                  f"👤 Продавец: @{user}\n"
                  f"📝 Текст: {message.text}")
        
        # Пересылаем тебе
        await bot.send_message(MY_ID, report)

async def main():
    print("Бот запущен и ждет сообщений в чатах...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
  
