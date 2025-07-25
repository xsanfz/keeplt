from aiogram import types
from storage_log import get_items

async def my_items_handler(message: types.Message):
    items = await get_items(message.from_user.id)
    if not items:
        await message.answer("У вас нет вещей на хранении.")
    else:
        await message.answer("Ваши вещи на хранении:\n" + "\n".join(f"• {item}" for item in items)) 
