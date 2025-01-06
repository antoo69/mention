from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["start"]))
async def start_message(client, message):
    buttons = [
        [InlineKeyboardButton("📢 Join Channel", url="https://t.me/yourchannel")],
        [InlineKeyboardButton("💬 Support Group", url="https://t.me/yoursupportgroup")],
    ]
    await message.reply(
        "👋 Halo! Saya adalah bot yang siap membantu Anda. Gunakan perintah berikut:\n\n"
        "/atag - Mention admin\n"
        "/utag - Mention semua anggota\n",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
