from pyrogram import Client
from bot.modules import tag_module
from start import start_message
from config import API_ID, API_HASH, BOT_TOKEN

def run_bot():
    app = Client(
        "my_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN
    )

    # Tambahkan handler
    app.add_handler(start_message)
    app.add_handler(tag_module.tag_admins)
    app.add_handler(tag_module.tag_all)
    app.add_handler(tag_module.stop_tag_all)

    # Jalankan bot
    print("Bot berjalan...")
    app.run()
