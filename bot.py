from aiogram import Dispatcher, Bot, types

TOKEN = '5675840357:AAEink0QilMecgu_yS30q5yjLVHzehhbrSg'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}")

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


