import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from google_images_search import GoogleImagesSearch
from config import BOT_TOKEN, GOOGLE_TOKEN, GOOGLE_CX, SAVE_IMAGES_DIR

gis = GoogleImagesSearch(GOOGLE_TOKEN, GOOGLE_CX)
bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Привет! Отправь мне запрос...')

@dp.message()
async def search_images(message: Message):
    _search_params = {
        'q': message.text,
        'num': 1
    }

    gis.search(search_params = _search_params)
    for image in gis.results():
        image.download(SAVE_IMAGES_DIR)
        await message.reply_photo(image.url)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())