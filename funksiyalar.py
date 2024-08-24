from aiogram import Bot, types
from aiogram.types import Message


async def get_user_info(message: types.Message, bot: Bot):
    user = await bot.get_chat(message.from_user.id)
    user_photos = await message.from_user.get_profile_photos()
    matn = (f"{message.from_user.mention_html('👉USERNAME👈')} INFO:\n\n"
            f"Ism-Familya: {user.full_name}\n"
            f"ID: {message.from_user.id}\n")
    if user.bio:
        matn += f"Bio: {user.bio}\n"
    if message.from_user.username:
        matn += f"Username: @{message.from_user.username}\n"
    if user_photos.photos:
        await message.answer_photo(user_photos.photos[0][-1].file_id, caption=matn, parse_mode='html')
    else:
        await message.answer(matn, parse_mode='html')
