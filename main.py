import logging
import random
from config import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
from button import *
from inline_button import *



# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    photo_file = InputFile(path_or_bytesio="images/rasm.jpg")
    await message.answer_photo(photo_file,caption=f"Assalomu alaykum\n",reply_markup=button)


@dp.message_handler(text = "👁 Kurslar ro'xatini ko'rish 👁")
async def send_welcome(message: types.Message):
    photo_file = InputFile(path_or_bytesio="images/rasm1.png")
    await message.answer_photo(photo_file,caption=f"Kurslar ro'yhati.",reply_markup=kurs)


@dp.message_handler(text = "🤡 Web hacking!")
async def send_welcome(message: types.Message):
    photo_file = InputFile(path_or_bytesio="images/Web.png")
    await message.answer_photo(photo_file,caption=f"Ro'yhatdan o'tmasdan to'lov qilishingiz mumkin.\nTugmani bosib pastga tushing.",reply_markup=payme_web)

@dp.message_handler(text = "Etihical hacking! 🤡")
async def send_welcome(message: types.Message):
    photo_file = InputFile(path_or_bytesio="images/Eth.jpg")
    await message.answer_photo(photo_file,caption=f"Ro'yhatdan o'tmasdan to'lov qilishingiz mumkin.\nTugmani bosib pastga tushing.",reply_markup=payme_eth)

@dp.message_handler(text = "🔙 Bosh menuga qaytish")
async def send_welcome(message: types.Message):
    photo_file = InputFile(path_or_bytesio="images/rasm.jpg")
    await message.answer_photo(photo_file,caption=f"Siz Bosh menudasiz\n",reply_markup=button)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)