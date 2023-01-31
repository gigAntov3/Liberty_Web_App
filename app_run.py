from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot("6029390680:AAGKHnH2I91rBmuIarPBhrTyDIlXKGpOsGI")
dp = Dispatcher(bot)

def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
   keyboard = InlineKeyboardMarkup(row_width=1) #создаем клавиатуру
   webAppTest = types.WebAppInfo(url = "https://gigantov3.github.io/Liberty_Web_App/") #создаем webappinfo - формат хранения url
   one_butt = InlineKeyboardButton(text="Нажми сюда!!!", web_app=webAppTest) #создаем кнопку типа webapp
   keyboard.add(one_butt) #добавляем кнопки в клавиатуру

   return keyboard #возвращаем клавиатуру

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.chat.id, "Вот то самое приложение...", reply_markup=webAppKeyboard())


executor.start_polling(dp, skip_updates= True)