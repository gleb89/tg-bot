from aiogram import Dispatcher, Bot, types

TOKEN = '5675840357:AAEink0QilMecgu_yS30q5yjLVHzehhbrSg'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    my_ads = types.KeyboardButton(f'Мои обьявления 💸')
    button_add_apartament = types.KeyboardButton('Жилье 💱')
    button_uslugi = types.KeyboardButton('Услуги💱')
    button_veschi = types.KeyboardButton('Вещи💱')
    greet_kb1 = types.ReplyKeyboardMarkup(
            resize_keyboard=True
        ).add(
            button_add_apartament,
            button_veschi,
           
            button_uslugi,
            my_ads
            
            )
   
    await message.reply(
        f'Привет!{message.from_user.first_name}',
         reply_markup = greet_kb1 
        )

@dp.message_handler()
async def start(message: types.Message):
    """
    {
        "message_id": 19, 
        "from": 
        {"id": 321044549, "is_bot": false, "first_name": "Gleb", "username": "hleb89", "language_code": "ru"}, 
        "chat": {"id": 321044549, "first_name": "Gleb", "username": "hleb89", "type": "private"}, 
        "date": 1666899794, "text": "rrrrrr"}
    """
    print(message.text)
    await message.answer(f"ответил, {message.from_user.full_name}, {message.text}")


@dp.callback_query_handler()
async def callback_inline(call:types.CallbackQuery):
    """
    Отслеживает нажатия кнопок
    """
    await call.message.answer("Успешно отменено!")


