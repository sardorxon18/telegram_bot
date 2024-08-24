# from aiogram import Bot, Dispatcher
# from asyncio import run
# from funksiyalar import get_user_info
#
# TOKEN = '7519980054:AAFa7Q3WCaAxm9336WRW9q5YNysZvBxyEnU'
# dp = Dispatcher()
#
#
# async def startup_asnwer(bot: Bot):
#     await bot.send_message(chat_id=7266833448, text="salom nima gap⛹️‍♀️✔️")
#
#
# async def shutdown_answer(bot:Bot):
#     await bot.send_message(chat_id=7266833448, text="Bot ish faoliyatini tugatdi🤬")
#
# # @dp.
# # async def echo(message: types.Message, bot: Bot):
# #     await message.copy_to(chat_id=message.chat.id)
#
#
# async def start():
#     dp.startup.register(startup_asnwer)
#     # dp.startup.register()
#     dp.message.register(get_user_info)
#     dp.shutdown.register(shutdown_answer)
#     bot = Bot(token=TOKEN)
#     await dp.start_polling(bot, polling_timeout=10)
#
#
# run(start())


from aiogram import Bot, Dispatcher, types
from asyncio import run
from funksiyalar import get_user_info

TOKEN = '7519980054:AAFa7Q3WCaAxm9336WRW9q5YNysZvBxyEnU'
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(chat_id=7266833448, text="salom nima gap⛹️‍♀️✔️")


async def shutdown_answer(bot: Bot):
    await bot.send_message(chat_id=7266833448, text="Bot ish faoliyatini tugatdi🤬")

# @dp.message_handler()
# async def echo(message: types.Message, bot: Bot):
#     await message.copy_to(chat_id=message.chat.id)


async def start():
    dp.startup.register(startup_answer)
    # dp.startup.register()
    dp.message.register(get_user_info)
    dp.shutdown.register(shutdown_answer)
    await dp.start_polling(bot)


run(start())
